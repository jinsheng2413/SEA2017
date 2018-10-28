# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.costControlManage.remoteCustControl.ctrlExecutSpec_locators import \
    CtrlExecutSpecLocators


class CtrlExecutSpecPage(Page):
    # 控制类别
    def inputRSel_controlType(self, name):
        self.click(*CtrlExecutSpecLocators.QRY_CONTROL_TYPE)
        locator = self.get_select_locator(CtrlExecutSpecLocators.QRY_CONTROL_TYPE_VALUE, name)
        self.click(*locator)

    # 工单号
    def inputStr_workOrder(self, value):
        self.input(value, *CtrlExecutSpecLocators.QRY_WORK_ORDER)

    # 结束时间
    def inputStr_endTime(self, value):
        self.input(value, *CtrlExecutSpecLocators.QRY_END_TIME)

    # 开始时间
    def inputStr_startTime(self, value):
        self.input(value, *CtrlExecutSpecLocators.QRY_START_TIME)

    # 终端地址
    def inputStr_tmnlAddr(self, value):
        self.input(value, *CtrlExecutSpecLocators.QRY_TMNL_ADDR)

    # 用户名称
    def inputStr_userName(self, value):
        self.input(value, *CtrlExecutSpecLocators.QRY_USER_NAME)

    # 用户编号
    def inputStr_userNo(self, value):
        self.input(value, *CtrlExecutSpecLocators.QRY_USER_NO)

    # 执行状态
    def inputSel_exeStatus(self, name):
        self.click(*CtrlExecutSpecLocators.QRY_EXE_STATUS)
        locator = self.get_select_locator(CtrlExecutSpecLocators.QRY_EXE_STATUS_VALUE, name)
        self.click(*locator)

        # 查询

    def btn_qry(self):
        self.click(*CtrlExecutSpecLocators.BTN_QRY)
