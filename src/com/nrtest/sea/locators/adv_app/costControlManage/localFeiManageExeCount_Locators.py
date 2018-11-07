# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: localFeiManageExeCount_Locators.py
@time: 2018/8/22 0022 14:25
@desc:
"""
from selenium.webdriver.common.by import By


class LocalFeiManageExeCount_dis_count_Locators:
    # 【显示区】
    # 工单类型
    QRY_WORK_CATA = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'工单类型')]/../div[1]/div/img)[1]")
    QRY_WORK_CATA_VALUE = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'电价参数下发')])[1]/../div[%s]")
    # 费控用户类型
    QRY_FEI_USER_CATA = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'费控用户类型')]/../div[1]/div/img)[1]")
    QRY_FEI_USER_CATA_VALUE = (
        By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'低压居民')])[1]/../div[%s]")
    # 接受日期
    QRY_RECEIVE_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'接收日期')]/../div[1]/div/input)[1]")
    # 结束时间
    QRY_END_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'--至--')]/../div[1]/div/input)[1]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\" x-panel x-panel-noborder x-form-label-right x-column\"]//button[contains(text(),'查询')])[1]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//div[@class=\"x-grid3-row-checker\"])[1]')
    # 工单总数
    TAB_ONE_WORK_ALL = (
        By.XPATH, '(// div[@class =\"x-grid3-row-checker\"])[1]/../../../td[7]/div/a')
    # 执行成功工单数
    TAB_ONE_WORK_SUECESS_ALL = (
        By.XPATH, '(// div[@class =\"x-grid3-row-checker\"])[1]/../../../td[8]/div/a')
    # 执行失败工单数
    TAB_ONE_WORK_FAIL_ALL = (
        By.XPATH, '(// div[@class =\"x-grid3-row-checker\"])[1]/../../../td[9]/div/a')

    # 本地费控执行统计
    BTN_LOCAL_FEI_MANGE_EXE_COUNT = (
        By.XPATH, "(//*[contains(text(),'本地费控执行统计')])[@class=\"x-tab-strip-text money\"]")


class LocalFeiManageExeCount_dis_detail_Locators:
    # 【显示区】
    # 工单类型
    QRY_WORK_CATA = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'工单类型')]/../div[1]/div/img)[2]")
    QRY_WORK_CATA_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'电价参数下发')]/../div[%s]")
    # 费控用户类型
    QRY_FEI_USER_CATA = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'费控用户类型')])[2]/../div[1]/div/img")
    QRY_FEI_USER_CATA_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'低压居民')]/../div[%s]")
    # 接受日期
    QRY_RECEIVE_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'接收日期')]/../div[1]/div/input)[2]")
    # 结束时间
    QRY_END_DATE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'--至--')]/../div[1]/div/input)[2]")
    # 执行状态
    QRY_EXECUTE_STATE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'执行状态:')]/../div[1]/div/img")
    # 执行状态的值
    QRY_EXECUTE_STATE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'失败')]/../div[%s]")
    # 工单编号
    QRY_EMPLOYEE_NUM = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'工单编号')]/../../div[1]/div[1]/input")
    # 用户编号
    QRY_USER_NUM = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'用户编号')]/../../div[1]/div[1]/input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\" x-panel x-panel-noborder x-form-label-right x-column\"]//button[contains(text(),'查询')])[2]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//div[@class=\"x-grid3-row-checker\"])[1]')
