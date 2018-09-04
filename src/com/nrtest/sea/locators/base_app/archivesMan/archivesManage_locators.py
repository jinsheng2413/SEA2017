# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesManage_locators.py
@time: 2018/8/29 0029 13:51
@desc:
'''
from selenium.webdriver.common.by import By
class ArchivesManage_locators:


    #【流程】
    BTN_LG_D = (By.XPATH,"(//span[contains(text(),'开平新苑路营业站')])[1]")
    BTN_LG = (By.XPATH,"(//span[contains(text(),'直属用户')])[1]")
    BTN_MENU = (By.XPATH,"(//*[contains(text(),'档案同步')])[@class=\"x-tab-strip-text icorun\"]")
    BTN_CONFIRM = (By.XPATH,"//*[contains(text(),'确定')]")
    BTN_MENU_ABNOLMAL_DETAIL= (By.XPATH,"(//*[contains(text(),'档案异常明细')])[@class=\"x-tab-strip-text \"]")
    #【查询条件】
    #用户类型
    QRY_USER_CATA = (By.XPATH,"//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//label[contains(text(),'用户类型')]/../div/div/img")
    QRY_USER_CATA_VALUE = (By.XPATH,"//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'全部')]/../div[%s]")
    #户号
    QRY_FAMILY_NO = (By.XPATH,"//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//label[contains(text(),'户号')]/../div/input")
    #终端资产号
    QRY_TERMINAL_ASSET_NO = (By.XPATH,"//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//label[contains(text(),'终端资产号')]/../div/input")
    # 终端地址
    QRY_TERMINAL_ADDR = (By.XPATH,"//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//label[contains(text(),'终端地址')]/../div/input")

    # 【操作区】
    BTN_QRY = (By.XPATH,"(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//div[@class=\"x-grid3-row-checker\"])[1]')
    #用户编号明细
    TAB_ONE_USER_CATA_DETAIL = (By.XPATH,'(//*[@class=\"x-grid3-row-checker\"])[1]/../../../td[3]/div/a')
    #终端资产号明细
    TAB_ONE_TERMINAL_ASSET_NO_DETAIL = (By.XPATH,'(//*[@class=\"x-grid3-row-checker\"])[1]/../../../td[6]/div/a')

    TAB_USER_ASSERT = (By.XPATH,"//*[contains(text(),'用户数据查询')]")


