# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: patrolIntegratedQuery_page.py
@time: 2018/10/19 16:03
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→巡检仪综合查询
class PatrolIntegratedQueryPage(Page):
    # 巡检仪运行指标
    # 日期类型
    def inputChk_date_type(self, index):
        self.clickRadioBox(index)

    # 日期
    def inputDt_query_date(self, content):
        # self.exec_script(PatrolIntegratedQueryLocators.DATE_JS)
        # self.input(content, *PatrolIntegratedQueryLocators.DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        # self.click(PatrolIntegratedQueryLocators.BTN_SEARCH)
        self.btn_query(True)


# 巡检仪运行指标明细
class PatrolIntegratedQueryDetailPage(Page):
    # 指标类型
    def inputChk_index_type(self, index):
        self.clickRadioBox(index)

    # 日期
    def inputDt_query_date(self, content):
        # self.exec_script(PatrolIntegratedQueryLocators.DETAIL_DATE_JS)
        # self.input(content, *PatrolIntegratedQueryLocators.DETAIL_DATE)
        self.inputDate(content)

    # 指标
    def inputSel_index(self, index):
        # self.click(PatrolIntegratedQueryLocators.DETAIL_INDEX)
        # locator = self.get_select_locator(
        #     PatrolIntegratedQueryLocators.DETAIL_INDEX_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)  #, *PatrolIntegratedQueryLocators.DETAIL_TMNL_ADDR)

    # 巡检仪标识
    def inputStr_patrol_indent(self, index):
        self.input(index)

    # 用户编号
    def inputStr_cons_no(self, index):
        self.input(index)

    # 电表地址
    def inputStr_meter_addr(self, index):
        self.input(index)

    # 查询按钮
    def btn_search(self):
        # self.click(PatrolIntegratedQueryLocators.BTN_DETAIL_SEARCH)
        self.btn_query(True)
