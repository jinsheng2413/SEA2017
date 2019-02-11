# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: orgLowVoltDay_page.py
@time: 2018/9/29 10:42
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→配变监测分析→电压质量分析→低压用户电压分析
# 台区低电压日统计
class OrgLowVoltDayStaticPage(Page):

    # 开始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query()

# 台区低电压日统计明细
class OrgLowVoltDayDetailPage(Page):

    # 开始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 结束日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 台区名称
    def inputStr_tg_name(self, value):
        self.input(value)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)

# 低压用户电压监测配置
class OrgLowVoltDayConfigPage(Page):

    # 是否电压监测--打开并选择
    def inputSel_is_volt_monitor(self, item):
        self.selectDropDown(item)

    # 点击查询
    def btn_qry(self):
        self.btn_query(True)
