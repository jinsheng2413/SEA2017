# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: costControlManage_page.py
@time: 2018/8/2 0002 18:53
@desc:
"""
from selenium import webdriver

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.costControlManage.costControlManage_page_locators import \
    CostControlManagePageLocators


class CostControlManagePage(Page):
    # 点击左边加号
    def btn_left_add(self):
        self.click(*CostControlManagePageLocators.LEFT_ADD)

    # 点击唐山供电公司
    def btn_t_company(self):
        self.click(*CostControlManagePageLocators.T_COMPANY)

    # 营销单号
    def inputStr_mark_sigle(self, value):
        self.input(value, *CostControlManagePageLocators.QRY_MARKETINF_SINGLE_NUM)

    # 终端地址
    def inputStr_terminal_addr(self, value):
        self.input(value, *CostControlManagePageLocators.QRY_TERMIAL_ADDR)

    # 用户编号
    def inputStr_user_num(self, value):
        self.input(value, *CostControlManagePageLocators.QRY_USER_NUM)

    # 用户名称
    def inputStr_user_name(self, value):
        self.input(value, *CostControlManagePageLocators.QRY_USER_NAME)

    # 业务类型
    def inputSel_buniess_cata(self, index):
        self.click(*CostControlManagePageLocators.SEL_BUNIESS_CATA)
        locator = self.get_select_locator(CostControlManagePageLocators.SEL_BUNIESS_CATA_VALUE, index)
        # print(locator)
        self.click(*locator)

    # 参数下发状态
    def inputSel_para_deve(self, index):
        self.click(*CostControlManagePageLocators.SEL_PARA_DEVE)
        locator = self.get_select_locator(CostControlManagePageLocators.SEL_PARA_DEVE_VALUE, index)
        self.click(*locator)

    # 购电日期
    def inputRSel_buy_ele_date(self, index):
        self.click(*CostControlManagePageLocators.SELR_ARRANGE)
        locator = self.get_select_locator(CostControlManagePageLocators.SELR_ARRANGE_VALUE, index)
        self.click(*locator)

    # 开始时间
    def input_start_date(self, value):
        self.exec_script(CostControlManagePageLocators.START_DATE_JS)
        self.input(value, *CostControlManagePageLocators.DATE_START)

    # 结束时间
    def input_end_date(self, value):
        self.exec_script(CostControlManagePageLocators.END_DATE_JS)
        self.input(value, *CostControlManagePageLocators.DATE_END)

    # 点击查询按钮
    def btn_qry(self):
        self.click(*CostControlManagePageLocators.BTN_QRY)


if __name__ == '__main__':
    dr = webdriver.Chrome()

    p = CostControlManagePage(dr)

    p.clear_values(CostControlManagePage)
