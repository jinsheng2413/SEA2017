# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: collectSuccessRateJb_page.py
@time: 2018/8/22 0022 11:31
@desc:
"""

from com.nrtest.common.base_page import Page


# 基本应用→数据采集管理→采集质量分析→采集成功率(冀北)
class CollectSuccessRateJbPage(Page):

    # 曲线类型
    def inputChk_curve_type(self, name):
        self.clickRadioBox(name)

    # 通讯规约
    def inputSel_tmnl_protocol(self, name):
        self.selectDropDown(name)

    # 终端厂家
    def inputSel_tmnl_factory(self, name):
        self.selectDropDown(name)

    # 相位
    def inputSel_phase_code(self, name):
        self.selectDropDown(name)

    # 通信方式
    def inputSel_comm_mode(self, name):
        self.selectDropDown(name)

    # 用户类型
    def inputSel_cons_type(self, options):
        self.selectCheckBox(options)

    # 芯片厂家
    def inputSel_chip_factory(self, name):
        self.selectDropDown(name)

    # 日期时间
    def inputDt_date_time(self, value):
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        self.btn_query()
