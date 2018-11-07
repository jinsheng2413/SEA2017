# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.dataGatherMan.gatherTaskCompile_locators import GatherTaskCompileLocators


class GatherTaskCompilePage(Page):
    # 任务状态
    def inputSel_taskState(self, name):
        self.click(*GatherTaskCompileLocators.QRY_TASK_STATE)
        locator = self.get_select_locator(GatherTaskCompileLocators.QRY_TASK_STATE_VALUE, name)
        self.click(*locator)

    # 终端类型
    def inputRSel_TmnlType(self, name):
        self.click(*GatherTaskCompileLocators.QRY_TMAL_TYPE)
        locator = self.get_select_locator(GatherTaskCompileLocators.QRY_TMAL_TYPE_VALUE, name)
        print(locator)
        self.click(*locator)

    # 采集点名称
    def inputStr_CollectionPointName(self, value):
        self.input(value, *GatherTaskCompileLocators.QRY_COLLECTION_POINT_NAME)

    # 终端地址
    def inputStr_TMNL_ADDR(self, value):
        self.input(value, *GatherTaskCompileLocators.QRY_TMNL_ADDR)

    # 任务名称
    def inputStr_taskName(self, value):
        self.input(value, *GatherTaskCompileLocators.QRY_TASK_NAME)

    # 任务编号
    def inputStr_taskNo(self, value):
        self.input(value, *GatherTaskCompileLocators.QRY_TAST_NO)

    # 任务类型
    def inputSel_taskType(self, name):
        self.click(*GatherTaskCompileLocators.QRY_TASK_TYPE)
        locator = self.get_select_locator(GatherTaskCompileLocators.QRY_TASK_TYPE_VALUE, name)
        self.click(*locator)

        # 查询

    def btn_qry(self):
        self.click(*GatherTaskCompileLocators.BTN_QRY)
