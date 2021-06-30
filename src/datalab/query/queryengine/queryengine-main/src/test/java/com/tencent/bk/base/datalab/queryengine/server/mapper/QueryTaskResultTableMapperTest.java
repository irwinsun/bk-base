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

package com.tencent.bk.base.datalab.queryengine.server.mapper;

import com.tencent.bk.base.datalab.queryengine.server.constant.CommonConstants;
import com.tencent.bk.base.datalab.queryengine.server.model.QueryTaskResultTable;
import com.tencent.bk.base.datalab.queryengine.server.util.ModelUtil;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
@EnableAutoConfiguration
public class QueryTaskResultTableMapperTest {

    @Autowired
    private ModelUtil modelUtil;

    @Autowired
    private QueryTaskResultTableMapper queryTaskResultTableMapper;

    @Before
    public void before() {
        modelUtil.truncateTb(CommonConstants.TB_DATAQUERY_QUERYTASK_RESULT_TABLE);
        modelUtil.addQueryTaskResultTable();
    }

    @After
    public void after() {
        modelUtil.truncateTb(CommonConstants.TB_DATAQUERY_QUERYTASK_RESULT_TABLE);
    }

    @Test
    public void insert() {
        QueryTaskResultTable queryTaskResultTable = new QueryTaskResultTable();
        queryTaskResultTable.setActive(1);
        queryTaskResultTable.setResultTableId("tab");
        queryTaskResultTable.setQueryId("aaa");
        queryTaskResultTable.setPhysicalTableName("test");
        queryTaskResultTable.setClusterName("default");
        queryTaskResultTable.setPriority(1);
        queryTaskResultTable.setClusterType("mysql");
        queryTaskResultTable.setClusterGroup("testgroup");
        queryTaskResultTable.setConnectionInfo("{}");
        queryTaskResultTable.setStorageConfig("{}");
        queryTaskResultTable.setStorageClusterConfigId(1);
        queryTaskResultTable.setCreatedBy("zhangsan");
        queryTaskResultTable.setVersion("v1");
        queryTaskResultTable.setDescription("just 4 test");
        int rows = queryTaskResultTableMapper.insert(queryTaskResultTable);
        Assert.assertTrue(queryTaskResultTable.getId() > 0);
        Assert.assertTrue(rows == 1);
    }

    @Test
    public void update() {
        QueryTaskResultTable queryTaskResultTable = new QueryTaskResultTable();
        queryTaskResultTable.setId(1);
        queryTaskResultTable.setActive(1);
        queryTaskResultTable.setResultTableId("tab");
        queryTaskResultTable.setQueryId("aaa");
        queryTaskResultTable.setPhysicalTableName("test");
        queryTaskResultTable.setClusterName("default");
        queryTaskResultTable.setPriority(1);
        queryTaskResultTable.setClusterType("mysql");
        queryTaskResultTable.setClusterGroup("testgroup");
        queryTaskResultTable.setConnectionInfo("{}");
        queryTaskResultTable.setStorageConfig("{}");
        queryTaskResultTable.setStorageClusterConfigId(1);
        queryTaskResultTable.setUpdatedBy("zhangsan");
        queryTaskResultTable.setVersion("v1");
        queryTaskResultTable.setDescription("just 4 test");
        int rows = queryTaskResultTableMapper.update(queryTaskResultTable);
        Assert.assertTrue(rows == 1);
    }
}