# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/29 10:42
@desc:
"""

from com.nrtest.common.base_page import Page


class SpVoltAnalyseDetailPage(Page):
    # 供电单位
    # def inputStr_org_no(self, value):
    #     self.openLeftTree(value)

    # 用户类型--打开并选择
    def inputSel_cons_type(self, item):
        self.selectDropDown(item,is_multi_tab=True,is_multi_elements=True)

    # 日期类型
    def inputChk_data_method(self, option):
        self.clickRadioBox(option, True, True)

    # 查询日期
    def inputStr_query_date(self, value):
        self.inputDate(value)
        # self.input(value)

    # 点击查询
    def btn_qry(self):
        # self.click(SpVoltAnalyseDetailLocators.BTN_QUERY)
        self.btn_query(True)
