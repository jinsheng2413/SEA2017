# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: outMemberMan_page.py
@time: 2018/11/13 0013 10:15
@desc:
"""

from com.nrtest.common.base_page import Page

# 运行管理-->采集运维平台-->组织运维管理
# 外包队伍管理
class OutRanksManPage(Page):
    # 外包队伍名称
    def inputStr_out_name(self, value):
        # self.input(value, *OutNameTroopLocators.QRY_OUT_NAME)
        self.input(value)

    # 查询
    def btn_qry(self):
        # self.click(OutNameTroopLocators.BTN_QRY)
        self.btn_query()

# 外包队伍成员管理
class OutMemberManPage(Page):
    # 外包队伍名称
    def inputStr_out_name(self, value):
        # self.input(value, *OutNameTroopMemberLocators.QRY_OUT_NAME)
        self.curr_input(value, is_multi_tab=True, is_multi_elements=True)

    # 查询
    def btn_qry(self):
        # self.click(OutNameTroopMemberLocators.BTN_QRY)
        self.btn_query(True)
