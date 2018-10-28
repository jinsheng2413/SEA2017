# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: terminalDataQueryLocators.py
@time: 2018/8/10 0002 09:30
'''

from selenium.webdriver.common.by import By


# 统计查询→综合查询→终端数据查询
class TerminalDataQueryLocators:
    # 页面元素
    # 终端资产号
    QRY_TERMINALNUM = (By.XPATH, '//input[@id="nari.synthQuery.tmnlAssetNo"]')
    # 终端地址
    QRY_TERMINALADDRESS = (By.XPATH, '//input[@id="nari.synthQuery.terminalAddr"]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//table[@id="tmnlDataQueryBtn"]//button')
    # 基本档案
    BTN_BASICFILE = (By.XPATH, '//span[contains(text(),"基本档案")]')
    # 数据展示
    BTN_DATASHOW = (By.XPATH, '//span[contains(text(),"数据展示")]')
    # 操作对象选择区
    # 国网冀北电力有限公司
    TREE_JIBEI = (By.XPATH, '//img[@class="x-tree-ec-icon x-tree-elbow-end-plus"]')
    # 唐山供电公司
    TREE_TANGSHAN = (By.XPATH, '//span[contains(text(),"唐山供电公司")]/../../img[@class="x-tree-ec-icon x-tree-elbow-plus"]')
    # 直属用户
    TREE_DIRECTLYUSER = (By.XPATH, '(//ul[@class="x-tree-node-ct"])[2]/li[1]/div/img[1]')
    # 电网_国各庄
    TREE_GUOGEZHUANG = (By.XPATH, '//span[contains(text(),"电网_国各庄")]')
    # 数据展示→电量
    # 电量
    BTN_ELECTRICQUANTITY = (By.XPATH, '(//span[contains(text(),"电量")])[1]')
    # 总加组
    SEL_ELECTRICQUANTITY_SUMGROUP = (By.XPATH, '//input[@id="elecQuant_addGroupCombox"]')
    # 查询日期_开始
    QRY_ELECTRICQUANTITY_STARTTIME = (By.XPATH, '(//div[contains(text(),"查询日期")]/../../td[5]/div/input)[1]')
    # 查询日期_结束
    QRY_ELECTRICQUANTITY_ENDTIME = (By.XPATH, '//div[contains(text(),"查询日期")]/../../td[8]/div/input')
    # 查询按钮
    BTN_ELECTRICQUANTITY_SEARCH = (By.XPATH, '(//tr[@class="x-toolbar-right-row"]//button[@class=" x-btn-text"])[1]')
    # 数据展示→功率
    # 功率
    BTN_POWER = (By.XPATH, '(//span[contains(text(),"功率")])[1]')
    # 总加组
    SEL_POWER_SUMGROUP = (By.XPATH, '//input[@id="power_addGroupCombox"]')
    # 查询日期
    QRY_POWER_TIME = (By.XPATH, '(//div[contains(text(),"查询日期")]/../../td[5]/div/input)[2]')
    # 查询按钮
    BTN_POWER_SEARCH = (By.XPATH, '(//tr[@class="x-toolbar-right-row"]//button[@class=" x-btn-text"])[2]')
