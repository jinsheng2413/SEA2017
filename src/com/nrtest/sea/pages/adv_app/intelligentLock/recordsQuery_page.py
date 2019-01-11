# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: recordsQuery_page.py
@time: 2018/10/26 16:43
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→智能锁具→记录查询
class RecordsQueryPage(Page):
    # 开关锁操作日志
    # 操作员名称
    def inputStr_staff_name(self, content):
        self.input(content)  # , *RecordsQueryLocators.STAFF_NAME)

    # 台区编号
    def inputStr_tg_no(self, content):
        self.input(content)  #, *RecordsQueryLocators.TG_NO)

    # 台区名称
    def inputStr_tg_name(self, content):
        self.input(content)  #, *RecordsQueryLocators.TG_NAME)

    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content)  #, *RecordsQueryLocators.CONS_NO)

    # 用户名称
    def inputStr_user_name(self, content):
        self.input(content)  #, *RecordsQueryLocators.USER_NAME)

    # 用户类型
    def inputSel_cons_type(self, index):
        # self.click(RecordsQueryLocators.CONS_TYPE)
        # locator = self.get_select_locator(
        #     RecordsQueryLocators.CONS_TYPE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 操作行为
    def inputSel_operant_hehavior(self, index):
        # self.click(RecordsQueryLocators.OPERANT_HEHAVIOR)
        # locator = self.get_select_locator(
        #     RecordsQueryLocators.OPERANT_HEHAVIOR_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 操作结果
    def inputSel_operant_result(self, index):
        # self.click(RecordsQueryLocators.OPERANT_RESULT)
        # locator = self.get_select_locator(
        #     RecordsQueryLocators.OPERANT_RESULT_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 电子钥匙编号
    def inputStr_key_no(self, content):
        self.input(content)  #, *RecordsQueryLocators.KEY_NO)

    # 锁封编号
    def inputStr_lock_no(self, content):
        self.input(content)  #, *RecordsQueryLocators.LOCK_NO)

    # 开始日期
    def inputDt_start_date(self, content):
        # self.exec_script(RecordsQueryLocators.START_DATE_JS)
        # self.input(content, *RecordsQueryLocators.START_DATE)
        self.inputDate(content)

    # 结束日期
    def inputDt_end_date(self, content):
        # self.exec_script(RecordsQueryLocators.END_DATE_JS)
        # self.input(content, *RecordsQueryLocators.END_DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        # self.click(RecordsQueryLocators.BTN_SEARCH)
        self.btn_query()

    # 资产管理记录查询


class RecordsQueryStaffPage(Page):
    # 操作员名称
    def inputStr_staff_name(self, content):
        self.curr_input(content, True, True)  # , *RecordsQueryLocators.TAB_STAFF_NAME)

    # 电子钥匙编号
    def inputStr_key_no(self, content):
        self.curr_input(content, True, True)  # , *RecordsQueryLocators.TAB_KEY_NO)

    # 锁封编号
    def inputStr_lock_no(self, content):
        self.curr_input(content, True, True)  #, *RecordsQueryLocators.TAB_LOCK_NO)

    # 锁封用户编号
    def inputStr_lock_user_no(self, content):
        self.curr_input(content, True, True)  #, *RecordsQueryLocators.TAB_LOCK_USER_NO)

    # 开始日期
    def inputDt_start_date(self, content):
        # self.exec_script(RecordsQueryLocators.TAB_START_DATE_JS)
        # self.input(content, *RecordsQueryLocators.TAB_START_DATE)
        self.inputDate(content)

    # 结束日期
    def inputDt_end_date(self, content):
        # self.exec_script(RecordsQueryLocators.TAB_END_DATE_JS)
        # self.input(content, *RecordsQueryLocators.TAB_END_DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        # self.click(RecordsQueryLocators.TAB_BTN_SEARCH)
        self.btn_query(True)
