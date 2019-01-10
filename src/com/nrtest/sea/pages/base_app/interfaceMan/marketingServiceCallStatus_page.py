# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: mServiceCallStatus_page.py
@time: 2018-10-15 14:40
@desc:
"""

from selenium.webdriver.common.by import By

from com.nrtest.common.base_page import Page


class MarketingServiceCallStatusPage(Page):
    # 业务系统
    def inputSel_business_system(self, value):
        self.selectDropDown(value, is_multi_elements=True, is_multi_tab=True)

    # 服务名称
    def inputSel_business_name(self, value):
        self.selectDropDown(value, is_multi_elements=True, is_multi_tab=True)

    # 调用时间
    def inputDt_start_date(self, value):
        self.inputDate(value)

    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.click((By.XPATH, '//button[text()="统计"]'))


class MarketingServiceCallStatus_detail_Page(Page):
    # 业务系统
    def inputSel_business_system(self, value):
        # self.click(MServiceCallStatus2Locators.QRY_BUSINESS_SYSTEM)
        # locator = self.get_select_locator(
        #     MServiceCallStatus2Locators.QRY_BUSINESS_SYSTEM_VALUE, value)
        # self.click(locator)
        self.selectDropDown(value, is_multi_elements=True, is_multi_tab=True)

    # 服务名称
    def inputSel_business_name(self, value):
        # self.click(MServiceCallStatus2Locators.QRY_BUSINESS_NAME)
        # locator = self.get_select_locator(
        #     MServiceCallStatus2Locators.QRY_BUSINESS_NAME_VALUE, value)
        # self.click(locator)
        self.selectDropDown(value, is_multi_elements=True, is_multi_tab=True)

    # 调用时间
    def inputDt_start_date(self, value):
        # self.input(value, *MServiceCallStatus2Locators.QRY_DATE_BEGIN)
        self.inputDate(value)

    def inputDt_end_date(self, value):
        # self.input(value, *MServiceCallStatus2Locators.QRY_DATE_END)
        self.inputDate(value)

    # 工单编号
    def inputStr_app_no(self, name):
        self.input(name)

    # 查询
    def btn_qry(self):
        # self.click(MServiceCallStatus2Locators.BTN_QUERY)
        self.btn_query()
