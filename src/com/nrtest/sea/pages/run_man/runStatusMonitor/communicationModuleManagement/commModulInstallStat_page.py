# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: commModulInstallStat_page.py
@time: 2018/11/6 0006 11:27
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→采集信道管理→通信模块管理→通信模块安装统计
class CommModulInstallStatPage(Page):
    # 日期
    def inputDt_query_date(self, value):
        self.input(value)#, *CommModulInstallStatLocators.QRY_DATE)

    # 模块类型
    def inputSel_moduleType(self, options):
        # self.click(CommModulInstallStatLocators.QRY_MODULE_TYPE)
        # locator = self.get_select_locator(CommModulInstallStatLocators.QRY_MODULE_TYPE_VALUE, name)
        # self.click(locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(options)

    # 模块厂商
    def inputSel_moduleFactory(self, options):
        # self.click(CommModulInstallStatLocators.QRY_MODULE_FACTORY)
        # locator = self.get_select_locator(CommModulInstallStatLocators.QRY_MODULE_FACTORY_VALUE, name)
        # self.click(locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(options)

    # 模块版本
    def inputSel_moduleVersion(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        # self.click(CommModulInstallStatLocators.BTN_QRY)
        self.btn_query()
