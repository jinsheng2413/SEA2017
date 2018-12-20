# -*- coding: utf-8 -*-

"""
@author: jinsheng
@license: (C) Copyright 2018, Nari.
@file: knowledge_page.py
@time: 2018-11-02 11:31
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.adv_app.newsanswer.knowledge_locators import Knowledge_Locators


class Knowledge_Page(Page):
    # 文件类型
    def inputSel_file_type(self, index):
        self.click(*Knowledge_Locators.QRY_FILE_TYPE)
        locator = self.get_select_locator(
            Knowledge_Locators.QRY_FILE_TYPE_VALUE, index)
        self.click(*locator)

    # 文件名称
    def inputStr_file_name(self, value):
        self.input(value, *Knowledge_Locators.QRY_FILE_NAME)

    # 开始日期
    def inputStr_start_date(self, value):
        self.input(value, *Knowledge_Locators.QRY_START_DATE)

    # 结束日期
    def inputStr_end_date(self, value):
        self.input(value, *Knowledge_Locators.QRY_END_DATE)

    # 查询
    def btn_qry(self):
        self.click(*Knowledge_Locators.BTN_QUERY)
