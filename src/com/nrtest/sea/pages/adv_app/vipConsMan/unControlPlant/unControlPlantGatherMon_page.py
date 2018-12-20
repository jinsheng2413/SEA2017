# -*- coding:utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: unControlPlantGatherMon_page.py
@time: 2018-11-06 14:46
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.vipConsMan.unControlPlant.unControlPlantGatherMon_locators import \
    UnControlPlantGatherMon1_locators, UnControlPlantGatherMon2_locators


# 第一个tab页
class UnControlPlantGatherMon1_Page(Page):
    # 开始时间
    def inputStr_start_date(self, value):
        self.input(value)  # , *UnControlPlantGatherMon1_locators.QRY_START_DATE)

    # 结束时间
    def inputStr_end_date(self, value):
        self.input(value)  #, *UnControlPlantGatherMon1_locators.QRY_END_DATE)

    # 发电方式
    def inputSel_generate_electricity_way(self, options):
        # self.click(*UnControlPlantGatherMon1_locators.QRY_GENERATE_ELECTRICITY_WAY)
        # locator = self.get_select_locator(UnControlPlantGatherMon1_locators.QRY_GENERATE_ELECTRICITY_WAY_VALUE, index)
        # self.click(*locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(options)

    # 采集方式
    def inputSel_gather_way(self, options):
        # self.click(*UnControlPlantGatherMon1_locators.QRY_GATHER_WAY)
        # locator = self.get_select_locator(UnControlPlantGatherMon1_locators.QRY_GATHER_WAY_VALUE, index)
        # self.click(*locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(options)

    # 查询
    def btn_qry(self):
        #self.click(*UnControlPlantGatherMon1_locators.BTN_QUERY)
        self.btn_query()


# 第二个tab页
class UnControlPlantGatherMon2_Page(Page):
    # 发电方式
    def inputSel_generate_electricity_way(self, options):
        # self.click(*UnControlPlantGatherMon2_locators.QRY_GENERATE_ELECTRICITY_WAY)
        # locator = self.get_select_locator(UnControlPlantGatherMon2_locators.QRY_GENERATE_ELECTRICITY_WAY_VALUE, index)
        # self.click(*locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(options, is_multi_tab=True, is_multi_elements=True)

    # 采集方式
    def inputSel_gather_way(self, options):
        # self.click(*UnControlPlantGatherMon2_locators.QRY_GATHER_WAY)
        # locator = self.get_select_locator(UnControlPlantGatherMon2_locators.QRY_GATHER_WAY_VALUE, index)
        # self.click(*locator)
        # self.delDropdownBoxHtml()
        self.selectDropDown(options, is_multi_tab=True, is_multi_elements=True)

    # 查询日期
    def inputStr_date(self, value):
        self.input(value)  #, *UnControlPlantGatherMon2_locators.QRY_DATE)

    # 户号
    def inputStr_cons_no(self, value):
        self.input(value)  #, *UnControlPlantGatherMon2_locators.QRY_CONS_NO)

    # 表资产编号
    def inputStr_meter_asst_no(self, value):
        self.input(value)  #, *UnControlPlantGatherMon2_locators.QRY_METER_ASST_NO)

    # 终端资产号
    def inputStr_tmnl_asst_no(self, value):
        self.input(value)  #, *UnControlPlantGatherMon2_locators.QRY_TMNL_ASST_NO)

    # 查询
    def btn_qry(self):
        #self.click(*UnControlPlantGatherMon2_locators.BTN_QUERY)
        self.btn_query(True)