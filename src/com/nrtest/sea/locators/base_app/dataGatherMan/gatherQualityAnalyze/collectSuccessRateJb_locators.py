# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: collectSuccessRateJb_locators.py
@time: 2018/9/30 0030 14:12
@desc:
"""
from selenium.webdriver.common.by import By


# 基本应用→数据采集管理→采集质量分析→采集成功率(冀北)
class CollectSuccessRateJbLocators:
    # 【查询条件区】
    # 通信类型
    QRY_CONMUNICATION_TYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'用户类型')]/../../div[1]/div[1]//input")
    QRY_CONMUNICATION_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'专变')]/../div[contains(text(),'%s')]")
    # 相位
    QRY_PHASE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'相位')]/../../div[1]/div[1]//input")
    QRY_PHASE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'A相')]/../div[contains(text(),'%s')]")
    # 通信方式
    QRY_COMUNICATION_MODE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'通信方式')]/../../div[1]/div[1]//input")
    QRY_COMUNICATION_MODE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'GPRS')]/../div[contains(text(),'%s')]")
    # 终端厂家
    QRY_TMNL_FACTORY = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端厂家')]/../../div[1]/div[1]//input")
    QRY_TMNL_FACTORY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'上海协同')]/../div[contains(text(),'%s')]")
    # 芯片厂家
    QRY_PIECE_FACTORY = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'芯片厂家')]/../../div[1]/div[1]//input")
    QRY_PIECE_FACTORY_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'瑞斯康')]/../div[contains(text(),'%s')]")
    # 通讯规约
    QRY_COMUNICATION_GLUE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'通讯规约')]/../../div[1]/div[1]//input")
    QRY_COMUNICATION_GLUE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'05规约')]/../div[contains(text(),'%s')]")
    # 日期时间
    QRY_DATE_TIME = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'日期时间')]/../../div[1]/div[1]//input")
    # 用户类型
    QRY_USER_TYPE = (
        By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'用户类型')]/../../div[1]/div[1]//input")
    QRY_USER_TYPE_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'专变')]/../div[contains(text(),'%s')]")
    #
    QRY_ = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'')]/../../div[1]/div[1]//input")
    #
    QRY_ = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("readDateJb").removeAttribute("readonly");'

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
