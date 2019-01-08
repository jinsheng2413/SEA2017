# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: mInterfaceRunStauts2_page.py
@time: 2018-10-31 11:11
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用--接口管理--营销业务接口--接口运行状态

class MInterfaceRunStatus2Page(Page):
    # 业务系统
    def inputSel_business_system(self, index):
        self.selectDropDown(index)

    # 服务对象名称
    def inputSel_service_name(self, index):
        self.selectDropDown(index)

    # 查询
    def btn_qry(self):
        self.btn_query()
