# -*- coding: utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: vipConsStealAnal_locators.py
@time: 2018-11-05 13:44
@desc:
'''
from selenium.webdriver.common.by import By


# 高级应用--》重点用户监测--》重点用户窃电分析
class VipConsStealAnal_locators:
    # [显示区]
    # 节点名
    QRY_ORG = (By.XPATH, "//input[@id='vipConsStealNodeName']")
    # 用户编号
    QRY_CONS_NO = (By.XPATH, "//label[contains(text(),'用户编号')]/../div/input")
    # 用户名称
    QRY_CONS_NAME = (By.XPATH, "//label[contains(text(),'用户名称')]/../div/input")
    # 类型--正常
    QRY_TYPE_NORMAL = (By.XPATH, "//label[contains(text(),'正常')]")
    # 类型--异常
    QRY_TYPE_ABNORMAL = (By.XPATH, "//label[contains(text(),'异常')]")

    # 【操作区】
    # 【查询】
    BTN_QUERY = (By.XPATH, "(//button[contains(text(),'查询')])[2]")

    # [显示区]
    TAB_ONE = (By.XPATH, "(//div[@class='x-grid3-scroller'])[1]")
