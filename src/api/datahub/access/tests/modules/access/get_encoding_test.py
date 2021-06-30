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

import json

import pytest
from datahub.access.tests.modules.access.conftest import test_field_type  # noqa
from datahub.access.tests.utils import get
from datahub.databus.tests import conftest  # noqa


@pytest.mark.httpretty
@pytest.mark.django_db
@pytest.mark.skip
@pytest.mark.usefixtures("test_field_type")
def test_ok():
    """业务ID不为数字"""
    res = get("/v3/access/encode/")
    compare_json = {
        "code": "1500200",
        "data": [
            {
                "id": 1,
                "active": 1,
                "created_at": "2018-10-23 12:02:18",
                "created_by": "admin",
                "description": "",
                "encoding_alias": "UTF8",
                "encoding_name": "UTF8",
                "updated_at": "2018-10-23 12:02:18",
                "updated_by": "admin",
            }
        ],
        "message": "ok",
        "errors": None,
        "result": True,
    }

    assert json.dumps(res, sort_keys=True) == json.dumps(compare_json, sort_keys=True)
