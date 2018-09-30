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
#功率因数越限明细
class PowerFactorCountDetailLocators:
    #【查询条件】
    # 供电单位
    ORG_NO = (By.XPATH,("(//div[@class=\"x-form-item \"]//*[contains(text(),'供电单位')]/../div/input)[2]"))
    # 用户类型-下拉框
    CONS_TYPE_SEL = (By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'用户类型')]/../div/div/img)[2]")
    # 用户类型
    CONS_TYPE = (By.XPATH, '(//div[@class =\"x-combo-list-inner\"])[1]//*[contains(text(),"%s")]')
    # 无功补偿情况-下拉框
    POWER_QUALITY_TYPE_SEL = (By.XPATH, "(//div[@ class =\"x-form-item \"]//*[contains(text(),'无功补偿情况')]/../div/div/img)[1]")
    # 无功补偿情况
    POWER_QUALITY_TYPE = (By.XPATH, '(//div[@class =\"x-combo-list-inner\"])[2]//*[contains(text(),"%s")]')
    # 查询日期
    QUERY_DATE = (By.XPATH, "(//div[@class=\"x-form-item \"]//*[contains(text(),'日期')])[2]/../div/div/input")

    #【按钮】
    # 查询
    BTN_QUERY = (By.XPATH, "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//button[contains(text(),'查询')])[2]")

    # 【js操作】
    # 查询日期，删除readonly属性
    QUERY_DATE_JS = 'document.getElementById("pfcdDate").removeAttribute("readonly");'

    # 【显示区】
    TABLE_DATA = (By.XPATH, "((//div[@class=\"x-grid3-scroller\"])[2]/div/div)[1]")