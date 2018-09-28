# -*- coding:utf-8 -*-

'''
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: availableCapacityAnalyse_locators.py
@time: 2018/9/27 14:47
@desc:
'''

from selenium.webdriver.common.by import By

# 高级应用--》配变负载分析--》包装可用容量分析
class AvailableCapacityAnalyseLocators:
    #【查询条件】
    # 供电单位
    ORG_NO = (By.XPATH,"//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input")
    # 查询日期
    QUERY_DATE = (By.XPATH, "//div[@class=\"x-form-item \"]//*[contains(text(),'月份')]/../div/div/input")
    # 负载率
    LOAD_RATE = (By.XPATH,"//div[@class=\"x-form-item \"]//*[contains(text(),'负载率')]/../div/input")

    #【按钮】
    # 查询
    BTN_QUERY = (By.XPATH, "(//button[contains(text(),'查询')])[2]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementsByTagName("input")[5].removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (By.XPATH,"(//div[@class=\"x-grid3-scroller\"])[1]/div/div")