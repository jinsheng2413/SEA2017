# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→终端管理→远程调试
class TmnlInstallDetaiPage(Page):

    # 终端类型
    def inputSel_TmnlType(self, options):
        # self.click(TmnlInstallDetaiLocators.QRY_TMNL_TYPE)
        # locator = self.get_select_locator(
        #     TmnlInstallDetaiLocators.QRY_TMNL_TYPE_VALUE, options)
        # self.click(locator)
        self.selectDropDown(options)

    # 开始时间
    def inputStr_Start_time(self, value):
        self.input(value)  # , *TmnlInstallDetaiLocators.QRY_START_TIME)

    # 结束时间
    def inputStr_end_time(self, value):
        self.input(value)  # , *TmnlInstallDetaiLocators.QRY_END_TIME)

        # 查询

    def btn_workCount_qry(self):
        # self.click(TmnlInstallDetaiLocators.BTN_WORK_COUNT_QRY)
        self.btn_query(True)


    # --------------------------------------终端调试------------------------------------------
    # 开始时间
    def inputStr_startTime_count(self, value):
        # self.input(value) #, *TmnlInstallDetaiLocators.QRY_START_TIME_COUNT)
        # ljf
        self.inputDate(value)

    # 结束时间
    def inputStr_endTime_Count(self, value):
        # self.input(value) #, *TmnlInstallDetaiLocators.QRY_END_TIME_COUNT)
        self.inputDate(value)

    # 申请单号
    def inputStr_applyNo_count(self, value):
        # self.input(value) #, *TmnlInstallDetaiLocators.QRY_APPLY_STATE_COUNT)
        self.input(value)

    # 用户编号
    def inputStr_userNo_count(self, value):
        # self.input(value) #, *TmnlInstallDetaiLocators.QRY_USER_NO_COUNT)
        self.input(value)

    # 终端地址
    def inputStr_tmnlAddr_count(self, value):
        # self.input(value) #, *TmnlInstallDetaiLocators.QRY_TMNL_ADDR_COUNT)
        self.input(value)

    # 终端厂家
    def inputSel_tmnlFactory_count(self, options):
        # self.input(options) #, *TmnlInstallDetaiLocators.QRY_TMNL_FACTORY_COUNT)
        self.selectCheckBox(options, sleep_sec=2)

    # 终端类型
    def inputSel_tmnlType_count(self, options):
        # self.input(options) #, *TmnlInstallDetaiLocators.QRY_TMNL_TYPE_COUNT)
        self.selectCheckBox(options, is_multi_tab=True, sleep_sec=2,
                            is_multi_elements=True)

    # 通信规约
    def inputSel_LCT_count(self, options):
        # self.input(options) #, *TmnlInstallDetaiLocators.QRY_LCT_COUNT)
        self.selectCheckBox(options)

    # 表类型
    def inputSel_surfaceType_count(self, options):
        # print(options)
        # self.click(TmnlInstallDetaiLocators.QRY_SURFACE_TYPE_COUNT)
        # locator = self.get_select_locator(
        #     TmnlInstallDetaiLocators.QRY_SURFACE_TYPE_VALUE, options)
        # self.click(locator)
        self.selectDropDown(options)

    # 流程标识
    def inputSel_processID_count(self, options):
        # self.click(TmnlInstallDetaiLocators.QRY_PROCESS_ID_COUNT)
        # locator = self.get_select_locator(
        #     TmnlInstallDetaiLocators.QRY_PROCESS_ID_COUNT_VALUE, options)
        # print(locator)
        # self.click(locator)
        # print(locator)
        self.selectDropDown(options)

    # 运行状态
    def inputSel_runState_count(self, options):
        # self.click(TmnlInstallDetaiLocators.QRY_RUN_STATE_COUNT)
        # locator = self.get_select_locator(
        #     TmnlInstallDetaiLocators.QRY_RUN_STATE_COUNT_VALUE, options)
        # self.click(locator)
        self.selectDropDown(options)

    # 装接类型
    def inputSel_moutingType_count(self, options):
        # self.click(TmnlInstallDetaiLocators.QRY_MOUNTING_COUNT)
        # locator = self.get_select_locator(
        #     TmnlInstallDetaiLocators.QRY_MOUNTING_COUNT_VALUE, options)
        # self.click(locator)
        self.selectDropDown(options)

    # 查询
    def btn_tmnl_qry(self):
        # self.click(TmnlInstallDetaiLocators.BTN_TMNL_QRY)
        # self.click(None)
        self.btn_query(True)
