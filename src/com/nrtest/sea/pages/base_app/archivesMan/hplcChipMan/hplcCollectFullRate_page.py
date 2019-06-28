# -*- coding: utf-8 -*-

"""
@author:郭春彪
@license: (C) Copyright 2019, Nari.
@file: hplcCollectFullRate_page.py
@time: 2019-06-28 10:48
@desc:
"""

from com.nrtest.common.base_page import Page

# 基本应用-->档案管理-->HPLC管理-->HPLC采集完整率:采集完整率统计
class HplcCollectFullRate_count_page(Page):


    # 统计时间
    def inputDt_count_time(self, value):
        self.inputDate(value)

    # 功率方式
    def inputChk_poewer_type(self, value):
        self.clickRadioBox(value,is_multi_tab=True,is_multi_elements=True)

    # 查询
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)


# 基本应用-->档案管理-->HPLC管理-->HPLC采集完整率:采集完整率统计
class HplcCollectFullRate_detail_page(Page):

    # 电表资产号
    def inputStr_meter_no(self, value):
        self.input(value)


    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 统计日期
    def inputDt_count_time(self, value):
        self.inputDate(value)

    # 功率方式
    def inputChk_poewer_type(self, value):
        self.clickRadioBox(value,is_multi_tab=True,is_multi_elements=True)
# 查询
    def btn_qry(self):
        self.btn_query(is_multi_tab=True)
