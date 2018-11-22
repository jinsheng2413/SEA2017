# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: scriptCheckTaskSet_locators.py
@time: 2018/11/19 0019 14:58
@desc:
"""
from selenium.webdriver.common.by import By

# 系统管理--》档案核查管理--》脚本核查任务编制
class ScriptCheckTaskSetLocators:
    #【查询条件区】
    #
    QRY_ = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'')]/../../div[1]/div[1]//input")
    #脚本类型
    QRY_SCRIPT_TYPE = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'脚本类型')]/../../div[1]/div[1]//input")
    QRY_SCRIPT_TYPE_VALUE = (
    By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'计量关键业务数据核查')]/../..//div[contains(text(),'%s')]")
    #脚本名称
    QRY_SCRIPT_NAME = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'脚本名称')]/../../div[1]/div[1]//input")
    #创建员工
    QRY_CREAT_STALL = (By.XPATH, "//*[@name=\"createUserTextField\"]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")
    # 任务状态
    QRY_TASK_STATUS = (
    By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'任务状态')]/../../div[1]/div[1]//input")
    QRY_TASK_STATUS_VALUE = (
        By.XPATH,
        "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'启用')]/../..//div[contains(text(),'%s')]")

    # 【js区】
    # 开始时间，删除readonly属性
    SCRIPT_TYPE_JS = 'document.getElementsByTagName(\'input\')[4].removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    TASK_STATUS_JS = 'document.getElementsByTagName(\'input\')[7].removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"

    #【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
     
     
     
     
     