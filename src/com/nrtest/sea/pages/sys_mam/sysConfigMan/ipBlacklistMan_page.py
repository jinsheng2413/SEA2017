# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: ipBlacklistMan_page.py
@time: 2018/11/20 14:08
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→系统配置管理→IP黑名单管理
class IpBlacklistManPage(Page):
    # IP地址
    def inputStr_ip_addr(self, content):
        # self.input(content, *IpBlacklistManLocators.QRY_IP_ADDR)
        self.input(content)

    # 查询按钮
    def btn_search(self):
        # self.click(*IpBlacklistManLocators.BTN_SEARCH)
        self.btn_query()
