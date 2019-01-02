# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/24 20:42
@desc:
"""

from com.nrtest.common.base_page import Page


class LoadRateDetailPage(Page):
    # 供电单位
    # def inputStr_org_no(self, value):
    #     self.openLeftTree(value)

    # 用户类型--打开并选择
    def inputSel_cons_type(self, item):
        #         self.click(ThreeUnbalanceAnalyStaticLocators.CONS_TYPE_SEL)
        #         locator = self.get_select_locator(
        #             LoadRateStaticLocators.CONS_TYPE, name)
        #         self.click(locator)
        self.selectDropDown(item,True,1,True)

    # 查询日期
    def inputStr_query_date(self, value):
        #self.input(value, *ThreeUnbalanceAnalyStaticLocators.QUERY_DATE)
        self.curr_input(value, True, True)

    # 点击查询
    def btn_qry(self):
        # self.click(ThreeUnbalanceAnalyStaticLocators.BTN_QUERY)
        self.btn_query(True)

