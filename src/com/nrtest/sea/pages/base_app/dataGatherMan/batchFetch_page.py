# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.dataGatherMan.batchFetch_locators import BatchFetchLocators


class BatchFetchPage(Page):
    # 任务名称
    def inputStr_taskName(self, value):
        self.input(value, *BatchFetchLocators.QRY_TASK_NAME)

    # 有效性
    def inputSel_effectiveness(self, name):
        self.click(*BatchFetchLocators.QRY_EFFECTIVENESS)
        locator = self.get_select_locator(BatchFetchLocators.QRY_EFFECTIVENESS_VALUE, name)
        self.click(*locator)

    # 开始时间
    def inputStr_startTime(self, value):
        self.input(value, *BatchFetchLocators.QRY_START_TIME)

    # 操作人
    def inputStr_performer(self, value):
        self.input(value, *BatchFetchLocators.QRY_PERFORMER)

        # 查询

    def btn_qry(self):
        self.click(*BatchFetchLocators.BTN_QRY)
