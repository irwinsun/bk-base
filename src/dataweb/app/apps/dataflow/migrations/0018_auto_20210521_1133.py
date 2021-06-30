# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making BK-BASE 蓝鲸基础计算平台 available.
Copyright (C) 2019 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""
# Generated by Django 2.2.6 on 2021-05-21 03:33


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dataflow", "0017_auto_20200710_1657"),
    ]

    operations = [
        migrations.AlterField(
            model_name="useroperaterecord",
            name="operate_type",
            field=models.CharField(
                choices=[("ProjectViewSet.create", "创建项目")], db_index=True, max_length=64, verbose_name="操作类型"
            ),
        ),
    ]