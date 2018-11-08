# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: lineTopologyDiagram_locators.py
@time: 2018/10/8 14:09
@desc:
"""

from selenium.webdriver.common.by import By


# 统计查询→综合查询→线路拓扑图
class LineTopologyDiagramLocators:
    # 线路名称
    LINE_NAME = (By.XPATH, '//label[contains(text(),"线路名称")]/../div/div/img')
    # 线路名称→值
    LINE_NAME_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[contains(text(),"查询")]')
