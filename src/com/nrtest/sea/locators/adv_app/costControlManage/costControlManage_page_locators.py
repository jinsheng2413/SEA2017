# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: costControlManage_page_locators.py
@time: 2018/8/2 0002 18:54
@desc:
'''
from selenium.webdriver.common.by import By


class CostControlManagePageLocators:
    # 【查询条件】
    # 营销单号
    QRY_MARKETINF_SINGLE_NUM = (By.XPATH, "//div[@class=\"x-form-item \"]/label[contains(text(),'营销单号')]/../div/input")
    # 终端地址
    QRY_TERMIAL_ADDR = (By.XPATH,
                        "//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//label[contains(text(),'终端地址')]/../div/input")
    # 按
    SELR_ARRANGE = (By.XPATH, "//label[contains(text(),'按')]/../div[1]/div/img")
    SELR_ARRANGE_VALUE = (By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'购电日期')]/../div[%s]")

    # 开始时间
    DATE_START = (By.XPATH, '//*[@id="buyStartDate"]')
    # 结束时间
    DATE_END = (By.XPATH, '//*[@id="buyEndDate"]')
    # 用户编号
    QRY_USER_NUM = (By.XPATH,
                    "//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//label[contains(text(),'用户编号')]/../div/input")
    # 用户名称
    QRY_USER_NAME = (By.XPATH,
                     "//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//label[contains(text(),'用户名称')]/../div/input")
    # 业务类型
    SEL_BUNIESS_CATA = (By.XPATH,
                        "//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//label[contains(text(),'业务类型')]/../div/div/input")
    SEL_BUNIESS_CATA_VALUE = (By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'缴费退补')]/../div[%s]")
    # 参数下发状态
    SEL_PARA_DEVE = (By.XPATH, '//*[@id="data_sendStatus"]')
    SEL_PARA_DEVE_VALUE = (By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'失败')]/../div[%s]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//div[@class=\"x-grid3-row-checker\"])[1]')

    # 【左边树】
    LEFT_ADD = (By.XPATH, '//div[@class=\"x-tree-root-node\"]/li/div/img[1]')
    # 唐山供电公司
    T_COMPANY = (By.XPATH, '(//a[@class=\"x-tree-node-anchor\"])[2]')

    # 【js操作】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("buyStartDate").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("buyEndDate").removeAttribute("readonly");'
