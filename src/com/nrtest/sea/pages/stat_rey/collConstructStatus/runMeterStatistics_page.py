# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: runMeterStatistics_page.py
@time: 2018/10/25 15:08
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→采集建设情况→运行电能表统计
class RunMeterStatisticsPage(Page):
    # 区域类型
    def inputChk_area_type(self, index):
        self.clickSingleCheckBox(index)

    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectCheckBox(index)

    # 统计日期
    def inputDt_query_date(self, content):
        self.inputDate(content)

    # 查询按钮
    def btn_qry(self):
        self.btn_query()


# 运行电能表明细
class RunMeterDetailPage(Page):
    # 用户类型
    def inputSel_cons_type(self, index):
        self.selectCheckBox(index, is_multi_elements=True, is_multi_tab=True)

    # 通信方式
    def inputSel_comm_mode(self, index):
        self.selectCheckBox(index)

    # 通讯规约
    def inputSel_tmnl_protocol(self, index):
        self.selectCheckBox(index)

    # 设备类型
    def inputSel_device_type(self, index):
        self.selectCheckBox(index)

    # 电能表厂家
    def inputSel_meter_factory(self, index):
        self.selectCheckBox(index)

    # 电能表状态
    def inputSel_meter_status(self, index):
        self.selectCheckBox(index)

    # 查询按钮
    def btn_qry(self):
        self.btn_query(True)
