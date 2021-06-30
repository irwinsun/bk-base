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

package com.tencent.bk.base.datahub.databus.pipe.assign;

import com.tencent.bk.base.datahub.databus.pipe.Context;
import com.tencent.bk.base.datahub.databus.pipe.EtlConsts;
import com.tencent.bk.base.datahub.databus.pipe.Node;
import com.tencent.bk.base.datahub.databus.pipe.exception.NotMapDataError;
import com.tencent.bk.base.datahub.databus.pipe.exception.PipeExtractorException;
import com.tencent.bk.base.datahub.databus.pipe.record.Field;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AssignObj extends Node {

    // 字段名到key的映射
    private Map<String, List<String>> varname2key;
    // 字段名到字段对象的映射
    private Map<String, Field> varname2field;

    /**
     * 对象赋值.
     */
    public AssignObj(Context ctx, Map<String, Object> config) {
        nodeConf = config;
        generateNodeLabel();

        varname2key = new HashMap<String, List<String>>();
        varname2field = new HashMap<String, Field>();
        List<Map<String, Object>> assignConf = (List<Map<String, Object>>) nodeConf.get(EtlConsts.ASSIGN);

        for (Map<String, Object> kv : assignConf) {
            String varName = (String) kv.get(EtlConsts.ASSIGN_TO);
            String type = kv.containsKey(EtlConsts.TYPE) ? ((String) kv.get(EtlConsts.TYPE)) : EtlConsts.STRING;
            Boolean isDimension = kv.containsKey(EtlConsts.IS_DIMENSION) ? true : false;
            Field field = new Field(varName, type, isDimension);

            if (!varname2key.containsKey(varName)) {
                varname2key.put(varName, new ArrayList<String>());
            }
            varname2key.get(varName).add((String) kv.get(EtlConsts.KEY));

            if (!varname2field.containsKey(varName)) {
                varname2field.put(varName, field);

                ctx.getSchema().append(field);
            }
        }
    }

    @Override
    public boolean validateNext() {
        return true;
    }

    @SuppressWarnings("unchecked")
    @Override
    public Object execute(Context ctx, Object o) {
        if (!(o instanceof Map)) {
            ctx.setNodeDetail(label, null);
            String errMsg = String.format("%s: %s not Map, can't assign by key", NotMapDataError.class.getSimpleName(),
                    o.getClass().getSimpleName());
            ctx.setNodeError(label, String.format("%s", NotMapDataError.class.getSimpleName()));
            throw new NotMapDataError(errMsg);
        }

        Map<String, Object> map = (Map<String, Object>) o;
        Map<String, Object> nodeResult = new HashMap<>();

        for (Map.Entry<String, List<String>> entry : varname2key.entrySet()) {
            List<String> keys = entry.getValue();
            Field field = varname2field.get(entry.getKey());

            // 按照目标对象类型对数据进行转换,如果转换失败,则默认使用null值填充
            Object value = null;
            try {
                value = field.castType(getFirst(map, keys));
            } catch (PipeExtractorException e) {
                ctx.appendBadValues(o, e);
            }
            ctx.setValue(field, value);
            nodeResult.put(field.getName(), value);
        }

        ctx.setNodeDetail(label, nodeResult);

        return null;
    }

    /**
     * 给定key列表，通过遍历，返回字典中第一个找到key的值，否则返回null
     */
    private Object getFirst(Map<String, Object> map, List<String> keys) {

        for (String key : keys) {
            Object o = map.get(key);
            if (o != null) {
                return o;
            }
        }
        return null;
    }
}

