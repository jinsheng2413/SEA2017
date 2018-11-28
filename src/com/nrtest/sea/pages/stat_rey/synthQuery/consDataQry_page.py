# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: consDataQry_page.py
@time: 2018/11/28 0028 10:17
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.consDataQry_locators import ConsDataQryLocators


# 统计查询→综合查询→用户数据
class ConsDataQryPage(Page):
    # 用户数据
    def inputStr_userNo(self, value):
        self.input(value, *ConsDataQryLocators.QRY_USER_NO)


        # 查询
    def btn_qry(self):
            self.click(*ConsDataQryLocators.BTN_QRY)