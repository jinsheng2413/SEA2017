# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: flowAnaly_page.py
@time: 2018/11/9 0009 9:43
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理-->SIM卡管理-->运行情况分析-->异常分析
# 异常统计
class AbnoralStaticPage(Page):

    # 月份
    def inputDt_month(self, value):
        # self.input(value,*AbnormalCountLocators.QRY_MONTH)
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        # self.click(AbnormalDetailLocators.BTN_QRY)
        self.btn_query()

# 异常明细
class AbnormalDetailPage(Page):

    # 异常类型
    def inputStr_Abnormal_Type(self, item):
        # self.click(AbnormalDetailLocators.QRY_ABNORMAL_TYPE)
        # locator = self.get_select_locator(AbnormalDetailLocators.QRY_ABNORMAL_TYPE_VALUE, name)
        # self.click(locator)
        self.selectDropDown(item)

    # 月份
    def inputDt_month(self, value):
        # self.input(value, *AbnormalDetailLocators.QRY_MONTH)
        self.inputDate(value)

    # 查询
    def btn_qry(self):
        # self.click(AbnormalDetailLocators.BTN_QRY)
        self.btn_query(True)
