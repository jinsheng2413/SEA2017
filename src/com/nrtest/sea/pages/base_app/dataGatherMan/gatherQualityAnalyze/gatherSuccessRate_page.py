# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: GatherSuccessRatePage.py
@time: 2018-09-17 14:15
@desc:
'''

from com.nrtest.sea.locators.base_app.dataGatherMan.gatherQualityAnalyze.gatherSuccessRate_locators import GatherSuccessRateLocators
from com.nrtest.common.base_page import Page

#基本应该→数据采集管理→采集质量分析→采集成功率
class GatherSuccessRatePage(Page):
#采集成功率→采集成功率
#页面元素
    # 查询日期开始
    def inputDt_start_date(self,content):
        self.exec_script(GatherSuccessRateLocators.STARTDATE_JS)
        self.input(content,*GatherSuccessRateLocators.START_DATE)
    #查询日期结束
    def inputDt_end_date(self,content):
        self.exec_script(GatherSuccessRateLocators.ENDDATE_JS)
        self.input(content,*GatherSuccessRateLocators.END_DATE)
    #查询按钮
    def btn_search(self):
        self.click(*GatherSuccessRateLocators.BTN_SEARCH)
    # 用户类型
    def inputCSel_cons_type(self,index):
        if index is 'c':
            self._find_element(*GatherSuccessRateLocators.CONS_TYPE)
        else:
            self.click(*GatherSuccessRateLocators.CONS_TYPE)
            locator = self.get_select_locator(GatherSuccessRateLocators.CONS_TYPE_VALUE,index)
            self.click(*locator)
            self.click(*GatherSuccessRateLocators.CONS_TYPE)

# 采集成功率→采集成功率统计
    # 采集成功率统计
    def btn_statistics(self):
        self.click(*GatherSuccessRateLocators.BTN_STATISTICS)
# 页面元素
    # 查询日期
    def inputDt_statistics_date(self,content):
        self.exec_script(GatherSuccessRateLocators.STATISTICS_DATE_JS)
        self.input(content,*GatherSuccessRateLocators.STATISTICS_DATE)
    #用户类型
    def inputCSel_statistics_cons_type(self,index):
        if index is 'c':
            self._find_element(*GatherSuccessRateLocators.STATISTICS_CONS_TYPE)
        else:
            self.click(*GatherSuccessRateLocators.STATISTICS_CONS_TYPE)
            locator = self.get_select_locator(GatherSuccessRateLocators.STATISTICS_CONS_TYPE_VALUE,index)
            self.click(*locator)
            self.click(*GatherSuccessRateLocators.STATISTICS_CONS_TYPE)
    #查询按钮
    def btn_statistics_search(self):
        self.click(*GatherSuccessRateLocators.BTN_STATISTICS_SEARCH)

#采集成功率→数据采集成功率明细
    # 采集成功率统计
    def btn_detail(self):
        self.click(*GatherSuccessRateLocators.BTN_DETAIL)
# 页面元素
    # 查询日期
    def inputDt_detail_date(self,content):
        self.exec_script(GatherSuccessRateLocators.DETAIL_DATE_JS)
        self.input(content,*GatherSuccessRateLocators.DETAIL_DATE)
    #用户类型
    def inputCSel_detail_cons_type(self,index):
        if index is 'c':
            self._find_element(*GatherSuccessRateLocators.DETAIL_CONS_TYPE)
        else:
            self.click(*GatherSuccessRateLocators.DETAIL_CONS_TYPE)
            locator = self.get_select_locator(GatherSuccessRateLocators.DETAIL_CONS_TYPE_VALUE, index)
            self.click(*locator)
            self.click(*GatherSuccessRateLocators.DETAIL_CONS_TYPE)
    #查询按钮
    def btn_detail_search(self):
        self.click(*GatherSuccessRateLocators.BTN_DETAIL_SEARCH)
    #未抄数
    def btn_detail_never(self):
        self.click(*GatherSuccessRateLocators.BTN_DETAIL_NEVER)

#采集成功率→连续抄表失败明细
    #连续抄表失败明细
    def btn_continuous_false(self):
        self.click(*GatherSuccessRateLocators.BTN_CONTINUOUS_FALSE)
#页面元素
    # 查询日期
    def inputDt_false_date(self,content):
        self.exec_script(GatherSuccessRateLocators.FALSE_DATE_JS)
        self.input(content,*GatherSuccessRateLocators.FALSE_DATE)
    #用户类型
    def inputCSel_false_cons_type(self,index):
        if index is 'c':
            self._find_element(*GatherSuccessRateLocators.FALSE_CONS_TYPE)
        else:
            self.click(*GatherSuccessRateLocators.FALSE_CONS_TYPE)
            locator = self.get_select_locator(GatherSuccessRateLocators.FALSE_CONS_TYPE_VALUE, index)
            self.click(*locator)
            self.click(*GatherSuccessRateLocators.FALSE_CONS_TYPE)
    #查询按钮
    def btn_false_search(self):
        self.click(*GatherSuccessRateLocators.BTN_FALSE_SEARCH)
    # 连续N天抄表失败明细
    def btn_false_detail(self):
        self.click(*GatherSuccessRateLocators.BTN_FALSE_DETAIL)

# 基本应用→数据采集管理→采集质量分析→采集成功率→按时间统计
    #查询日期，开始
    def inputDt_data_start_date(self,content):
        self.exec_script(GatherSuccessRateLocators.DATE_START_DATE_JS)
        self.input(content,*GatherSuccessRateLocators.DATE_START_DATE)
    #查询日期，结束
    def inputDt_data_end_date(self,content):
        self.exec_script(GatherSuccessRateLocators.DATE_END_DATE_JS)
        self.input(content,*GatherSuccessRateLocators.DATE_END_DATE)
    #用户类型
    def inputCSel_date_cons_type(self,index):
        if index is 'c':
            self._find_element(*GatherSuccessRateLocators.DATE_CONS_TYPE)
        else:
            self.click(*GatherSuccessRateLocators.DATE_CONS_TYPE)
            locator = self.get_select_locator(GatherSuccessRateLocators.DATE_CONS_TYPE_VALUE, index)
            self.click(*locator)
            self.click(*GatherSuccessRateLocators.DATE_CONS_TYPE)
    #查询按钮
    def btn_date_search(self):
        self.click(*GatherSuccessRateLocators.BTN_DATE_SEARCH)

#显示区
    #第一个单位
    def btn_first_unit(self):
        self.click(*GatherSuccessRateLocators.BTN_FIRST_UNIT)
    #第一个“更多”按钮
    def btn_first_more(self):
        self.click(*GatherSuccessRateLocators.BTN_FIRST_MORE)
    # 跳出窗口关闭按钮
    def btn_close(self):
        self.click(*GatherSuccessRateLocators.BTN_CLOSE)
    # 第一个结果的采集成功率
    def show_first_statistics(self):
        self.click(*GatherSuccessRateLocators.SHOW_FIRST_STATISTICS)