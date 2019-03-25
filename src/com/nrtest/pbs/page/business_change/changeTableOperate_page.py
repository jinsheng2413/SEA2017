# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: changeTableOperate_page.py
@time: 2019/03/06 15:43
@desc:
"""

from com.nrtest.pbs.locators.business_change.changeTableOperate_locators import ChangeTableOperateLocators
from com.nrtest.pbs.tree.tree_page import TreePBSPage


# 业务变更→换表操作:换表操作
class ChangeTableOperatePage(TreePBSPage):
    # 电表
    def inputStr_meter(self, value):
        self.input(value)

    # 开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 资产号
    def inputStr_asset_no(self, value):
        self.input(value)

    # 查询按钮
    def btn_qry(self):
        self.click(ChangeTableOperateLocators.BTN_QUERY)


# 业务变更→换表操作:换表记录
class ChangeTableRecordPage(TreePBSPage):
    # 时间类型
    def inputChk_date_type(self, value):
        self.selectDropDown(value)

    # 开始时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束时间
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(True)
