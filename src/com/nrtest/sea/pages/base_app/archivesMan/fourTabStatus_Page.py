# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.archivesMan.fourTabStatus_locators import FourTabStatusLocators


class FourTabStatusPage(Page):

    # 用户状态
    def inputSel_userState(self, name):
        self.click(*FourTabStatusLocators.QRY_USER_STATE)
        locator = self.get_select_locator(FourTabStatusLocators.QRY_USER_STATE_VALUE, name)
        self.click(*locator)

        # 查询

    def btn_qry(self):
        self.click(*FourTabStatusLocators.BTN_QRY)
