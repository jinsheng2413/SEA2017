# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesChangeRecord_locators.py
@time: 2018/9/25 0025 16:41
@desc:
'''
from selenium.webdriver.common.by import By

from com.nrtest.common.base_page import Page


class ArchivesChangeRecordLocators:
    #【查询条件区】
    #设备类型
    QRY_DEVICE_TYPE = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'设备类型')]/../../div[1]/div[1]/div/img")
    QRY_DEVICE_TYPE_VALUE = (By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'电能表')]/../div[contains(text(),'%s')]")
    #变更类型div/
    QRY_CHANGE_TYPE = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'变更类型')]/../../div[1]/div[1]/div/img")
    QRY_CHANGE_TYPE_VALUE = (By.XPATH, "//div[@class=\"x-combo-list-inner\"]//*[contains(text(),'新增')]/../div[contains(text(),'%s')]")
    #
    QRY_START_TIME = (By.XPATH, "(//div[@class=\"x-form-item \"]//label[contains(text(),'开始日期')])[1]/../../div[1]/div[1]/div/input")
    #
    QRY_END_TIME = (By.XPATH, "//div[@class=\"x-form-item \"]//label[contains(text(),'结束日期')]/../../div[1]/div[1]/div/input")

    # 【操作区】
    BTN_QRY = (By.XPATH,"(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")
    #专变
    BTN_SPECIAL_CHANGE = (By.XPATH,'(//*[@name=\"changeRecord_consTypeRadio\"])[1]')
    #低压
    BTN_LOW = (By.XPATH,'(//*[@name=\"changeRecord_consTypeRadio\"])[2]')

    #【js区】
    # 开始时间，删除readonly属性
    START_DATE_JS = "document.getElementsByTagName('input')[8].removeAttribute(\"readonly\");"
    # 结束时间，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[9].removeAttribute("readonly");'
    JS = "document.getElementsByTagName('input')[0].removeAttribute(\"readOnly\")"
    #【显示区】
    TAB_ONE = (By.XPATH, '(//table[@class=\"x-grid3-row-table\"])[1]')
    TAB_ONE_VALUE = (By.XPATH, "//*[@class=\"x-grid3-row-table\"])[]//div[]")



     
     
     
     