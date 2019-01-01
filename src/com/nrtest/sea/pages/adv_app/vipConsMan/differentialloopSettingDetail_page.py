# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: differentialloopSettingDetail_page.py
@time: 2018-11-07 13:57
@desc:
"""

from com.nrtest.common.base_page import Page


class DifferentialloopSettingDetail_Page(Page):
    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value)  # , *DifferentialloopSettingDetail_locators.QRY_CONS_NAME)

    # 查询
    def btn_qry(self):
        # self.click(DifferentialloopSettingDetail_locators.BTN_QUERY)
        self.btn_query()
