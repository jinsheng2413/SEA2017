# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: unControlPlantStat_page.py
@time: 2018/11/12 11:14
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→重点用户监测→非统调电厂管理→非统调电厂接入统计
class UnControlPlantStatPage(Page):
    # 发电方式
    def inputSel_gc_mode(self, index):
        # self.click(UnControlPlantStatLocators.QRY_GC_MODE)
        # locator = self.get_select_locator(UnControlPlantStatLocators.QRY_GC_MODE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 采集方式
    def inputSel_coll_mode(self, index):
        # self.click(UnControlPlantStatLocators.QRY_COLL_MODE)
        # locator = self.get_select_locator(UnControlPlantStatLocators.QRY_COLL_MODE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index)

    # 日期
    def inputDt_query_date(self, content):
        # self.exec_script(UnControlPlantStatLocators.DATE_JS)
        # self.input(content, *UnControlPlantStatLocators.QRY_DATE)
        self.inputDate(content)

    # 查询
    def btn_search(self):
        # self.click(UnControlPlantStatLocators.BTN_SEARCH)
        self.btn_query()

# 高级应用→重点用户监测→非统调电厂管理→非统调电厂接入统计→非统调电厂接入明细
class UnControlPlantDetailPage(Page):
    # 发电方式
    def inputSel_gc_mode(self, index):
        # self.click(UnControlPlantDetailLocators.QRY_GC_MODE)
        # locator = self.get_select_locator(UnControlPlantDetailLocators.QRY_GC_MODE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 采集方式
    def inputSel_coll_mode(self, index):
        # self.click(UnControlPlantDetailLocators.QRY_COLL_MODE)
        # locator = self.get_select_locator(UnControlPlantDetailLocators.QRY_COLL_MODE_VALUE, index)
        # self.click(locator)
        self.selectDropDown(index, is_multi_tab=True, is_multi_elements=True)

    # 统计日期
    def inputDt_query_date(self, content):
        # self.exec_script(UnControlPlantDetailLocators.DATE_JS)
        # self.input(content, *UnControlPlantDetailLocators.QRY_DATE)
        self.inputDate(content)

    # 户号
    def inputStr_cons_no(self, content):
        self.input(content)  # , *UnControlPlantDetailLocators.QRY_CONS_NO)

    # 表资产编号
    def inputStr_meter_asset_no(self, content):
        self.input(content)  #, *UnControlPlantDetailLocators.QRY_METER_ASSET_NO)

    # 终端资产编号
    def inputStr_tmnl_addr(self, content):
        self.input(content)  #, *UnControlPlantDetailLocators.QRY_TMNL_ASSET_NO)

    # 查询
    def btn_search(self):
        # self.click(UnControlPlantDetailLocators.BTN_SEARCH)
        self.btn_query(True)
