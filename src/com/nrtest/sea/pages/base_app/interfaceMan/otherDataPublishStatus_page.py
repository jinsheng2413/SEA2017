# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: mDataPublishStatus2_page.py
@time: 2018-10-30 16:03
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→接口管理→其他业务接口→数据发布情况
class OtherDataPublishStatusPage(Page):

    # 业务系统
    def inputSel_business_system(self, option):
        self.selectDropDown(option)

    # 发布时间 开始
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 结束时间
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 查询
    def btn_qry(self):
        self.btn_query()
