# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: param_abnormal_page.py
@time: 2019-02-15 14:37:05
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→设备巡检→参数指标管理
class ParamIndexManPage(Page):
    # 参数指标项
    def inputSel_para_tpi_nape(self, option):
        self.selectDropDown(option)

    # 仪器
    def inputChk_instrument(self, option):
        self.clickRadioBox(option)

    # 巡检类型
    def inputSel_polling_type(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query()
