# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: msgSendQuery_page.py
@time: 2018/11/22 13:56
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→信息定制→推送信息定制→手机订阅→短信发送查询
class MsgSendQueryPage(Page):
    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content)

    # 开始时间
    def inputDt_start_date(self, content):
        self.inputDate(content)

    # 结束时间
    def inputDt_end_date(self, content):
        self.inputDate(content)

    # 发送状态
    def inputSel_send_stat(self, options):
        self.selectDropDown(options)

    # 发送方式
    def inputSel_send_way(self, options):
        self.selectDropDown(options)

    # 发送人
    def inputStr_send_man(self, content):
        self.input(content)

    # 查询按钮
    def btn_qry(self):
        self.btn_query()
