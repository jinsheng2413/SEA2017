# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: strategicManualRecord_page.py
@time: 2018-11-08 10:01
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.interfaceMan.strategicManualRecord_locators import StrategicManualRecord_Locators


class StrategicManualRecordPage(Page):
    # 采集点名
    def inputStr_gatherpoint_name(self, value):
        self.input(value, *StrategicManualRecord_Locators.QRY_GATHERPOINT_NAME)

    # 电表名称
    def inputStr_meter_name(self, value):
        self.input(value, *StrategicManualRecord_Locators.QRY_METER_NAME)

    # 电表地址
    def inputStr_meter_addr(self, value):
        self.input(value, *StrategicManualRecord_Locators.QRY_METER_ADDR)

    def inputStr_date(self, value):
        self.input(value, *StrategicManualRecord_Locators.QRY_DATE)

    # 查询
    def btn_qry(self):
        self.click(StrategicManualRecord_Locators.BTN_QRY)
