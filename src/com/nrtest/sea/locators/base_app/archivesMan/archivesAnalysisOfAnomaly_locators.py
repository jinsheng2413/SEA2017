# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesAnalysisOfAnomaly_locators.py
@time: 2018/8/29 0029 15:56
@desc:
"""
from selenium.webdriver.common.by import By


class ArchivesAnalysisOfAnomaly_count_locators:
    # 【菜单】
    # 档案异常明细
    BTN_MENU_ARCHIVES_ABNOLMAL_DETAIL = (By.XPATH, "(//*[contains(text(),'档案异常明细')])[@class=\"x-tab-strip-text \"]")
    # 档案异常统计
    BTN_MENU_ARCHIVES_ABNOLMAL_COUNT = (By.XPATH, "(//*[contains(text(),'档案异常统计')])[@class=\"x-tab-strip-text \"]")
    # 【查询条件】
    # 用户类型
    QRY_USER_CATA = (By.XPATH,
                     "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//label[contains(text(),'用户类型')]/../div/div/img)[1]")
    QRY_USER_CATA_VALUE = (By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'全部')]/../div[%s]")
    # 日期
    QRY_DATE = (By.XPATH,
                "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//label[contains(text(),'日期')])[1]/../div[1]/div/input")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//*[@class=\"x-grid3-row-table\"])[1]')
    # 用户档案异常数
    TAB_ONE_USER_ARCHIVES_ANOMALS_NUM = (By.XPATH, '(//*[@class=\"x-grid3-row-table\"])[1]/tbody/tr/td[3]/div/a')
    # 电表档案异常数
    TAB_ONE_METER_ARCHIVES_ANOMALS_NUM = (By.XPATH, '(//*[@class=\"x-grid3-row-table\"])[1]/tbody/tr/td[4]/div/a')
    # 终端档案异常数
    TAB_ONE_TERMIANAL_ARCHIVES_ANOMALS_NUM = (By.XPATH, '(//*[@class=\"x-grid3-row-table\"])[1]/tbody/tr/td[5]/div/a')


class ArchivesAnalysisOfAnomaly_detail_locators:
    # 【菜单】
    BTN_MENU_ARCHIVES_ABNOLMAL_AL = (By.XPATH, "(//*[contains(text(),'档案异常分析')])[@class=\"x-tab-strip-text icorun\"]")
    BTN_LOS = (By.XPATH, "//*[contains(text(),'异常信息明细')]/../div[1]")
    BTN_USER_DATA_QRY = (By.XPATH, "//*[contains(text(),'用户数据查询')]")
    BTN_CONFIRM = (By.XPATH, "(//*[contains(text(),'确定')])[@class=\" x-btn-text\"]")
    # 档案异常明细
    BTN_MENU_ARCHIVES_ABNOLMAL_DETAIL = (By.XPATH, "(//*[contains(text(),'档案异常明细')])[@class=\"x-tab-strip-text \"]")
    # 档案异常统计
    BTN_MENU_ARCHIVES_ABNOLMAL_COUNT = (By.XPATH, "(//*[contains(text(),'档案异常统计')])[@class=\"x-tab-strip-text \"]")
    # 【查询条件】
    # 档案类型
    QRY_ARCHIVES_CATA = (By.XPATH,
                         "//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//label[contains(text(),'档案类型')]/../div/div/img")
    QRY_ARCHIVES_CATA_VALUE = (
        By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'用户档案')]/../div[%s]")

    # 用户类型
    QRY_USER_CATA = (By.XPATH,
                     "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//label[contains(text(),'用户类型')]/../div/div/img)[2]")
    QRY_USER_CATA_VALUE = (By.XPATH, "//div[@class=\"x-combo-list-inner\"]//div[contains(text(),'全部')]/../div[%s]")
    # 日期
    QRY_DATE = (By.XPATH, "//*[@id=\"statDateDetail\"]")

    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-panel-body x-panel-body-noheader x-panel-body-noborder\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[2]")

    # 【显示区】
    TAB_ONE = (By.XPATH, '(//*[@class=\"x-grid3-row-table\"])[1]')
    # 用户编号
    TAB_ONE_USER_NO_DETAIL = (By.XPATH, '(//*[@class=\"x-grid3-row-table\"])[1]/tbody/tr/td[4]/div/a')
    # 终端资产号
    TAB_ONE_TERMINAL_ASSET_NO_DETAIL = (By.XPATH, '(//*[@class=\"x-grid3-row-table\"])[1]/tbody/tr/td[7]/div/a')
    # 异常明细
    TAB_ABNOLMAI_DETAIL = (By.XPATH, '(//*[@class=\"x-grid3-row-table\"])[1]/tbody/tr/td[13]/div/a')
