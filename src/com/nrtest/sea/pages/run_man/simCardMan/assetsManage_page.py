# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: assetsManage_page.py
@time: 2018/11/8 0008 14:55
@desc:
"""

from com.nrtest.common.base_page import Page


#运行管理-->SIM卡管理-->资产管理
class AssetsManagePage(Page):
    # 所属系统
    def inputSel_subordinateSystem(self, item):
        self.selectDropDown(item)

    # 运营商
    def inputSel_operator(self, item):
        self.selectDropDown(item)

    # 导入日期
    def inputDt_lead_start_time(self, value):
        self.inputDate(value)

    # 时间至
    def inputDt_lead_end_time(self, value):
        self.inputDate(value)

    # SIM卡段号
    def inputStr_simCardNo(self, value):
        self.input(value)

    # SIM卡段号至
    def inputStr_simCardNoTO(self, value):
        self.input(value)

    # sim卡状态
    def inputSel_simCardStatus(self, item):
        self.selectDropDown(item)

    # 查询
    def btn_qry(self):
        self.btn_query()
