# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesMaintain_locators.py
@time: 2018/8/30 0030 14:43
@desc:
"""
from com.nrtest.common.base_page import Page


# 档案维护
class ArchivesMaintain_pages(Page):


    # 【查询名称】
    # 厂站名称
    def inputSel_factoryNmae(self, index):
        # self.click(ArchivesMaintain_locators.QRY_FACTORY_NAME)
        # locator = self.get_select_locator(
        #     ArchivesMaintain_locators.QRY_FACTORY_NAME_VALUE, index)
        # # print(locator)
        # self.click(locator)
        self.selectDropDown(index)

    # 电压等级
    def inputStr_eleGrade(self, index):
        # self.click(ArchivesMaintain_locators.QRY_ELE_GRADE)
        # locator = self.get_select_locator(
        #     ArchivesMaintain_locators.QRY_ELE_GRADE_VALUE, index)
        # # print(locator)
        # self.click(locator)
        self.selectDropDown(index)

    # 终端资产号
    def inputStr_termainalAssetNo(self, value):
        self.input(value)  # , *ArchivesMaintain_locators.QRY_TERMINAL_ASSET_NO)

    # 终端地址
    def inputStr_termainalAddr(self, value):
        self.input(value)  # , *ArchivesMaintain_locators.QRY_TERMINAL_ADDR)

    def btn_qry(self):
        # self.click(ArchivesMaintain_locators.BTN_FACTORY_QRY)
        self.btn_query(True)

class ArchivesMaintain_factory_pages(Page):


    # 电压等级
    def inputSel_eleGrade(self, index):
        # self.click(ArchivesMaintain_locators.QRY_ELE_GRADE)
        # locator = self.get_select_locator(
        #     ArchivesMaintain_locators.QRY_ELE_GRADE_VALUE, index)
        # # print(locator)
        # self.click(locator)
        self.selectDropDown(index)

    def btn_qry(self):
        # self.click(ArchivesMaintain_locators.BTN_FACTORY_QRY)
        self.btn_query(True)


class ArchivesMaintain_terminal_pages(Page):

    # 【查询名称】
    # 厂站名称
    def inputSel_factoryName(self, option):
        # self.click(ArchivesMaintain_locators.QRY_FACTORY_NAME)
        # locator = self.get_select_locator(
        #     ArchivesMaintain_locators.QRY_FACTORY_NAME_VALUE, index)
        # # print(locator)
        # self.click(locator)
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    def btn_qry(self):
        # self.click(ArchivesMaintain_locators.BTN_FACTORY_QRY)
        self.btn_query(True)


class ArchivesMaintain_meter_pages(Page):

    # 【查询名称】

    # 终端资产号
    def inputStr_termainalAssetNo(self, value):
        self.input(value)  #, *ArchivesMaintain_locators.QRY_TERMINAL_ASSET_NO)

    # 终端地址
    def inputStr_termainalAddr(self, value):
        self.input(value)  # , *ArchivesMaintain_locators.QRY_TERMINAL_ADDR)

    def btn_qry(self):
        # self.click(ArchivesMaintain_locators.BTN_METER_QRY)
        self.btn_query(True)
