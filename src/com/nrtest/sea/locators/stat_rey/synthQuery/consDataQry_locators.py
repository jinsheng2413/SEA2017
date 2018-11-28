# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: consDataQry_locators.py
@time: 2018/11/28 0028 10:16
@desc:
"""
from selenium.webdriver.common.by import By


# 统计查询→综合查询→用户数据
class ConsDataQryLocators:
    #【查询条件区】
    #用户编号
    QRY_USER_NO = (By.XPATH, "//*[@name=\"consDataQry.seaNodeField\"]")


    # 【操作区】
    BTN_QRY = (By.XPATH,
               "(//div[@class=\"x-column-inner\"]//tbody[@class=\"x-btn-small x-btn-icon-small-left\"]//button[contains(text(),'查询')])[1]")


     
     
     
     
     