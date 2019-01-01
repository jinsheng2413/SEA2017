# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: userOperationMan_page.py
@time: 2018/11/20 14:57
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→系统配置管理→用户操作监测
class UserOperationMonitorPage(Page):
    # 日期
    def inputDt_date(self, content):
        # self.exec_script(UserOperationMonitorLocators.DATE_JS)
        # self.input(content, *UserOperationMonitorLocators.QRY_DATE)
        self.inputDate(content)

    # 操作模块
    def inputSel_operation_module(self, option):
        # self.click(UserOperationMonitorLocators.QRY_OPERATION_MODULE)
        # locator = self.get_select_locator(UserOperationMonitorLocators.QRY_OPERATION_MODULE_VALUE, option)
        # self.click(locator)
        self.selectDropDown(option)

    # 操作人员
    def inputStr_operator(self, content):
        # self.input(content, *UserOperationMonitorLocators.QRY_OPERATOR)
        self.input(content)

    # 查询按钮
    def btn_search(self):
        # self.click(UserOperationMonitorLocators.BTN_SEARCH)
        self.btn_query()
