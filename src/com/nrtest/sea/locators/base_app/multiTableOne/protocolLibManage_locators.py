# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: protocolLibManage_locators.py
@time: 2018/10/17 0017 15:13
@desc:
"""
from selenium.webdriver.common.by import By


# 基本应用--》多表合一--》协议管理
class ProtocolLibManageLocators:
    # 【查询条件区】
    # 协议名称
    QRY_PROTOCOL_NAME = (By.XPATH, '//*[@id="protocolLib_protocolName"]')
    # 厂商名称
    QRY_MANUFACTORY_NAME = (By.XPATH, "//*[@id=\"protocolLib_factoryName\"]")
    # 协议类型
    QRY_PROTOCOL_TYPE = (By.XPATH, "//*[@id=\"protocolLib_protocolType\"]")

    QRY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'新增')]/../div[contains(text(),'%s')]")
    # 表记类型
    QRY_SURFACE_TYPE = (By.XPATH, "//*[@id=\"protocolLib_meterType\"]")
    # 维护时间
    QRY_MAINTENANCE_TIME = (By.XPATH, "//*[@id=\"protocolLib_startDate\"]")
    # 结束时间
    QRY_END_TIME = (By.XPATH, '//*[@id="protocolLib_endDate"]')
    # 有效标志
    QRY_EFFECTIVE_SIGN = (By.XPATH, '//*[@id="protocolLib_protocolValid"]')
    QRY_EFFECTIVE_SIGN_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'有效')]/../div[contains(text(),'%s')]")
    # 协议版本号
    QRY_PROTOCOL_VERSION_NO = (By.XPATH, '//*[@id="protocolLib_protocolVersionNo"]')
    # 协议代码
    QEY_PROTOCOL_CODE = (By.XPATH, '//*[@id="protocolLib_protocolID"]')

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("protocolLib_startDate").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("protocolLib_endDate").removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
