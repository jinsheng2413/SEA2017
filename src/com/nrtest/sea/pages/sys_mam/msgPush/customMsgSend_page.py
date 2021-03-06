# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: customMsgSend_page.py
@time: 2018/11/21 16:33
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→信息定制→推送信息定制→手机订阅→自定义短信发送
class CustomMsgSendPage(Page):
    # 单位名称
    def inputStr_org_name(self, content):
        self.input(content)

    # 联系人
    def inputStr_linkman(self, content):
        self.input(content)

    # 手机号码
    def inputStr_phone_no(self, content):
        self.input(content)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
