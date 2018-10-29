# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: sectfailedAppQuery_page.py
@time: 2018/10/29 11:19
@desc:
'''

from com.nrtest.sea.locators.adv_app.appDispose.sectfailedAppQuery_locators import SectfailedAppQueryLocators
from com.nrtest.common.base_page import Page

# 高级应用→工单处理→抄表失败工单查询
class SectfailedAppQueryPage(Page):
    # 抄表段号
    def inputStr_sect_no(self,content):
        self.input(content,*SectfailedAppQueryLocators.SECT_NO)
    # 抄表管理员工号
    def inputStr_sect_manager_no(self,content):
        self.input(content,*SectfailedAppQueryLocators.SECT_MANAGER_NO)
    # 查询按钮
    def btn_search(self):
        self.click(*SectfailedAppQueryLocators.BTN_SEARCH)