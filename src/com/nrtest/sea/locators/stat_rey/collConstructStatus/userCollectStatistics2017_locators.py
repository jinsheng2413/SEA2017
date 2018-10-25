# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: userCollectStatistics2017_locators.py
@time: 2018/10/24 14:51
@desc:
'''

from selenium.webdriver.common.by import By

#统计查询→综合查询→采集建设情况→采集覆盖情况→用户采集覆盖率统计2017
class UserCollectStatistics2017Locators:
#页面元素
    #用户类型
    CONS_TYPE = (By.XPATH,'//label[contains(text(),"用户类型")]/../div/div/input')
    #用户类型→值
    CONS_TYPE_VALUE = (By.XPATH,'//div[@class="x-combo-list-inner"]/div[%s]')
    #统计月份
    DATE = (By.XPATH,'//label[contains(text(),"统计月份")]/../div/div/input')
    #统计口径
    STATISTICS_CALIBER = (By.XPATH,'//label[contains(text(),"统计口径")]/../div/div/input')
    #统计口径→值
    STATISTICS_CALIBER_VALUE = (By.XPATH,'(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    #查询按钮
    BTN_SEARCH = (By.XPATH,'//button[text()="查询"]')

#【JS操作】
    #统计月份，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[6].removeAttribute("readonly");'

#【校验区】
    #第一行数据
    CHECK_FIRST = (By.XPATH,'//div[@class="x-grid3-row  x-grid3-row-first x-grid3-row-selected"]')