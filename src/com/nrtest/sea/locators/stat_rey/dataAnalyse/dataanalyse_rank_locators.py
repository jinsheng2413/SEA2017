# -*- coding:utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: dataanalyse_rank_locators.py
@time: 2018/8/8 9:23
@desc:
"""
from selenium.webdriver.common.by import By


class DataAnalyseRankLocators:
    # 国网冀北电力有限公司
    ORG_NO = (By.XPATH, '//span[@unselectable="on"]')
    # 开始时间
    START_TIME = (By.XPATH, '//label[contains(text(),"开始日期")]/../div[1]/div/img')
    # 开始时间-2014年
    START_TIME_YEAR1 = (By.XPATH, '//button[contains(text(),"八月 2018")]')
    START_TIME_YEAR2 = (By.XPATH, '//td[@class="x-date-mp-year"]/a[contains(text(),"2014")]')
    # 开始时间-1月
    START_TIME_MOUTH = (By.XPATH, '(//div[@class="x-date-mp"]//a[contains(text(),"一月")])[1]')
    # 开始时间-确定
    START_TIME_CONFIRM = (By.XPATH, '//button[@class=\"x-date-mp-ok\"]')
    # 开始时间-1号
    START_TIME_DAY = (By.XPATH, '//td[@class="x-date-active x-date-selected"]')
    # 查询
    BTN_SEARCH = (
        By.XPATH,
        '(//tbody[@class="x-btn-small x-btn-icon-small-left"]/tr[2]/td[2]/em/button[contains(text(),"查询")])[4]')
    # 点击户号
    BTN_CONS_NO = (By.XPATH, '//a[contains(text(),"1184272782")]')
    # 排名数量
    RANK_NUM = (By.XPATH, '//*[@id="lsaSortNum"]')
    # 用户类型-下拉框
    DROP_DOWN = (By.XPATH, '//label[contains(text(),"用户类型")]/../div/div/img')
    # 用户类型--专变
    CONS_TYPE_SPECIAL = (By.XPATH, '//div[@class="x-combo-list-inner"]//div[contains(text(),"专变")]/../div[%s]')
    # 用户类型--公变
    CONS_TYPE_PUBLIC = (By.XPATH, '//div[@class="x-combo-list-inner"]//div[contains(text(),"公变")]')
    # 【显示区】
    TAB_ONE = (By.XPATH, "(//div[@class=\"x-grid3-scroller\"])[1]/div/div")
