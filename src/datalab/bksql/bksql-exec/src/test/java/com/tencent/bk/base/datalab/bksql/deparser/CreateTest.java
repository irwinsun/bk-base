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

package com.tencent.bk.base.datalab.bksql.deparser;

import com.tencent.bk.base.datalab.bksql.protocol.BaseProtocolPlugin;
import com.typesafe.config.ConfigFactory;
import org.hamcrest.core.IsEqual;
import org.junit.Test;

public class CreateTest extends DeParserTestSupport {

    @Test
    public void test1() throws Exception {
        final String sql = "create table tab as select * from tab1";
        final String expected = "CREATE TABLE tab AS SELECT * FROM tab1";
        assertThat(new Sql(ConfigFactory.empty(), BaseProtocolPlugin.EMPTY_WALKER_CONFIG), sql,
                new IsEqual<>(expected));
    }

    @Test
    public void test2() throws Exception {
        final String sql = "create table tab as select * from tab1 order by id limit 1";
        final String expected = "CREATE TABLE tab AS SELECT * FROM tab1 ORDER BY id "
                + "LIMIT 1";
        assertThat(new Sql(ConfigFactory.empty(), BaseProtocolPlugin.EMPTY_WALKER_CONFIG), sql,
                new IsEqual<>(expected));
    }

    @Test
    public void test3() throws Exception {
        final String sql = "create table tab as (select a.* from tab1 a join "
                + "tab2 b on(a.id=b.id))";
        final String expected = "CREATE TABLE tab AS SELECT a.* FROM tab1 AS a INNER "
                + "JOIN tab2 AS b ON (a.id = b.id)";
        assertThat(new Sql(ConfigFactory.empty(), BaseProtocolPlugin.EMPTY_WALKER_CONFIG), sql,
                new IsEqual<>(expected));
    }
}
