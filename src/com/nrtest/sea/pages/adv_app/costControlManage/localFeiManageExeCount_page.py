# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: localFeiManageExeCount_page.py
@time: 2018/8/22 0022 15:39
@desc:
'''
from com.nrtest.sea.locators.adv_app.costControlManage.localFeiManageExeCount_Locators import LocalFeiManageExeCount_dis_count_Locators,LocalFeiManageExeCount_dis_detail_Locators
from com.nrtest.common.base_page import Page
class LocalFeiManageExeCount_dis_count_Page(Page):
    #工单类型
    def inputSel_work_cata(self,index):
        self.click(*LocalFeiManageExeCount_dis_count_Locators.QRY_WORK_CATA)
        locator = self.get_select_locator(LocalFeiManageExeCount_dis_count_Locators.QRY_WORK_CATA_VALUE, index)
        # print(locator)
        self.click(*locator)

    #费控用户类型
    def inputSel_feiUserCata(self,index):
        self.click(*LocalFeiManageExeCount_dis_count_Locators.QRY_FEI_USER_CATA)
        locator = self.get_select_locator(LocalFeiManageExeCount_dis_count_Locators.QRY_FEI_USER_CATA_VALUE, index)
        # print(locator)
        self.click(*locator)

    #接收时间

    def inputStr_receive_time(self, value):
            self.input(value, *LocalFeiManageExeCount_dis_count_Locators.QRY_RECEIVE_DATE)


    # 结束时间
    def inputStr_end_time(self, value):
            self.input(value, *LocalFeiManageExeCount_dis_count_Locators.QRY_END_DATE)

    # 查询
    def btn_qry(self):
        self.click(*LocalFeiManageExeCount_dis_count_Locators.BTN_QRY)

    # 工单总数
    def btn_work_all(self):
        self.click(*LocalFeiManageExeCount_dis_count_Locators.TAB_ONE_WORK_ALL)

    # 执行成功工单总数
    def btn_work_success_all(self):
        self.click(*LocalFeiManageExeCount_dis_count_Locators.TAB_ONE_WORK_SUECESS_ALL)

   # 执行成功工单总数
    def btn_work_fail_all(self):
        self.click(*LocalFeiManageExeCount_dis_count_Locators.TAB_ONE_WORK_FAIL_ALL)

    #点击菜单
    def btn_localFeiMangeexeCount(self):
        self.click(*LocalFeiManageExeCount_dis_count_Locators.BTN_LOCAL_FEI_MANGE_EXE_COUNT)

class LocalFeiManageExeCount_dis_detail_Page(Page):
    # 工单类型
    def inputSel_work_cata(self, index):
        self.click(*LocalFeiManageExeCount_dis_detail_Locators.QRY_WORK_CATA)
        locator = self.get_select_locator(LocalFeiManageExeCount_dis_detail_Locators.QRY_WORK_CATA_VALUE, index)
        # print(locator)
        self.click(*locator)

    # 费控用户类型
    def inputSel_feiUserCata(self, index):
        self.click(*LocalFeiManageExeCount_dis_detail_Locators.QRY_FEI_USER_CATA)
        locator = self.get_select_locator(LocalFeiManageExeCount_dis_detail_Locators.QRY_FEI_USER_CATA_VALUE, index)
        # print(locator)
        self.click(*locator)

    # 执行状态
    def inputSel_execute_state(self, index):
        self.click(*LocalFeiManageExeCount_dis_detail_Locators.QRY_EXECUTE_STATE)
        locator = self.get_select_locator(LocalFeiManageExeCount_dis_detail_Locators.QRY_EXECUTE_STATE_VALUE, index)
        # print(locator)
        self.click(*locator)

    # 接收时间

    def inputStr_receive_time(self, value):
        self.input(value, *LocalFeiManageExeCount_dis_detail_Locators.QRY_RECEIVE_DATE)

    # 结束时间
    def inputStr_end_time(self, value):
        self.input(value, *LocalFeiManageExeCount_dis_detail_Locators.QRY_END_DATE)

    # 工单编号
    def inputStr_work_num(self, value):
        self.input(value, *LocalFeiManageExeCount_dis_detail_Locators.QRY_EMPLOYEE_NUM)

    # 用户编号
    def inputStr_user_num(self, value):
        self.input(value, *LocalFeiManageExeCount_dis_detail_Locators.QRY_USER_NUM)

    # 查询
    def btn_qry(self):
        self.click(*LocalFeiManageExeCount_dis_detail_Locators.BTN_QRY)

