# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesQuery_locators.py
@time: 2018/8/31 0031 9:28
@desc:
"""
from selenium.webdriver.common.by import By


class ArchivesQuery_locators:
    # 【菜单】
    BTN_CONFIRM = (By.XPATH, "//*[contains(text(),'确定')]")
    BTN_ARCHIVES_QUERY = (By.XPATH, "(//*[contains(text(),'档案查询')])[1]")
    # 【查询条件】
    # 用户类型
    QRY_CONS_TYPE_CLEAR = (By.XPATH,
                           "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//label[contains(text(),'用户类型')]/../div/div/input)[1]")
    QRY_CONS_TYPE = (By.XPATH,
                     "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//label[contains(text(),'用户类型')]/../div/div/img)[1]")
    QRY_CONS_TYPE_VALUE = (By.XPATH, "//div[@class=\"x-layer x-combo-list \"]/div/div[%s]/div/img")

    # 抄表段号
    QRY_SECT_NO = (By.XPATH, '//*[@id="mrSectNo"]')

    # 终端地址
    QRY_TMNL_ADDR = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端地址')]/../div[1]/input")

    # 【操作区】
    BTN_QRY = (By.XPATH, "//button[contains(text(),'查询')]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//*[@class=\"x-grid3-scroller\"])[1]/div/div[1]')
    # 用户编号
    TAB_ONE_CONS_NO = (By.XPATH, '(//*[@class=\"x-grid3-scroller\"])[1]/div/div[1]/table/tbody/tr/td[2]/div/a')
    # 终端地址
    TAB_ONE_TMNL_ADDR = (By.XPATH, '(//*[@class=\"x-grid3-scroller\"])[1]/div/div[1]/table/tbody/tr/td[7]/div/a')
    # 【js操作区】
    js = "document.getElementById('consTypeCombox').removeAttribute(\"readOnly\")"
