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

package com.tencent.bk.base.dataflow.spark.sql.pipeline

import com.tencent.bk.base.dataflow.core.topo.Topology
import com.tencent.bk.base.dataflow.spark.dmonitor.DMonitor
import com.tencent.bk.base.dataflow.spark.exception.{BatchInputNoDataException, BatchOutputNoDataException}
import com.tencent.bk.base.dataflow.spark.pipeline.BatchPipeline
import com.tencent.bk.base.dataflow.spark.sql.runtime.BatchOneTimeSQLRuntime
import com.tencent.bk.base.dataflow.spark.topology.BatchTopology
import com.tencent.bk.base.dataflow.spark.exception.BatchOutputNoDataException

class BatchOneTimeSQLPipeline(topology: Topology)
  extends BatchPipeline(topology.asInstanceOf[BatchTopology]) {

  override def createRuntime(): BatchOneTimeSQLRuntime = {
    new BatchOneTimeSQLRuntime(this.topology.asInstanceOf[BatchTopology])
  }

  override def afterSource(): Unit = {
    this.updateMetricsInput()
    if (DMonitor.isInputEmpty()) {
      throw new BatchInputNoDataException("上级数据节点没有数据输出")
    }
  }

  override def afterTransform(): Unit = {

  }

  override def afterSink(): Unit = {
    this.updateMetricsOutput()
    if (DMonitor.isOutputEmpty()) {
      throw new BatchOutputNoDataException("计算结果无数据，请检查SQL。")
    }
  }
}

