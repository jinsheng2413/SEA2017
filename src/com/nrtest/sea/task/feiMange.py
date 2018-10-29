# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: feiMange.py
@time: 2018/8/2 0002 18:40
@desc:
"""
from com.nrtest.common.setting import Setting
from com.nrtest.sea.locators.adv_app.costControlManage.custControlCommissioning_locators import \
    CustControlCommissioning_locators
from com.nrtest.sea.pages.adv_app.costControlManage.costControlManage_page import CostControlManagePage
from com.nrtest.sea.pages.adv_app.costControlManage.lowUserMoneyCheck_Page import BalanceCheck_page
from com.nrtest.sea.pages.other.common_page import Common_page
from com.nrtest.sea.task.login import Login


# 专变用户费控管理
def specil_user_fei_mange():
    lg = Login(Setting.DEFAULT_USER, Setting.DEFAULT_PASSWORD)
    dr = lg.login()
    # 点击高级应用
    cp = Common_page(dr)
    cp.btn_advApp()
    # 点击费控管理
    cp.btn_fei_mange()
    cp.hover_local_fei_mange()
    cp.btn_specil_user_fei_mange()
    ccm = CostControlManagePage(cp.driver)
    ccm.btn_left_add()
    ccm.btn_t_company()
    return ccm.driver


# 低压用户余额查看_余额统计
def low_user_money_check():
    lg = Login(Setting.DEFAULT_USER, Setting.DEFAULT_PASSWORD)
    dr = lg.login()
    # 点击高级应用
    cp = Common_page(dr)
    cp.btn_advApp()
    # 点击费控管理
    cp.btn_fei_mange()
    cp.hover_local_fei_mange()
    cp.btn_low_user_money_check()
    cp.btn_left_add()
    cp.sleep_time(1)
    cp.btn_select_company(2)
    return cp.driver


# 低压用户余额查看_余额查看
def low_user_money_check_two():
    lg = Login(Setting.DEFAULT_USER, Setting.DEFAULT_PASSWORD)
    dr = lg.login()
    # 点击高级应用
    cp = Common_page(dr)
    cp.btn_advApp()
    # 点击费控管理
    cp.btn_fei_mange()
    cp.hover_local_fei_mange()
    cp.btn_low_user_money_check()
    print("------------")
    b = BalanceCheck_page(cp.driver)
    b.btn_balance_check()
    cp.driver = b.driver
    cp.btn_left_add()
    cp.sleep_time(1)
    cp.btn_select_company(6)

    return cp.driver


# 电价参数下发
def ele_price_para():
    lg = Login(Setting.DEFAULT_USER, Setting.DEFAULT_PASSWORD)
    dr = lg.login()
    # 点击高级应用
    cp = Common_page(dr)
    cp.btn_advApp()
    # 点击费控管理
    cp.btn_fei_mange()
    cp.hover_local_fei_mange()
    cp.btn_ele_price_para()
    cp.btn_left_add()
    cp.sleep_time(1)
    cp.btn_select_company(6)

    return cp.driver


# 专变用户余额查看
def specialUserBalanceQuery():
    lg = Login(Setting.DEFAULT_USER, Setting.DEFAULT_PASSWORD)
    dr = lg.login()
    # 点击高级应用
    cp = Common_page(dr)
    cp.btn_advApp()
    # 点击费控管理
    cp.btn_fei_mange()
    cp.hover_local_fei_mange()
    cp.btn_specialUserBalanceQuery()
    cp.btn_left_add()
    cp.sleep_time(1)
    cp.btn_select_company(6)
    cp.sleep_time(2)
    js = "document.getElementsByTagName('input')[8].removeAttribute(\"readOnly\")"
    cp.exec_script(js)

    return cp.driver


# 低压用户购电参数下发
def lowUserBuyParaGiveOut():
    lg = Login(Setting.DEFAULT_USER, Setting.DEFAULT_PASSWORD)
    dr = lg.login()
    # 点击高级应用
    cp = Common_page(dr)
    cp.btn_advApp()
    # 点击费控管理
    cp.btn_fei_mange()
    cp.hover_local_fei_mange()
    cp.btn_lowUserBuyParaGiveOut()
    cp.btn_left_add()
    cp.sleep_time(1)
    cp.btn_select_company(3)

    return cp.driver


# 本地费控执行统计_费控情况统计
def localFeiManageCount_dis_count():
    lg = Login(Setting.DEFAULT_USER, Setting.DEFAULT_PASSWORD)
    dr = lg.login()
    # 点击高级应用
    cp = Common_page(dr)
    cp.btn_advApp()
    # 点击费控管理
    cp.btn_fei_mange()
    cp.hover_local_fei_mange()
    cp.btn_localFeiMangeExecutCount()
    cp.btn_left_add()
    cp.sleep_time(1)
    cp.btn_select_company(4)

    return cp.driver


# 本地费控执行统计_费控情况明细
def localFeiManageCount_dis_detail():
    lg = Login(Setting.DEFAULT_USER, Setting.DEFAULT_PASSWORD)
    dr = lg.login()
    # 点击高级应用
    cp = Common_page(dr)
    cp.btn_advApp()
    # 点击费控管理
    cp.btn_fei_mange()
    cp.hover_local_fei_mange()
    cp.btn_localFeiMangeExecutCount()
    cp.btn_localFeiMangeExecutCount_dis_detail()
    cp.btn_left_add()
    cp.sleep_time(1)
    cp.btn_select_company(6)

    return cp.driver


# 费控投入调试_电量控
def custControlCommissioning_ele_manage():
    lg = Login(Setting.DEFAULT_USER, Setting.DEFAULT_PASSWORD)
    dr = lg.login()
    # 点击高级应用
    cp = Common_page(dr)
    cp.btn_advApp()
    # 点击费控管理
    cp.btn_fei_mange()
    cp.hover_local_fei_mange()
    cp.btn_cust_control_commssioning()
    cp.sleep_time(2)
    cp.exec_script(CustControlCommissioning_locators.START_DATE_JS)
    cp.exec_script(CustControlCommissioning_locators.END_DATE_JS)
    cp.btn_left_add()
    cp.sleep_time(1)
    cp.btn_select_company(2)

    return cp.driver


# 费控投入调试_电fei控
def custControlCommissioning_ele_cust():
    lg = Login(Setting.DEFAULT_USER, Setting.DEFAULT_PASSWORD)
    dr = lg.login()
    # 点击高级应用
    cp = Common_page(dr)
    cp.btn_advApp()
    # 点击费控管理
    cp.btn_fei_mange()
    cp.hover_local_fei_mange()
    cp.btn_cust_control_commssioning()
    cp.btn_ele_cust_mange()
    cp.exec_script(CustControlCommissioning_locators.START_DATE_JS)
    cp.exec_script(CustControlCommissioning_locators.END_DATE_JS)
    cp.btn_left_add()
    cp.sleep_time(1)
    cp.btn_select_company(4)

    return cp.driver


if __name__ == '__main__':
    custControlCommissioning_ele_cust()
