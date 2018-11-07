# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesQuery_locators.py
@time: 2018/8/31 0031 9:28
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.archivesMan.archivesQuery_locators import ArchivesQuery_locators


class ArchivesQueryPages(Page):
    # 【菜单】
    # 确认
    def btn_confirm(self):
        self.click(*ArchivesQuery_locators.BTN_CONFIRM)

    # 档案查询
    def btn_archivesQuery(self):
        self.click(ArchivesQuery_locators.BTN_ARCHIVES_QUERY)

    # 【查询条件】
    # 用户类型
    def inputCSel_cons_type(self, index):
        if index == 'c':
            self._find_element(*ArchivesQuery_locators.QRY_CONS_TYPE_CLEAR)
        else:
            self.click(*ArchivesQuery_locators.QRY_CONS_TYPE)
            locator = self.get_select_locator(
                ArchivesQuery_locators.QRY_CONS_TYPE_VALUE, index)
            self.click(*locator)
            self.click(*ArchivesQuery_locators.QRY_CONS_TYPE)

    # 抄表段号
    def inputStr_sect_no(self, value):
        self.input(value, *ArchivesQuery_locators.QRY_SECT_NO)

    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value, *ArchivesQuery_locators.QRY_TMNL_ADDR)

    # 【操作区】
    def btn_qry(self):
        self.click(*ArchivesQuery_locators.BTN_QRY)

    # 用户编号
    def btn_tab_cons_no(self):
        self.click(*ArchivesQuery_locators.TAB_ONE_CONS_NO)

    # 终端地址
    def btn_tab_tmnl_addr(self):
        self.click(*ArchivesQuery_locators.TAB_ONE_TMNL_ADDR)
