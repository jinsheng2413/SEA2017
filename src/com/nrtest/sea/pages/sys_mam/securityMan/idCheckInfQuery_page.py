# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: idCheckInfQuery_page.py
@time: 2018/11/15 11:34
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.securityMan.idCheckInfQuery_locators import IdCheckInfQueryLocators


# 系统管理→权限密码管理→账号审核信息查询
class IdCheckInfQueryPage(Page):
    # 审核开始日期
    def inputDt_start_date(self, content):
        self.exec_script(IdCheckInfQueryLocators.START_DATE_JS)
        # self.input(content, *IdCheckInfQueryLocators.QRY_START_DATE)
        self.inputDate(content)

    # 审核结束日期
    def inputDt_end_date(self, content):
        self.exec_script(IdCheckInfQueryLocators.END_DATE_JS)
        # self.input(content, *IdCheckInfQueryLocators.QRY_END_DATE)
        self.inputDate(content)

    # 审核结果
    def inputSel_result(self, option):
        # self.click(IdCheckInfQueryLocators.QRY_RESULT)
        # locator = self.get_select_locator(IdCheckInfQueryLocators.QRY_RESULT_VALUE, option)
        # self.click(locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(option)

    # 查询按钮
    def btn_search(self):
        # self.click(IdCheckInfQueryLocators.BTN_SEARCH)
        self.btn_query()
