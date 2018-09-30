# -*- coding:utf-8 -*-

'''
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: loadRateStatic_locators.py
@time: 2018/9/24 20:42
@desc:
'''

from selenium.webdriver.common.by import By

# 高级应用--》配变监测分析--》功率因数越限统计
#功率因数越限统计
class PowerFactorCountStaticLocators:
    #【查询条件】
    # 供电单位
    ORG_NO = (By.XPATH,("(//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input)[1]"))
    # 用户类型-下拉框
    CONS_TYPE_SEL = (By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'用户类型')]/../div/div/img)[1]")
    # 用户类型
    CONS_TYPE = (By.XPATH, '//div[@class=\"x-combo-list-inner\"]//div[contains(text(),"%s")]')
    # 查询日期
    QUERY_DATE = (By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'日期')])[1]/../div/div/input")

    #【按钮】
    # 查询
    BTN_QUERY = (By.XPATH, "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[1]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementsByTagName("input")[6].removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[1]/div/div)[1]")

