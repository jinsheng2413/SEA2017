# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: assetsManage_page.py
@time: 2018/11/8 0008 14:55
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.simCardMan.assetsManage_locators import AssetsManageLocators


#运行管理-->SIM卡管理-->资产管理
class AssetsManagePage(Page):
    # 所属系统
    def inputSel_subordinateSystem(self, item):
        # self.click(*AssetsManageLocators.QRY_SUBORDINATE_SYSTEM)
        # locator = self.get_select_locator(AssetsManageLocators.QRY_SUBORDINATE_SYSTEM_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 运营商
    def inputSel_operator(self, item):
        # self.click(*AssetsManageLocators.QRY_OPERATOR)
        # locator = self.get_select_locator(AssetsManageLocators.QRY_OPERATOR_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(item)


    # 时间至
    def inputStr_timeTO(self, value):
        # self.input(value, *AssetsManageLocators.QRY_TIME_TO)
        self.input(value)

    # 导入日期
    def inputStr_leadTime(self, value):
        # self.input(value, *AssetsManageLocators.QRY_LEAD_TO_TIME)
        self.input(value)

    # SIM卡段号至
    def inputStr_simCardNoTO(self, value):
        # self.input(value, *AssetsManageLocators.QRY_SIM_CARD_NO_TO)
        self.input(value)

    # SIM卡段号
    def inputStr_simCardNo(self, value):
        # self.input(value, *AssetsManageLocators.QRY_SIM_CARD_NO)
        self.input(value)

    # sim卡状态
    def inputSel_simCardStatus(self, item):
        # self.click(*AssetsManageLocators.QRY_SIM_CARD_STATUS)
        # locator = self.get_select_locator(AssetsManageLocators.QRY_SIM_CARD_STATUS_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(item)

    # 查询
    def btn_qry(self):
        # self.click(*AssetsManageLocators.BTN_QRY)
        self.btn_query()