# -*- coding: utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: securityQueryAndDelete_page.py
@time: 2018/10/29 9:22
@desc:
'''

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.intelligentLock.securityQueryAndDelete_locators import \
    SecurityQueryAndDeleteLocators


# 高级应用→智能锁具→权限查询及删除
class SecurityQueryAndDeletePage(Page):
    #电子钥匙编号
    def inputStr_key_no(self,content):
        self.input(content,*SecurityQueryAndDeleteLocators.KEY_NO)
    #锁封编号
    def inputStr_lock_no(self,content):
        self.input(content,*SecurityQueryAndDeleteLocators.LOCK_NO)
    #操作员编号
    def inputStr_staff_no(self,content):
        self.input(content,*SecurityQueryAndDeleteLocators.STAFF_NO)
    #查询按钮
    def btn_search(self):
        self.click(*SecurityQueryAndDeleteLocators.BTN_SEARCH)
