# -*- coding: utf-8 -*-


"""
@author: 卢炎炎
@license: (C) Copyright 2018, Nari.
@file: workQuery_page.py
@time: 2018/10/31 15:27
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→工单查询→工单查询
class WorkCountPage(Page):

    # 日期
    def inputDt_query_date(self, value):
        self.input(value)  # , *WorkCountLocators.QRY_DATE)

    # 查询
    def btn_qry(self):
        # self.click(WorkCountLocators.BTN_QRY)
        self.btn_query()

class WorkQueryPage(Page):

    # 异常编号
    def inputStr_abnormalNo(self, value):
        self.input(value)  # , *WorkQueryLocators.QRY_ABNORMAL_NO)

    # 异常状态
    def inputSel_abnormalStatus(self, options):
        # self.click(WorkQueryLocators.QRY_ABNORMAL_STATUS)
        # locator = self.get_select_locator(
        #     WorkQueryLocators.QRY_ABNORMAL_STATUS_VALUE, index)
        # self.click(locator)
        self.selectDropDown(options)
        # 日期

    def inputDt_query_date(self, value):
        self.inputDate(value, is_multi_tab=True)  # , *WorkQueryLocators.QRY_DATE)

    # 查询
    def btn_qry(self):
        # self.click(WorkQueryLocators.BTN_QRY)
        self.btn_query(True)
