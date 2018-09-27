# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: ctrlExecut_locators.py
@time: 2018/9/27 0027 14:58
@desc:
'''
from selenium.webdriver.common.by import By

#基本应用--》费控管理--》低压用户远程费控执行
class CtrlExecutLocators:
    #【查询条件区】
    #用户编号
    QRY_USER_NO = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'用户编号')]/../../div[1]/div[1]/input")
    # 用户名称
    QRY_USER_NAME = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'用户名称')]/../../div[1]/div[1]/input")
    # 终端地址
    QRY_TMNL_ADDR = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'终端地址')]/../../div[1]/div[1]/input")
    # 抄表段编号
    QRY_SECT_NO = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'抄表段号')]/../../div[1]/div[1]/input")
    # 开始时间
    QRY_START_TIME = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'开始时间')]/../../div[1]/div[1]/div/input")
    # 结束时间
    QRY_END_TIME = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'结束时间')]/../../div[1]/div[1]/div/input")
    # 工单号
    QRY_WORRK_ORDER = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'工单号')]/../../div[1]/div[1]/input")

    #控制类型
    QRY_CONTROL_TYPE = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'控制类型')]/../../div[1]/div[1]/div/input")
    QRY_CONTROL_TYPE_VALUE = (By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'保电投入')]/../div[contains(text(),'%s')]")
    # 执行状态
    QRY_EXE_STATUS = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'执行状态')]/../../div[1]/div[1]/div/input")
    QRY_EXE_STATUS_VALUE = (By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'待下发命令')]/../div[contains(text(),'%s')]")
    # 数据来源
    QRY_DATA_COME = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'数据来源')]/../../div[1]/div[1]/div/input")
    QRY_DATA_COME_VALUE = (By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'营销系统')]/../div[contains(text(),'%s')]")
    # 确认状态
    QRY_CONFIRM_STATUS = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'确认状态')]/../../div[1]/div[1]/div/img")
    QRY_CONFIRM_STATUS_VALUE = ( By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'执行待确认')]/../div[contains(text(),'%s')]")
    # 执行结果状态
    QRY_EXE_STATUS_RESULT = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'执行结果状态')]/../../div[1]/div[1]/div/input")
    QRY_EXE_STATUS_RESULT_VALUE = (By.XPATH, "(//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'成功')])[2]/../div[contains(text(),'%s')]")


    # 【操作区】
    BTN_QRY = (By.XPATH,"(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    #【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = 'document.getElementById("startDateTime").removeAttribute("readonly");'
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementById("endDateTime").removeAttribute("readonly");'

    #【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")
     
     
     
     
     