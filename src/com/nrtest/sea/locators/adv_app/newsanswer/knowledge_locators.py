# -*- coding: utf-8 -*-

'''
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: knowledge_locators.py
@time: 2018-11-02 11:23
@desc:
'''

from selenium.webdriver.common.by import By


class Knowledge_Locators:
    # [显示区]
    # 供电公司
    QRY_ORG = (By.XPATH, "//label[contains(text(),'供电公司')]/../div/input")
    # 文件类型
    QRY_FILE_TYPE = (By.XPATH, "//label[contains(text(),'文件类型')]/../div/div//input")
    # 值（文件类型）
    QRY_FILE_TYPE_VALUE = (
    By.XPATH, "//div[@class='x-combo-list-inner']//div[contains(text(),'算法说明')]/../div[contains(text(),'%s')]")
    # 文件名称
    QRY_FILE_NAME = (By.XPATH, "//label[contains(text(),'文件名称')]/../div/input")
    # 开始日期
    QRY_START_DATE = (By.XPATH, "//label[contains(text(),'从')]/../div/div/input")
    # 结束日期
    QRY_END_DATE = (By.XPATH, "//label[contains(text(),'到')]/../div/div/input")

    # 【操作区】
    # 查询
    BTN_QUERY = (By.XPATH, "(//button[contains(text(),'查询')])[2]")

    # [显示区]
    TAB_ONE = (By.XPATH, "(//div[@class='x-grid3-scroller'])[1]")

    # 【js操作】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[6].removeAttribute("readonly");'
    END_DATE_JS = 'document.getElementsByTagName("input")[7].removeAttribute("readonly");'
