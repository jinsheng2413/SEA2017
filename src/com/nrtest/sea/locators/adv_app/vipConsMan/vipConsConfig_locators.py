# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: vipConsConfig_locators.py
@time: 2018-11-05 10:20
@desc:
"""

from selenium.webdriver.common.by import By


# 高级应用--》重点用户监测--》重点用户管理
class VipConsConfig_locators:
    # [显示区]
    # 请选择节点
    QRY_ORG = (By.XPATH, "//input[@id='vipConsOrgName']")
    # [运行容量等级]
    QRY_RUN_LEVEL = (
        By.XPATH, "//label[contains(text(),'运行容量等级')]/../div/div/img")
    # 值（运行容量等级）
    QRY_RUN_LEVEL_VALUE = (
        By.XPATH,
        "(//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'<50')])[1]/../div[contains(text(),'%s')]")
    # 供电电压
    QRY_VOLTAGE_LEVEL = (
        By.XPATH, "//label[contains(text(),'供电电压')]/../div/div/img")
    # 行业--选择
    BTN_FACTORY_SELECT = (By.XPATH, "//button[contains(text(),'选择')]")
    # 行业--清除
    BTN_FACTORY_CLEAR = (By.XPATH, "(//button[contains(text(),'清除')])[1]")
    # 用户编号
    QRY_CONS_NO = (By.XPATH, "//label[contains(text(),'用户编号')]/../div/input")
    # 用户名称
    QRY_CONS_NAME = (By.XPATH, "//label[contains(text(),'用户名称')]/../div/input")
    # 已定义重点用户
    QRY_VIP_CONS = (By.XPATH, "//input[@name='isqueryvip']")

    # 【操作区】
    # 【查询】
    BTN_QUERY = (By.XPATH, "(//button[contains(text(),'查询')])[2]")

    # [显示区]
    TAB_ONE = (By.XPATH, "(//div[@class='x-grid3-scroller'])[1]")
