# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: verficationResultDetail_page.py
@time: 2018/11/16 0016 14:33
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.sys_mam.archivesVerficationMan.VerficationResultDetail_locators import \
    VerficationResultDetailLocators


# 系统管理--》档案核查管理--》核查结果明细查询
class VerficationResultDetailPage(Page):
    # 开始日期
    def inputStr_start_time(self, value):
        self.input(value, *VerficationResultDetailLocators.QRY_START_DATE)

        # 开始日期

    def inputStr_zoneAreaNo(self, value):
        self.input(value, *VerficationResultDetailLocators.QRY_ZONE_AREA_NO)

    # 结束时间
    def inputStr_end_time(self, value):
        self.input(value, *VerficationResultDetailLocators.QRY_END_TIME)

        # 查询

    def btn_qry(self):
        self.click(*VerficationResultDetailLocators.BTN_QRY)
