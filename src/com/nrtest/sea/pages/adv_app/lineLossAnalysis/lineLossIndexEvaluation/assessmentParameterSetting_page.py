# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: assessmentParameterSetting_page.py
@time: 2018/11/1 9:24
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.lineLossAnalysis.lineLossIndexEvaluation.assessmentParameterSetting_locators import \
    AssessmentParameterSettingLocators


# 高级应用→线损分析→线损指标考核→考核参数设置
class AssessmentParameterSettingPage(Page):
    # 台区/线路名称
    def inputStr_tg_name(self, content):
        self.input(content, *AssessmentParameterSettingLocators.QRY_TG_NAME)

    # 查询按钮
    def btn_search(self):
        self.click(AssessmentParameterSettingLocators.BTN_SEARCH)
