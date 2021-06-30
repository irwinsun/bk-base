/*
 * Tencent is pleased to support the open source community by making BK-BASE 蓝鲸基础平台 available.
 * Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.
 * BK-BASE 蓝鲸基础平台 is licensed under the MIT License.
 *
 * License for BK-BASE 蓝鲸基础平台:
 * --------------------------------------------------------------------
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
 * documentation files (the "Software"), to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
 * and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 * The above copyright notice and this permission notice shall be included in all copies or substantial
 * portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
 * LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
 * NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
 * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
 */

import { Component, Emit, Prop, PropSync, Vue, Watch } from 'vue-property-decorator';
import { DragTableColumn, DragTable, DragTableRow } from '@/components/DragTable/index';

interface IIndexTableData {
  columns: string[];
  list: any[];
}

@Component({
  components: { DragTableColumn, DragTable, DragTableRow },
})
export default class IndexFields extends Vue {
  /** 拖拽组件宽度 */
  @Prop({ default: 320 }) dragTableWidth: Number;

  /** 排序字段表格 */
  @Prop({ default: () => ({ columns: [], list: [] }) }) indexTableData: IIndexTableData;

  /** 是否只读状态 */
  @Prop({ default: true }) readonly: boolean;

  /** 主体高度 */
  @Prop({ default: '100%' }) bodyHeight: Number | string;

  /** 是否显示提示信息 */
  @Prop({ default: false }) showTip: boolean;

  get dragTableStyle() {
    return {
      width: `${this.dragTableWidth}px`,
    };
  }

  get indexFieldsLength() {
    return (this.indexTableData.list || []).length;
  }

  @Emit('remove-index-field')
  handleRemoveIndexField(field) {
    return field;
  }

  @Emit('drag-end')
  handleDragEnd(endList) {
    return endList;
  }
}
