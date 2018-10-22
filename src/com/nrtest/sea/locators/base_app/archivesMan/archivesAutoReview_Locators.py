# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesAutoReview_Locators.py
@time: 2018/9/29 0029 10:54
@desc:
'''
from selenium.webdriver.common.by import By

# 基本应用--》档案管理--》电表批量导出（冀北）
class ArchivesAutoReviewLocators:
    #【查询条件区】
    #导入电表信息
    QRY_LEADINTO_METER_INFO = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'导入电表信息')]/../../div[1]/div[1]//input")
    QRY__LEADINTO_METER_INFO_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'条形码')]/../div[contains(text(),'%s')]")
    #日期
    QRY_DATE = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'日期')]/../../div[1]/div[1]//input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    #【js区】
    # 开始时间，删除readonly属性
    DATE_JS = "document.getElementsByTagName('input')[6].removeAttribute(\"readonly\");"

    #【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
     
     
     
     
     