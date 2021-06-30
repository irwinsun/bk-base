# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making BK-BASE 蓝鲸基础平台 available.
Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.
BK-BASE 蓝鲸基础平台 is licensed under the MIT License.
License for BK-BASE 蓝鲸基础平台:
--------------------------------------------------------------------
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import time

from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

from datamanage.utils.drf import GeneralSerializer
from datamanage.pro.dataquality.models.audit import EventTypeConfig, DataQualityEventTemplateVariable
from datamanage.pro.dataquality.serializers.base import DataQualityDataSetSerializer


class DataQualitySummarySerializer(DataQualityDataSetSerializer):
    field = serializers.CharField(required=False, allow_null=True, label=_('字段名称'))
    with_current = serializers.BooleanField(required=False, default=False, label=_('是否获取当前值'))
    with_whole = serializers.BooleanField(required=False, default=False, label=_('是否获取全量'))


class DataQualityEventListSerializer(DataQualityDataSetSerializer):
    start_time = serializers.IntegerField(required=False, label=_('开始时间'), default=int(time.time()) - 86400)
    end_time = serializers.IntegerField(required=False, label=_('结束时间'), default=int(time.time()))


class EventTypeConfigSerializer(GeneralSerializer):
    class Meta:
        model = EventTypeConfig


class DataQualityEventTemplateVariableSerializer(GeneralSerializer):
    class Meta:
        model = DataQualityEventTemplateVariable
