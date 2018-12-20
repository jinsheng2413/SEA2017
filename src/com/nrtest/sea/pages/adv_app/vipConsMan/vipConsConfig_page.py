# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: vipConsConfig_page.py
@time: 2018-11-05 11:06
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.vipConsMan.vipConsConfig_locators import VipConsConfig_locators


class VipConsConfig_Page(Page):
    # 运行容量等级
    def inputSel_run_level(self, options):
        # self.click(*VipConsConfig_locators.QRY_RUN_LEVEL)
        # locator = self.get_select_locator(
        #     VipConsConfig_locators.QRY_RUN_LEVEL_VALUE, index)
        # self.click(*locator)
        self.selectDropDown(options)

    # 用户编号
    def inputStr_cons_no(self, value):
        self.input(value)  # , *VipConsConfig_locators.QRY_CONS_NO)

    # 用户名称
    def inputStr_cons_name(self, value):
        self.input(value)  #, *VipConsConfig_locators.QRY_CONS_NAME)

    # 查询
    def btn_qry(self):
        self.click(*VipConsConfig_locators.BTN_QUERY)
