# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: baseStationManage_page.py
@time: 2018/11/6 0006 15:59
@desc:
"""

from com.nrtest.common.base_page import Page

# 运行管理→采集信道管理→230M通信管理→基站信息维护
from com.nrtest.sea.locators.run_man.runStatusMonitor.MComMan230.baseStationManage_locators import \
    BaseStationManageLocators


class BaseStationManagePage(Page):
    # 通信地址
    def inputStr_comm_addr(self, value):
        self.input(value, *BaseStationManageLocators.QRY_COMMUNICATION_ADDR)

    # 查询
    def btn_qry(self):
        self.btn_query()
