# -*- coding: utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: loadingEquipment_page.py
@time: 2018-11-05 15:53
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.vipConsMan.loadingEquipment_locators import LoadingEquipment_locators


class LoadingEquipment_Page(Page):
    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value, *LoadingEquipment_locators.QRY_TMNL_ADDR)

    # 查询
    def btn_qry(self):
        self.click(*LoadingEquipment_locators.BTN_QUERY)
