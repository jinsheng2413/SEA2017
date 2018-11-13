# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: outMemberMan_page.py
@time: 2018/11/13 0013 10:15
@desc:
"""
from com.nrtest.sea.locators.run_man.collegeywplat.outMemberMan_locators import OutNameTroopMemberLocators,OutNameTroopLocators


from com.nrtest.common.base_page import Page

# 运行管理-->采集运维平台-->组织运维管理
class OutNameTroopPage(Page):
    # 外包队伍名称
    def inputStr_outName(self, value):
        self.input(value, *OutNameTroopLocators.QRY_OUT_NAME)




        # 查询
    def btn_qry(self):
            self.click(*OutNameTroopLocators.BTN_QRY)
class OutNameTroopMemberPage(Page):
    # 外包队伍名称
    def inputStr_outName(self, value):
        self.input(value, *OutNameTroopMemberLocators.QRY_OUT_NAME)




        # 查询
    def btn_qry(self):
            self.click(*OutNameTroopMemberLocators.BTN_QRY)