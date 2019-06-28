# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: checkTaskManage_page.py
@time: 2019-06-28 15:38:39
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→档案管理→HPLC管理→户变关系档案校核→户变校核任务管理：PMS台区停电信息查询
class CheckTaskManagePMSPage(Page):
    # 台区编号
    def inputStr_tg_no(self, value):
        self.input(value)

    # 台区名称
    def inputStr_tg_name(self, value):
        self.input(value)

    #停电时间
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)

# 基本应用→档案管理→HPLC管理→户变关系档案校核→户变校核任务管理：历史户变校核任务信息查询
class CheckTaskManageHistoryPage(Page):
    # 台区编号
    def inputStr_tg_no(self, value):
        self.input(value)

    # 台区名称
    def inputStr_tg_name(self, value):
        self.input(value)

    #校核日期
    def inputDt_query_date(self, value):
        self.inputDate(value)

    #存在异常
    def inputChk_exist_abnormal(self,option):
        self.clickSingleCheckBox(option)
    # 查询
    def btn_qry(self):
        self.btn_query(True)
