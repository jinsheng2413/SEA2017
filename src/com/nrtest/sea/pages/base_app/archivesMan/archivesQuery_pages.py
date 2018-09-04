# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: archivesQuery_locators.py
@time: 2018/8/31 0031 9:28
@desc:
'''
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.base_app.archivesMan.archivesQuery_locators import ArchivesQuery_locators
class ArchivesQuery_pages(Page):
    #【菜单】
    #确认
    def btn_confirm(self):
        self.click(*ArchivesQuery_locators.BTN_CONFIRM)

    #档案查询
    def btn_archivesQuery(self):
        self.click(ArchivesQuery_locators.BTN_ARCHIVES_QUERY)

    #【查询条件】
    # 用户类型
    def inputCSel_user_cata(self,index):
        if index is 'c':
            self._find_element(*ArchivesQuery_locators.QRY_USER_CATA_CLEAR)
        else:
            self.click(*ArchivesQuery_locators.QRY_USER_CATA)
            locator = self.get_select_locator(ArchivesQuery_locators.QRY_USER_CATA_VALUE, index)
            self.click(*locator)
            self.click(*ArchivesQuery_locators.QRY_USER_CATA)



    #抄表段号
    def inputStr_readMeterNum(self,value):
        self.input(value,*ArchivesQuery_locators.QRY_READ_METER_NUM)

    #终端地址
    def inputStr_terminalAddr(self,value):
        self.input(value,*ArchivesQuery_locators.QRY_TERMINAL_ADDR)


    #【操作区】
    def btn_qry(self):
        self.click(*ArchivesQuery_locators.BTN_QRY)

    # 用户编号
    def btn_userNo_detail(self):
        self.click(*ArchivesQuery_locators.TAB_ONE_USER_NO)


    #终端地址
    def btn_termainal_addr(self):
        self.click(*ArchivesQuery_locators.QRY_TERMINAL_ADDR)




