# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: PublicDataQueryPage.py
@time: 2018-08-15 16:40
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→配变数据查询
class CollcateDataQueryPage(Page):

    # 配变用户
    def inputStr_user(self, value):
        self.input(value)  # , *PublicDataQueryLocators.QRY_PUBLICCONSNO)

    # 配变表号
    def inputSel_meter_asset_no(self, value):
        self.input(value)  # , *PublicDataQueryLocators.QRY_PUBLICNUM)
