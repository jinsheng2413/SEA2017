# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: lowUserBuyEleParaGiveOut_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


class ReadCompleteRatePage(Page):
    # 蕊片厂家
    def inputSel_chipFactory(self, name):
        # self.click(*ReadCompleteRateLocators.QRY_CHIP_FACTORY)
        # locator = self.get_select_locator(
        #     ReadCompleteRateLocators.QRY_CHIP_FACTORY_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    #  蕊片厂家
    def inputSel_chipFactoryCount(self, name):
        # self.click(*ReadCompleteRateLocators.QRY_CHIP_FACTORY_COUNT)
        # locator = self.get_select_locator(
        #     ReadCompleteRateLocators.QRY_CHIP_FACTORY_COUNT_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    #  蕊片厂家
    def inputSel_chipFactoryDetail(self, name):
        # self.click(*ReadCompleteRateLocators.QRY_CHIP_FACTORY_DETAIL)
        # locator = self.get_select_locator(
        #     ReadCompleteRateLocators.QRY_CHIP_FACTORY_DETAIL_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 终端厂家
    def inputSel_tmnlFactory(self, name):
        # self.click(*ReadCompleteRateLocators.QRY_TMNL_FACTORY)
        # locator = self.get_select_locator(
        #     ReadCompleteRateLocators.QRY_TMNL_FACTORY_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 终端厂家
    def inputSel_tmnlFactoryCount(self, name):
        # self.click(*ReadCompleteRateLocators.QRY_TMNL_FACTORY_COUNT)
        # locator = self.get_select_locator(
        #     ReadCompleteRateLocators.QRY_TMNL_FACTORY_COUNT_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 终端厂家
    def inputSel_ctmnlFactoryDetail(self, name):
        # self.click(*ReadCompleteRateLocators.QRY_TMNL_FACTORY_DETAIL)
        # locator = self.get_select_locator(
        #     ReadCompleteRateLocators.QRY_TMNL_FACTORY_DETAIL_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 通信方式
    def inputSel_communicationMode(self, name):
        # self.click(*ReadCompleteRateLocators.QRY_COMMUNICATION_MODE)
        # locator = self.get_select_locator(
        #     ReadCompleteRateLocators.QRY_COMMUNICATION_MODE_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 通信方式
    def inputSel_communicationModeCount(self, name):
        # self.click(*ReadCompleteRateLocators.QRY_COMMUNICATION_MODE_COUNT)
        # locator = self.get_select_locator(
        #     ReadCompleteRateLocators.QRY_COMMUNICATION_MODE_COUNT_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 通信方式
    def inputSel_communicationModeDetail(self, name):
        # self.click(*ReadCompleteRateLocators.QRY_COMMUNICATION_MODE_DETAIL)
        # locator = self.get_select_locator(
        #     ReadCompleteRateLocators.QRY_COMMUNICATION_MODE_DETAIL_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 用户类型
    def inputSel_userType_detail(self, name):
        # self.click(*ReadCompleteRateLocators.QRY_USER_TYPE_DETAIL)
        # locator = self.get_select_locator(
        #     ReadCompleteRateLocators.QRY_USER_TYPE_DETAIL_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 用户类型
    def inputSel_userType_count(self, name):
        # self.click(*ReadCompleteRateLocators.QRY_USER_TYPE_COUNT)
        # locator = self.get_select_locator(
        #     ReadCompleteRateLocators.QRY_USER_TYPE_COUNT_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 用户类型
    def inputSel_userType(self, name):
        # self.click(*ReadCompleteRateLocators.QRY_USER_TYPE)
        # locator = self.get_select_locator(
        #     ReadCompleteRateLocators.QRY_USER_TYPE_VALUE, name)
        # self.click(*locator)
        self.selectDropDown(name, is_multi_tab=True, is_multi_elements=True)

    # 开始时间
    def inputStr_start_time(self, value):
        # self.input(value, *ReadCompleteRateLocators.QRY_START_TIME)
        self.input(value)

    # 结束时间
    def inputStr_end_time(self, value):
        # self.input(value, *ReadCompleteRateLocators.QRY_END_TIME)
        self.input(value)

    # 日期时间
    def inputStr_date_time_count(self, value):
        # self.input(value, *ReadCompleteRateLocators.QRY_DATE_TIME_COUNT)
        self.input(value)

    # 日期时间
    def inputStr_date_time_detail(self, value):
        # self.input(value, *ReadCompleteRateLocators.QRY_DATE_TIME_DETAIL)
        self.input(value)

    # # 查询
    # def btn_qry(self):
    #     self.click(*ReadCompleteRateLocators.BTN_QRY)
    #
    # # 查询
    # def btn_count_qry(self):
    #     self.click(*ReadCompleteRateLocators.BTN_QRY_COUNT)
    #
    # # 查询
    # def btn_detail_qry(self):
    #     self.click(*ReadCompleteRateLocators.BTN_QRY_DETAIL)
