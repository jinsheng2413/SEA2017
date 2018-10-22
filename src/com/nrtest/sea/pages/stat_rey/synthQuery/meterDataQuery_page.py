# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: meterDataQuery_page.py
@time: 2018/10/9 16:45
@desc:
'''

from com.nrtest.sea.locators.stat_rey.synthQuery.meterDataQuery_locators import MeterDataQueryLocators
from com.nrtest.common.base_page import Page

# 统计查询→综合查询→抄表数据查询
class MeterDataQueryPage(Page):
    #抄表段号
    def inputStr_sect_no(self,content):
        self.input(content,*MeterDataQueryLocators.SECT_NO)
    #电表资产号
    def inputStr_meter_asset_no(self,content):
        self.input(content,*MeterDataQueryLocators.METER_ASSET_NO)
    #用户类型
    def inputSel_cons_type(self,index):
        self.click(*MeterDataQueryLocators.CONS_TYPE)
        locator = self.get_select_locator(MeterDataQueryLocators.CONS_TYPE_VALUE,index)
        self.click(locator)
    # 查询日期
    def inputDt_date(self,content):
        self.exec_script(MeterDataQueryLocators.DATE_JS)
        self.input(content,*MeterDataQueryLocators.DATE)
    #查询按钮
    def btn_search(self):
        self.click(*MeterDataQueryLocators.BTN_SEARCH)