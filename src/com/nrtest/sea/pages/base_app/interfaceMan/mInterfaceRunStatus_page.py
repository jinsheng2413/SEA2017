# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: mInterfaceRunStatus_page.py
@time: 2018-10-30 11:21
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用--接口管理--其他业务接口--接口运行状态
class MInterfaceRunStatusPage(Page):
    # 业务系统
    def inputSel_business_system(self, option):
        self.selectDropDown(option)

    # 服务对象名称
    def inputSel_service_name(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query()
