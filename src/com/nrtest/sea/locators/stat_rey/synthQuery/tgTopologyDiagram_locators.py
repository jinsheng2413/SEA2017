# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgTopologyDiagram_locators.py
@time: 2018/10/9 9:36
@desc:
'''

from selenium.webdriver.common.by import By

# 统计查询→综合查询→台区拓扑图
class TgTopologyDiagramLocators:
    #专公变类型
    TMNL_TYPE = (By.XPATH,'//label[contains(text(),"专公变类型")]/../div/div/img')
    #专公变类型→值
    TMNL_TYPE_VALUE = (By.XPATH,'//div[@class="x-combo-list-inner"]/div[%s]')
    #台区编码
    TG_NO = (By.XPATH,'//label[contains(text(),"台区编码")]/../div/input')
    #台区名称
    TG_NAME = (By.XPATH,'//label[contains(text(),"台区名称")]/../div/input')
    #查询按钮
    BTN_SEARCH = (By.XPATH,'//button[contains(text(),"查询")]')