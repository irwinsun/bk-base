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

package com.tencent.bk.base.dataflow.bksql.udf;

import java.util.List;
import org.apache.flink.api.common.typeinfo.TypeInformation;
import org.apache.flink.table.api.Types;
import org.apache.flink.table.functions.AggregateFunction;

public abstract class AbstractFlinkUdaf extends AggregateFunction<Object, AbstractFlinkUdaf.DummyAccum> {

    private final List<String> outputTypes;

    public AbstractFlinkUdaf(List<String> outputTypes) {
        this.outputTypes = outputTypes;
    }

    @Override
    public DummyAccum createAccumulator() {
        return new DummyAccum();
    }

    @Override
    public Object getValue(DummyAccum acc) {
        return null;
    }

    public void merge(DummyAccum acc, Iterable<DummyAccum> it) {

    }

    public void resetAccumulator(DummyAccum acc) {

    }

    @Override
    public TypeInformation getResultType() {
        return generateOutputTypes();
    }

    private TypeInformation<?> generateOutputTypes() {
        switch (outputTypes.get(0).toLowerCase()) {
            case "string":
                return Types.STRING();
            case "boolean":
                return Types.BOOLEAN();
            case "int":
                return Types.INT();
            case "long":
                return Types.LONG();
            case "float":
                return Types.FLOAT();
            case "double":
                return Types.DOUBLE();
            default:
                throw new RuntimeException("Don't support the type " + outputTypes.get(0).toLowerCase());
        }
    }

    public static class DummyAccum {

    }
}
