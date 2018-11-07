# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.dataGatherMan.tmnlInstallDetai import TmnlInstallDetaiLocators


# 基本应用→终端管理→远程调试
class TmnlInstallDetaiPage(Page):

    # 终端类型
    def inputSel_TmnlTYPE(self, name):
        self.click(*TmnlInstallDetaiLocators.QRY_TMNL_TYPE)
        locator = self.get_select_locator(TmnlInstallDetaiLocators.QRY_TMNL_TYPE_VALUE, name)
        self.click(*locator)

    # 开始时间
    def inputStr_Start_time(self, value):
        self.input(value, *TmnlInstallDetaiLocators.QRY_START_TIME)

    # 结束时间
    def inputStr_end_time(self, value):
        self.input(value, *TmnlInstallDetaiLocators.QRY_END_TIME)

        # 查询

    def btn_workCount_qry(self):
        self.click(*TmnlInstallDetaiLocators.BTN_WORK_COUNT_QRY)

    # --------------------------------------终端调试------------------------------------------
    # 开始时间
    def inputStr_startTime_count(self, value):
        self.input(value, *TmnlInstallDetaiLocators.QRY_START_TIME_COUNT)

    # 结束时间
    def inputStr_enTime_Count(self, value):
        self.input(value, *TmnlInstallDetaiLocators.QRY_END_TIME_COUNT)

    # 申请单号
    def inputStr_applyNo_count(self, value):
        self.input(value, *TmnlInstallDetaiLocators.QRY_APPLY_STATE_COUNT)

    # 用户编号
    def inputStr_userNo_count(self, value):
        self.input(value, *TmnlInstallDetaiLocators.QRY_USER_NO_COUNT)

    # 终端地址
    def inputStr_tmnlAddr_count(self, value):
        self.input(value, *TmnlInstallDetaiLocators.QRY_TMNL_ADDR_COUNT)

    # 终端厂家
    def inputStr_tmnlFactory_count(self, value):
        self.input(value, *TmnlInstallDetaiLocators.QRY_TMNL_FACTORY_COUNT)

    # 终端类型
    def inputStr_tmnlType_count(self, value):
        self.input(value, *TmnlInstallDetaiLocators.QRY_TMNL_TYPE_COUNT)

    # 通信规约
    def inputStr_LCT_count(self, value):
        self.input(value, *TmnlInstallDetaiLocators.QRY_LCT_COUNT)

    # 表类型
    def inputSel_surfaceType_count(self, value):
        print(value)
        self.click(*TmnlInstallDetaiLocators.QRY_SURFACE_TYPE_COUNT)
        locator = self.get_select_locator(TmnlInstallDetaiLocators.QRY_SURFACE_TYPE_VALUE, value)
        self.click(*locator)

    # 流程标识
    def inputSel_processID_count(self, name):
        self.click(*TmnlInstallDetaiLocators.QRY_PROCESS_ID_COUNT)
        locator = self.get_select_locator(TmnlInstallDetaiLocators.QRY_PROCESS_ID_COUNT_VALUE, name)
        print(locator)
        self.click(*locator)
        print(locator)

    # 运行状态
    def inputSel_runState_count(self, name):
        self.click(*TmnlInstallDetaiLocators.QRY_RUN_STATE_COUNT)
        locator = self.get_select_locator(TmnlInstallDetaiLocators.QRY_RUN_STATE_COUNT_VALUE, name)
        self.click(*locator)

    # 装接类型
    def inputSel_moutingType_count(self, name):
        self.click(*TmnlInstallDetaiLocators.QRY_MOUNTING_COUNT)
        locator = self.get_select_locator(TmnlInstallDetaiLocators.QRY_MOUNTING_COUNT_VALUE, name)
        self.click(*locator)

    # 查询
    def btn_tmnl_qry(self):
        self.click(*TmnlInstallDetaiLocators.BTN_TMNL_QRY)
