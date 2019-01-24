# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: tgLineLossDetail_page.py
@time: 2018/11/2 10:07
@desc:
"""
from com.nrtest.common.base_page import Page


# 高级应用→线损分析→台区线损统计查询→台区线损明细
class TgLineLossDetailPage(Page):
    # 台区编号
    def inputStr_tg_no(self, content):
        self.input(content)

    # 台区名称
    def inputStr_tg_name(self, content):
        self.input(content)

    # 查询日期,开始
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 查询日期，结束
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 责任人工号
    def inputStr_person_resp_no(self, content):
        self.input(content)

    # 采集覆盖率
    def inputSel_collectCoverRate(self, value):
        self.selectDropDown(value)

    # 采集成功率
    def inputSel_collectSuccessRate(self, value):
        self.selectDropDown(value)

    # 同期线损率
    def inputSel_lineLoss(self, value):
        self.selectDropDown(value)

    # 时间类型
    def inputChk_dateType(self, value):
        self.clickRadioBox(value)

    # 运算类型
    def inputChk_runType(self, value):
        self.clickRadioBox(value)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
