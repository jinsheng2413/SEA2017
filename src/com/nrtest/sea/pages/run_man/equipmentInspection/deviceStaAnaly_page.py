# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: deviceStaAnaly_page.py
@time: 2019/2/14 0014 15:37
@desc:
"""
# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: device_sta_analy_page.py
@time: 2019-02-14 15:38:09
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→设备巡检→设备巡检合格情况统计:设备巡检合格率统计
class DeviceStaAnaly_count_Page(Page):
    # 终端厂家
    def inputSel_tmnl_manufactory(self, option):
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 包含仪器
    def inputChk_instrument(self, option):
        self.clickRadioBox(option, is_multi_elements=True, is_multi_tab=True)

    # 参数指标项
    def inputSel_para_tpitmnl_nape(self, option):
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 结束日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 开始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 巡检类型
    def inputSel_polling_type(self, option):
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 日月
    def inputChk_day_month(self, option):
        self.clickRadioBox(option, is_multi_tab=True, is_multi_elements=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


from com.nrtest.common.base_page import Page


# 运行管理→设备巡检→设备巡检合格情况统计:设备巡检指标参数明细
class DeviceStaAnaly_detail_Page(Page):
    # 终端厂家
    def inputSel_tmnl_manufactory(self, option):
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 包含仪器
    def inputChk_instrument(self, option):
        self.clickRadioBox(option, is_multi_elements=True, is_multi_tab=True)

    # 参数指标项
    def inputSel_para_tpitmnl__nape(self, option):
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 结束日期
    def inputDt_end_date(self, value):
        self.inputDate(value)

    # 开始日期
    def inputDt_start_date(self, value):
        self.inputDate(value)

    # 巡检类型
    def inputSel_polling_type(self, option):
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 日月
    def inputChk_day_month(self, option):
        self.clickRadioBox(option, is_multi_tab=True, is_multi_elements=True)

    # 电表资产编号
    def inputStr_meter_asset_no(self, value):
        self.input(value)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)

    # 终端资产编号
    def inputStr_tmnl_asset_no(self, value):
        self.input(value)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
