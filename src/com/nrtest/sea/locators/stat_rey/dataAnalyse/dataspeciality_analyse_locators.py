# -*- coding:utf-8 -*-

'''
@author: 邵茜
@license: (C) Copyright 2018, Nari.
@file: dataspeciality_analyse_locators.py
@time: 2018/8/15 11:35
@desc:
'''
from selenium.webdriver.common.by import By
class DataSpecialityAnalyseLocators:

    #点击唐山供电公司
    SPREAD_ORG_NO = (By.XPATH,'//span[contains(text(),"国网冀北电力有限公司")]/../../img[1]')
    TANGSHAN_ORG_NO = (By.XPATH,'//span[contains(text(),"唐山供电公司")]')
    #选择公变
    SELECT_CONS_TYPE = (By.XPATH,'//label[contains(text(),"用户类型")]/../div/div/img')
    SELECT_PUBLIC = (By.XPATH,'//div[@class="x-combo-list-inner"]//div[contains(text(),"公变")]')
    #时间
    TIME = (By.XPATH, '//label[contains(text(),"日期")]/../div[1]/div/img')
    TIME_YEAR1 = (By.XPATH,'//button[contains(text(),"八月 2018")]')
    TIME_YEAR2 = (By.XPATH, '//div[@class="x-date-picker x-unselectable"]/div/table/tbody/tr[6]/td[3]/a')
    # 开始时间-1月
    TIME_MOUTH = (By.XPATH, '//div[@class="x-date-picker x-unselectable"]/div/table/tbody/tr[2]/td[2]/a')
    # 开始时间-确定
    TIME_CONFIRM = (By.XPATH, '//button[@class=\"x-date-mp-ok\"]')
    # 开始时间-13号
    TIME_DAY = (By.XPATH,"//table[@class=\"x-date-inner\"]/tbody/tr[3]//*[contains(text(),'13')]")
    #查询
    BTN_SEARCH = (By.XPATH, '(//tbody[@class="x-btn-small x-btn-icon-small-left"]/tr[2]/td[2]/em/button[contains(text(),"查询")])[4]')
    # 【显示区】
    TAB_ONE = (By.XPATH,'(//div[@class="x-grid3-scroller"])[1]/div')
