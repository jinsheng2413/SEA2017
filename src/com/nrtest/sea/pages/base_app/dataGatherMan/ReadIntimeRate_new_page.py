# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: ReadIntimeRate_new_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→采集质量检查(new):采集及时率
class ReadIntimeRateNewPage(Page):

    # 芯片厂家
    def inputSel_chip_factory(self, name):
        self.selectDropDown(name)

    # 终端厂家
    def inputSel_tmnl_factory(self, name):
        self.selectDropDown(name)

    # 用户类型
    def inputSel_cons_type(self, name):
        self.selectDropDown(name)

    # 日期时间
    def inputDt_query_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
