# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: tmnlInstallDetai.py
@time: 2018/10/16 0016 15:06
@desc:
"""
from selenium.webdriver.common.by import By


# 基本应用→终端管理→远程调试

class TmnlInstallDetaiLocators:
    # 【查询条件区】
    # 终端类型
    QRY_TMNL_TYPE = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'终端类型')]/../../div[1]/div[1]//input)[1]")
    QRY_TMNL_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'负荷控制终端')]/../div[contains(text(),'%s')]")
    # 开始时间
    QRY_START_TIME = (By.XPATH, "//*[@id=\"tmnlInstallStartMonth\"]")

    # 结束时间
    QRY_END_TIME = (By.XPATH, "//*[@id=\"tmnlInstallEndMonth\"]")

    # 【操作区】
    BTN_WORK_COUNT_QRY = (By.XPATH,
                          "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("tmnlInstallStartMonth").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("tmnlInstallEndMonth").removeAttribute("readonly");'
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")

    # ----------------------------------------------终端调式页面-----------------------------------------
    # 【查询条件】
    # 申请单号
    QRY_APPLY_STATE_COUNT = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'申请单号')]/../../div[1]/div[1]//input)[1]")
    # 用户编号
    QRY_USER_NO_COUNT = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'用户编号')]/../../div[1]/div[1]//input)[1]")

    # 终端地址
    QRY_TMNL_ADDR_COUNT = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'终端地址')]/../../div[1]/div[1]//input)[1]")

    # 开始时间
    QRY_START_TIME_COUNT = (By.XPATH, '//*[@id="tmnlStartDate"]')
    # 结束世间
    QRY_END_TIME_COUNT = (By.XPATH, '//*[@id="tmnlEndDate"]')

    # 运行状态
    QRY_RUN_STATE_COUNT = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'运行状态')]/../../div[1]/div[1]//input)[1]")
    QRY_RUN_STATE_COUNT_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'离线')]/../div[contains(text(),'%s')]")
    # 流程标识
    QRY_PROCESS_ID_COUNT = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'流程标识')]/../../div[1]/div[1]//input)[1]")
    QRY_PROCESS_ID_COUNT_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'负控')]/../div[contains(text(),'%s')]")

    # 装接类型
    QRY_MOUNTING_COUNT = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'装接类型')]/../../div[1]/div[1]//input)[1]")
    QRY_MOUNTING_COUNT_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'终端安装')]/../div[contains(text(),'%s')]")

    # 表类型
    QRY_SURFACE_TYPE_COUNT = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'表类型')]/../../div[1]/div[1]/div/img")
    QRY_SURFACE_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'电表')]/../div[contains(text(),'%s')]")

    # 终端厂家
    QRY_TMNL_FACTORY_COUNT = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'终端厂家')]/../../div[1]/div[1]//input)[1]")

    # 终端类型
    QRY_TMNL_TYPE_COUNT = (By.XPATH, '//*[@id="tilldet_interfaceType"]')

    # 通信规约
    QRY_LCT_COUNT = (By.XPATH, '//*[@id="protocolCodeName_tmnlTaskConfig"]')

    # 【操作区】
    BTN_TMNL_QRY = (By.XPATH,
                    "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[2]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS_COUNT = 'document.getElementById("tmnlStartDate").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS_COUNT = 'document.getElementById("tmnlEndDate").removeAttribute("readonly");'
    # 终端厂家
    TMNL_FACTORY_JS_COUNT = 'document.getElementById("anhuitmnlFacRadiocombo").removeAttribute("readonly");'
    # 终端类型
    TMNL_TYPE_JS_COUNT = 'document.getElementById("tilldet_interfaceType").removeAttribute("readonly");'
    # 通信规约
    LCT_JS_COUNT = 'document.getElementById("protocolCodeName_tmnlTaskConfig").removeAttribute("readonly");'
    # 电表类型
    METER_TYPE_JS_COUNT = 'document.getElementsByTagName(\'input\')[29].removeAttribute("readonly");'
