# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: realData_locators.py
@time: 2018/10/12 0012 10:12
@desc:
'''
from selenium.webdriver.common.by import By

# 统计查询→综合查询→抄表数据查询（冀北）
class RealDataLocators:
    #【查询条件区】

    #抄表段号
    QRY_READ_METER_SEGMENT_NO_RDETAIL = (By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'抄表段号')]/../../div[1]/div[1]//input)[1]")
    QRY_READ_METER_SEGMENT_NO_FAILDETAIL = (
    By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'抄表段号')]/../../div[1]/div[1]//input)[2]")

    #电表资产号
    QRY_METER_ASSET_NO_RDETAIL = (By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'电表资产号')]/../../div[1]/div[1]//input)[1]")
    QRY_METER_ASSET_NO_FAILDETAIL = (
    By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'电表资产号')]/../../div[1]/div[1]//input)[2]")

    #用户类型
    QRY_USER_TYPE_RDETAIL = (By.XPATH, "//*[@id=\"consSortComboJb\"]")
    QRY_USER_TYPE_RDETAIL_VALUE = (
        By.XPATH, "//div[@class=\"x-layer x-combo-list \"]//div[contains(text(),'专变')]/../div[contains(text(),'%s')]//img")

    QRY_USER_TYPE_FAILDETAIL = (By.XPATH, "//*[@id=\"consSortCombo_failJb\"]")
    QRY_USER_TYPE_FAILDETAIL_VALUE = (
        By.XPATH, "//div[@class=\"x-layer x-combo-list \"]//div[contains(text(),'专变')]/../div[contains(text(),'%s')]")
    #终端生产厂家
    QRY_TMNL_MANUFACTUREE = (By.XPATH,'//*[@id="tmnlFactoryComboJb"]')
    QRY_TMNL_MANUFACTUREE_VALUE = (
    By.XPATH, "//div[@class=\"x-layer x-combo-list \"]//div[contains(text(),'反向采集失败')]/../div[contains(text(),'全部')]")

    #反向采集结果
    QRY_REVERS_COLLECT_RESULT = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'反向采集结果')]/../../div[1]/div[1]//input")
    QRY_REVERS_COLLECT_RESULT_VALUE= (By.XPATH,"//div[@class=\"x-layer x-combo-list \"]//div[contains(text(),'东方电子')]/../div[contains(text(),'%s')]")
    # 相位
    QRY_PHASE_RDETAIL = (
    By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'相位')]/../../div[1]/div[1]//input)[1]")
    QRY_PHASE_RDETAIL_VALUE = (
    By.XPATH, "//div[@class=\"x-layer x-combo-list \"]//div[contains(text(),'A相')]/../div[contains(text(),'%s')]")

    #相位
    QRY_PHASE_FAILDETAIL = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'相位')]/../../div[1]/div[1]//input)[2]")
    QRY_PHASE_FAILDETAIL_VALUE = (
        By.XPATH, "//div[@class=\"x-layer x-combo-list \"]//div[contains(text(),'A相')]/../div[contains(text(),'%s')]")

    # 数据类别
    QRY_DATATYPE_RDETAIL = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'数据类别')]/../../div[1]/div[1]//input)[1]")
    QRY_DATATYPE_RDETAIL_VALUE = (
        By.XPATH, "//div[@class=\"x-layer x-combo-list \"]//div[contains(text(),'正常采集')]/../div[contains(text(),'%s')]")

    # 电能表抄表状态
    QRY_METER_READ_STATE_RDETAIL = (
        By.XPATH, "//*[@id=\"metStatusComboBoxJb\"]")
    QRY_METER_READ_STATE_RDETAIL_VALUE = (
        By.XPATH, "//div[@class=\"x-layer x-combo-list \"]//div[contains(text(),'未停抄')]/../div[contains(text(),'%s')]")

    # 电能表抄表状态
    QRY_METER_READ_STATE_FAILDETAIL = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'电能表抄表状态')]/../../div[1]/div[1]//input)[2]")
    QRY_METER_READ_STATE_FAILDETAIL_VALUE = (
        By.XPATH, "//div[@class=\"x-layer x-combo-list \"]//div[contains(text(),'未停抄')]/../div[contains(text(),'%s')]")

    # 终端运行状态
    QRY_TMNL_RUN_STATE_RDETAIL = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'终端运行状态')]/../../div[1]/div[1]//input)[1]")
    QRY_TMNL_RUN_STATE_RDETAIL_VALUE = (
        By.XPATH, "//div[@class=\"x-layer x-combo-list \"]//div[contains(text(),'运行')]/../div[contains(text(),'%s')]")
    #查询时间
    QRY_TIME_RDETAIL = (By.XPATH,'//*[@id="sendDataQueryDateStartJb"]')
    QRY_TIME_FAILTIME = (By.XPATH,'//*[@id="sendDataQueryDateStart_failJb"]')


    # 终端运行状态
    QRY_TMNL_RUN_STATE_FAILDETAIL = (
        By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'终端运行状态')]/../../div[1]/div[1]//input)[1]")
    QRY_TMNL_RUN_STATE_FAILDETAIL_VALUE = (
        By.XPATH, "//div[@class=\"x-layer x-combo-list \"]//div[contains(text(),'运行')]/../div[contains(text(),'%s')]")

    # 【操作区】
    BTN_QRY_RDETAIL = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")
    BTN_QRY_FAILDETAIL = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[2]")

    #【js区】
    # 开始时间，删除readonly属性
    QUERY_TIME_RDETAIL = 'document.getElementById("sendDataQueryDateStartJb").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    QUERY_TIME_FAILDETAIL = 'document.getElementById("sendDataQueryDateStart_failJb").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    #【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
     
     
     
     
     