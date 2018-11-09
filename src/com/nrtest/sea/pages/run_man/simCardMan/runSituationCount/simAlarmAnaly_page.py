# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: flowAnaly_page.py
@time: 2018/11/9 0009 9:43
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.simCardMan.runSituationCount.simAlarmAnaly_locators import AbnormalCountLocators,AbnormalDetailLocators



# 运行管理-->SIM卡管理-->运行情况分析-->异常分析
class AbnoralCountPage(Page):

    # 月份
    def inputStr_month(self, value):
        self.input(value,*AbnormalCountLocators.QRY_MONTH)

        # 查询
    def btn_qry(self):
            self.click(*AbnormalDetailLocators.BTN_QRY)


class AbnormalDetailPage(Page):

    # 异常类型
    def inputStr_AbnormalType(self, name):
        self.click(*AbnormalDetailLocators.QRY_ABNORMAL_TYPE)
        locator = self.get_select_locator(AbnormalDetailLocators.QRY_ABNORMAL_TYPE_VALUE, name)
        self.click(*locator)
        # 月份

    def inputStr_month(self, value):
        self.input(value, *AbnormalDetailLocators.QRY_MONTH)

    # 查询
    def btn_qry(self):
        self.click(*AbnormalDetailLocators.BTN_QRY)