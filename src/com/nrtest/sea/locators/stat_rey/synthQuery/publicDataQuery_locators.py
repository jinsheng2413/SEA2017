# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: PublicDataQueryLocators.py
@time: 2018-08-15 11:00
@desc:
'''

from selenium.webdriver.common.by import By


# 统计查询→综合查询→配变数据查询
class PublicDataQueryLocators:
    # 页面元素
    # 配变用户
    QRY_PUBLICCONSNO = (By.XPATH, '//input[@class=" x-form-text x-form-field  x-form-empty-field"]')
    # 配变表号
    QRY_PUBLICNUM = (By.XPATH, '//input[@id="assetNoForQuery"]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//div[@class="x-column-inner"]//button[contains(text(),"查询")]')
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
    # 电网_狮子湾农改
    TREE_SHIZIWAN = (By.XPATH, '//span[contains(text(),"狮子湾农改")]')
    # 数据展示
    # 电压曲线
    # 下拉菜单
    INPUTSEL_VOLTAGECURVE_GROUP = (
        By.XPATH, '//input[@class=" x-form-text x-form-field x-trigger-noedit  x-form-focus"]')
    # 查询日期
    INPUTDT_VOLTAGECURVE_TIME = (By.XPATH, 'class=" x-form-text x-form-field x-trigger-noedit x-form-focus"')
    # 查询按钮
    BTN_VOLTAGECURVE_SEARCH = (By.XPATH, '(//table[@class="x-toolbar-right-ct"]//button[contains(text(),"查询")])[1]')
    # 电流曲线
    BTN_CURRENTCURVE = (By.XPATH, '//span[contains(text(),"电流曲线")]')
    # 下拉菜单
    INPUTSEL_CURRENTCURVE_GROUP = (
        By.XPATH, '//input[@class=" x-form-text x-form-field x-trigger-noedit  x-form-focus"]')
    # 查询日期
    INPUTDT_CURRENTCURVE_TIME = (By.XPATH, '//input[@class=" x-form-text x-form-field x-trigger-noedit x-form-focus"]')
    # 查询按钮
    BTN_CURRENTCURVE_SEARCH = (By.XPATH, '(//table[@class="x-toolbar-right-ct"]//button[contains(text(),"查询")])[2]')
    # 功率曲线
    BTN_POWERCURVE = (By.XPATH, '//span[contains(text(),"功率曲线")]')
    # 下拉菜单
    INPUTSEL_POWERCURVE_GROUP = (
        By.XPATH, '//div[@class="x-form-field-wrap x-form-field-trigger-wrap  x-trigger-wrap-focus"]/input[2]')
    # 查询日期
    INPUTDT_POWERCURVE_TIME = (By.XPATH, '//input[@class=" x-form-text x-form-field x-trigger-noedit x-form-focus"]')
    # 查询按钮
    BTN_POWERCURVE_SEARCH = (By.XPATH, '(//table[@class="x-toolbar-right-ct"]//button[contains(text(),"查询")])[3]')
    # 功率因数曲线
    BTN_POWERFACTORCURVE = (By.XPATH, '//span[contains(text(),"功率因数曲线")]')
    # 查询日期
    INPUTDT_POWERFACTORCURVE_TIME = (
        By.XPATH, '//input[@class=" x-form-text x-form-field x-trigger-noedit x-form-focus"]')
    # 查询按钮
    BTN_POWERFACTORCURVE_SEARCH = (By.XPATH, '(//table[@class="x-toolbar-right-ct"]//button[contains(text(),"查询")])[4]')
