# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: mInterfaceRunStatus_page.py
@time: 2018-10-30 11:21
@desc:
"""

from com.nrtest.common.base_page import Page


class MInterfaceRunStatusPage(Page):
    # 业务系统
    def inputSel_business_system(self, option):
        # self.click(MInterfaceRunStatusLocators.QRY_BUSINESS_SYSTEM)
        # locator = self.get_select_locator(
        #     MInterfaceRunStatusLocators.QRY_BUSINESS_SYSTEM_VALUE, option)
        # self.click(locator)
        self.selectDropDown(option)

    # 服务对象名称
    def inputSel_service_name(self, option):
        # self.click(MInterfaceRunStatusLocators.QRY_SERVICE_NAME)
        # locator = self.get_select_locator(
        #     MInterfaceRunStatusLocators.QRY_SERVICE_NAME_VALUE, option)
        # self.click(locator)
        # print('------')
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        # self.click(MInterfaceRunStatusLocators.BTN_QRY)
        self.btn_query()
