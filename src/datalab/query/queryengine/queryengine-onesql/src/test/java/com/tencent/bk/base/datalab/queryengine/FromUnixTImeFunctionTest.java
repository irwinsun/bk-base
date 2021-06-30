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

package com.tencent.bk.base.datalab.queryengine;

import com.google.common.collect.Maps;
import com.tencent.bk.base.datalab.bksql.validator.SemanticTestSupporter;
import com.tencent.bk.base.datalab.queryengine.func.date.FromUnixTimeFunction;
import java.util.Map;
import org.apache.calcite.schema.Function;
import org.apache.calcite.schema.impl.ScalarFunctionImpl;
import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;

public class FromUnixTImeFunctionTest extends SemanticTestSupporter {

    @BeforeClass
    public static void beforeClass() {
        SemanticTestSupporter.initReader(null, null);
    }

    @Test
    public void test1() {
        String sql = "SELECT FROM_UNIXTIME(dtEventTimeStamp/1000, \"%Y-%m-%d %H:%i:00\") FROM "
                + "tab";
        Assert.assertFalse(check(sql));
    }

    @Test
    public void test2() {
        String sql = "SELECT FROM_UNIXTIME(dtEventTimeStamp/1000, \"%Y-%m-%d %H:%i:00\") FROM "
                + "tab";
        Map<String, Function> udtMap = Maps.newHashMap();
        udtMap.putIfAbsent("from_unixtime",
                ScalarFunctionImpl.create(FromUnixTimeFunction.class, "from_unixtime"));
        addFunction(udtMap);
        Assert.assertTrue(check(sql));
    }
}
