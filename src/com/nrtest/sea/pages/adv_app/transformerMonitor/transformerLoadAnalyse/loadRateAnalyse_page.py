# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/24 20:42
@desc:
"""

from com.nrtest.common.base_page import Page

# 高级应用--》配变负载分析--》负载率分析
# 负载率统计
class LoadRateStaticPage(Page):

    # 用户类型--打开并选择
    def inputSel_cons_type(self, item):
        self.selectDropDown(item)

    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query()

# 负载率明细
class LoadRateDetailPage(Page):

    # 用户类型--打开并选择
    def inputSel_cons_type(self, item):
        self.selectDropDown(item,is_multi_elements=True,is_multi_tab=True)

    # 负载情况
    def inputChk_load_status(self, para):
        for i in range (7):
            self.clickSingleCheckBox(para['LOAD_STATUS' + str(i)])


    # 查询日期
    def inputDt_query_date(self, value):
        self.inputDate(value,True,True)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)
