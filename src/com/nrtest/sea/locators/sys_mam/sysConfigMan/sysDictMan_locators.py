# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: sysConfigMan_locators.py
@time: 2018/9/13 10:15
@desc:
"""

from selenium.webdriver.common.by import By


# 系统管理--》系统配置管理--》数据字典管理
class SysDictManLocators:
    # 【查询条件】
    # 分类名称
    CATALOG_NAME = (By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'分类名称')]/../div/input")
    # 生效日期
    START_DATE = (By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'生效日期')]/../div/div/input")
    # 失效日期
    END_DATE = (By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'失效日期')]/../div/div/input")
    # 维护类型-下拉框
    EDIT_TYPE_SEL = (By.XPATH, '//div[@class=\"x-form-item \"]//*[contains(text(),"维护类型")]/../div/div/img')
    # 维护类型
    EDIT_TYPE = (By.XPATH, '(//div[@class =\"x-layer x-combo-list  x-resizable-pinned\"])[1]//*[contains(text(),"%s")]')
    # 维护人员
    EDITOR = (By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'维护人员')]/../div/input")
    # 数据来源-下拉框
    DATA_SOURCE_SEL = (By.XPATH, '//div[@class=\"x-form-item \"]//*[contains(text(),"数据来源")]/../div/div/img')
    # 数据来源
    DATA_SOURCE = (
        By.XPATH, '(//div[@class =\"x-layer x-combo-list  x-resizable-pinned\"])[2]//*[contains(text(),"%s")]')

    # 【按钮】
    # 查询
    BTN_QUERY = (By.XPATH, "//button[contains(text(),'查询')]")

    # 【js操作】
    # 生效日期，删除readonly属性
    START_DATE_JS = 'document.getElementById("sysDictMan.startDate").removeAttribute("readonly");'
    # 失效日期，删除readonly属性
    END_DATE_JS = 'document.getElementById("sysDictMan.endDate").removeAttribute("readonly");'

    # 【显示区】
    TAB_ONE = (By.XPATH, "(//div[@class=\"x-grid3-scroller\"])[1]/div/div")
