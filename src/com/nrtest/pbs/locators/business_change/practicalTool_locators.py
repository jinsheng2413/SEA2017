# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: practicalTool_locators.py
@time: 2019-07-08 13:48
@desc:
"""

from selenium.webdriver.common.by import By

# 业务变更→实用工具
class PracticalToolLocators:
    # 统计相关电量配置
    Practical_Tool_Stat = (By.ID,'tree_7_span')
    # 松原地区
    Tree_Song_Yuan = (By.ID,'treeDemo_6_span')
    # 计算公式手动查询
    Practical_Tool_Query = (By.ID,'tree_12_span')