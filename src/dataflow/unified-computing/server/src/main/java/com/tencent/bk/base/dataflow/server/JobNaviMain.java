/*
 * Tencent is pleased to support the open source community by making BK-BASE 蓝鲸基础平台 available.
 *
 * Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.
 *
 * BK-BASE 蓝鲸基础平台 is licensed under the MIT License.
 *
 * License for BK-BASE 蓝鲸基础平台:
 * --------------------------------------------------------------------
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
 * documentation files (the "Software"), to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
 * and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all copies or substantial
 * portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
 * LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
 * NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
 * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

package com.tencent.bk.base.dataflow.server;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.tencent.bk.base.dataflow.core.conf.ConstantVar;
import com.tencent.bk.base.dataflow.core.topo.ITopoParamMaker;
import com.tencent.bk.base.dataflow.jobnavi.api.JobNaviTask;
import com.tencent.bk.base.dataflow.jobnavi.state.event.EventListener;
import com.tencent.bk.base.dataflow.jobnavi.state.event.TaskEvent;
import java.lang.reflect.Constructor;
import java.util.HashMap;
import java.util.Map;


public class JobNaviMain implements JobNaviTask {

    @Override
    public void run(TaskEvent taskEvent) throws Throwable {
        String scheduleId = taskEvent.getContext().getTaskInfo().getScheduleId();
        Long scheduleTime = taskEvent.getContext().getTaskInfo().getScheduleTime();
        String extraInfo = taskEvent.getContext().getTaskInfo().getExtraInfo();
        Long execId = taskEvent.getContext().getExecuteInfo().getId();
        ObjectMapper objectMapper = new ObjectMapper();
        Map<String, Object> parameters = objectMapper.readValue(extraInfo, HashMap.class);

        String jobTypeStr = taskEvent.getContext().getTaskInfo().getType().getName();
        parameters.put("schedule_id", scheduleId);
        parameters.put("schedule_time", scheduleTime);
        parameters.put("exec_id", execId);

        ConstantVar.Component jobType = ConstantVar.Component.valueOf(jobTypeStr);
        // add for spark and hive
        parameters.put("job_type", jobType.toString());
        String configContent = null;
        ITopoParamMaker maker;
        switch (jobType) {
            case spark_sql:
                if (parameters.get("params") != null && "udf_debug"
                        .equals(((Map<String, Object>) parameters.get("params")).get("run_mode"))) {
                    Map<String, Object> info = (Map<String, Object>) parameters.get("info");
                    Map<String, Object> params = (Map<String, Object>) info.get("params");
                    params.put("schedule_id", scheduleId);
                    params.put("schedule_time", scheduleTime);
                    params.put("exec_id", execId);
                    configContent = objectMapper.writeValueAsString(parameters);
                    Main.main(new String[]{configContent});
                    return;
                }
                maker = getTopoParamMaker("com.tencent.bk.base.dataflow.spark.sql.topo.SparkTopoParamMaker");
                break;
            default:
                maker = null;
        }

        Object license = parameters.get("license");
        if (license == null) {
            if (maker != null) {
                configContent = maker.getConfigContent(parameters);
            }
            Main.main(new String[]{configContent});
        } else {
            String licenseContent = objectMapper.writeValueAsString(license);
            parameters.remove("license");
            if (maker != null) {
                configContent = maker.getConfigContent(parameters);
            }
            Main.main(new String[]{configContent, licenseContent});
        }
    }


    private ITopoParamMaker getTopoParamMaker(String classStr) {
        try {
            Class pipelineClass = Class.forName(classStr);
            Constructor constructor = pipelineClass.getConstructor();
            return (ITopoParamMaker) constructor.newInstance();
        } catch (Exception e) {
            throw new RuntimeException(String.format("The class %s is not found.", classStr));
        }
    }


    @Override
    public EventListener getEventListener(String s) {
        return null;
    }
}
