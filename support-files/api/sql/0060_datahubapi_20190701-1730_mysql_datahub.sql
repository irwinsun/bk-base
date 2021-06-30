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

CREATE DATABASE IF NOT EXISTS bkdata_basic;

USE bkdata_basic;

SET NAMES utf8;

CREATE TABLE `storage_cron_task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `trigger_time` int(11) NOT NULL COMMENT '触发时间，精确到分钟',
  `task_type` varchar(32) NOT NULL COMMENT '任务类型名称，比如es_maintain，hdfs_maintain',
  `status` varchar(64) NOT NULL COMMENT '状态(成功，失败，运行中)',
  `begin_time` datetime(6) DEFAULT NULL COMMENT '开始时间',
  `end_time` datetime(6) DEFAULT NULL COMMENT '结束时间',
  `created_by` varchar(128) NOT NULL COMMENT '创建人',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `description` text COMMENT '备注信息',
  PRIMARY KEY (`id`),
  UNIQUE KEY `trigger_task` (`trigger_time`, `task_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='存储定时任务';

