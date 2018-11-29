# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: monitorDeskCust_page.py
@time: 2018/11/27 13:57
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.msgPush.monitorDeskCust_locators import MonitorDeskCustLocators


# 系统管理→信息定制→监控台定制
class MonitorDeskCustPage(Page):
    # 角色名称
    def inputStr_role_name(self, content):
        self.input(content, *MonitorDeskCustLocators.QRY_ROLE_NAME)

    # 查询按钮
    def btn_search(self):
        self.click(*MonitorDeskCustLocators.BTN_SEARCH)
