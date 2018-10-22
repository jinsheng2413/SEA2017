# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: patrolDataQuery_locators.py
@time: 2018/10/18 11:19
@desc:
'''

from selenium.webdriver.common.by import By

# 统计查询→综合查询→巡检仪数据查询
class PatrolDataQueryLocators:
#基本档案
    #终端资产号
    TMNL_ASSET_NO = (By.XPATH,'//label[contains(text(),"终端资产号")]/../div/input')
    #终端地址
    TMNL_ADDR = (By.XPATH,'//label[contains(text(),"终端地址")]/../div/input')
    #用户编号
    CONS_NO = (By.XPATH,'//label[contains(text(),"用户编号")]/../div/input')
    #查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[4]')
#曲线数据
    #用户编号
    CURVE_DATA_CONS_NO = (By.XPATH,'(//label[contains(text(),"用户编号")]/../div/input)[2]')
    # 终端地址
    CURVE_DATA_TMNL_ADDR = (By.XPATH, '(//label[contains(text(),"终端地址")]/../div/input)[2]')
    #日期
    CURVE_DATA_DATE = (By.XPATH,'//label[contains(text(),"日期")]/../div/div/input')
    #曲线类型
    CURVE_DATA_CURVE_TYPE = (By.XPATH,'//label[contains(text(),"曲线类型")]/../div/div/img')
    # 曲线类型→值
    CURVE_DATA_CURVE_TYPE_VALUE = (By.XPATH,'//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_CURVE_DATA_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[5]')
#曲线对比
    # 终端资产号
    CURVE_CONTRAST_TMNL_ASSET_NO = (By.XPATH, '(//label[contains(text(),"终端资产号")]/../div/input)[2]')
    # 终端地址
    CURVE_CONTRAST_TMNL_ADDR = (By.XPATH, '(//label[contains(text(),"终端地址")]/../div/input)[2]')
    # 曲线类型
    CURVE_CONTRAST_CURVE_TYPE = (By.XPATH, '//label[contains(text(),"曲线类型")]/../div/div/img')
    # 曲线类型→值
    CURVE_CONTRAST_CURVE_TYPE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    #电表资产号
    CURVE_CONTRAST_METER_ASSET_NO = (By.XPATH,'//label[contains(text(),"电表资产号")]/../div/input')
    # 日期
    CURVE_CONTRAST_DATE = (By.XPATH, '//label[contains(text(),"日期")]/../div/div/input')
    # 查询按钮
    BTN_CONTRAST_DATA_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[5]')
#电流回路状态
    # 终端地址
    CURRENT_STATUS_TMNL_ADDR = (By.XPATH, '(//label[contains(text(),"终端地址")]/../div/input)[2]')
    #电流回路状态
    CURRENT_STATUS = (By.XPATH,'//label[contains(text(),"电流回路状态")]/../div/div/img')
    #电流回路状态→值
    CURRENT_STATUS_VALUE = (By.XPATH,'//div[@class="x-combo-list-inner"]/div[%s]')
    #日期
    CURRENT_STATUS_DATE = (By.XPATH,'//label[contains(text(),"日期")]/../div/div/input')
    # 终端资产号
    CURRENT_STATUS_TMNL_ASSET_NO = (By.XPATH, '(//label[contains(text(),"终端资产号")]/../div/input)[2]')
    #用户编号
    CURRENT_STATUS_CONS_NO = (By.XPATH,'(//label[contains(text(),"用户编号")]/../div/input)[2]')
    # 查询按钮
    BTN_CURRENT_STATUS_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[5]')
#异常事件查询
    # 终端地址
    ANOMALOUS_EVENT_TMNL_ADDR = (By.XPATH, '(//label[contains(text(),"终端地址")]/../div/input)[2]')
    # 终端资产号
    ANOMALOUS_EVENT_TMNL_ASSET_NO = (By.XPATH, '(//label[contains(text(),"终端资产号")]/../div/input)[2]')
    #用户编号
    ANOMALOUS_EVENT_CONS_NO = (By.XPATH,'(//label[contains(text(),"用户编号")]/../div/input)[2]')
    #异常事件
    ANOMALOUS_EVENT = (By.XPATH,'//label[contains(text(),"异常事件")]/../div/div/img')
    #异常事件→值
    ANOMALOUS_EVENT_VALUE = (By.XPATH,'//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询按钮
    BTN_ANOMALOUS_EVENT_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[5]')

#【JS属性】
    #曲线数据，日期，删除readonly属性
    CURVE_DATA_DATE_JS = 'document.getElementsByTagName("input")[9].removeAttribute("readonly");'
    #曲线对比，日期，删除readonly属性
    CURVE_CONTRAST_DATE_JS = 'document.getElementsByTagName("input")[9].removeAttribute("readonly");'
    #电流回路状态，日期，删除readonly属性
    CURRENT_STATUS_DATE_JS = 'document.getElementsByTagName("input")[14].removeAttribute("readonly");'