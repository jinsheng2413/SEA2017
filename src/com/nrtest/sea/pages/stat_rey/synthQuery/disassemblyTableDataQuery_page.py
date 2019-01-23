# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: disassemblyTableDataQuery_page.py
@time: 2018/10/9 14:01
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→销户和拆表数据查询
class DisassemblyTableDataQueryPage(Page):
    # 用户名称
    def inputStr_cons_name(self, content):
        self.input(content)  # , *DisassemblyTableDataQueryLocators.CONS_NAME)

    # 用户编号
    def inputStr_cons_no(self, content):
        self.input(content)  # , *DisassemblyTableDataQueryLocators.CONS_NO)

    # 用户类型
    def inputSel_cons_type(self, index):
        # if index == 'c':
        #     self._find_element(DisassemblyTableDataQueryLocators.CONS_TYPE)
        # else:
        #     self.click(DisassemblyTableDataQueryLocators.CONS_TYPE)
        #     locator = self.get_select_locator(
        #         DisassemblyTableDataQueryLocators.CONS_TYPE_VALUE, index)
        #     self.click(locator)
        #     self.click(DisassemblyTableDataQueryLocators.CONS_TYPE)
        self.selectCheckBox(index)

    # 终端地址
    def inputStr_tmnl_addr(self, content):
        self.input(content)  #, *DisassemblyTableDataQueryLocators.TMNL_ADDR)

    # 电能表资产号
    def inputStr_meter_asset_no(self, content):
        self.input(content)  #, *DisassemblyTableDataQueryLocators.METER_ASSET_NO)

    # 开始时间
    def inputDt_start_date(self, content):
        # self.exec_script(DisassemblyTableDataQueryLocators.START_DATE_JS)
        # self.input(content, *DisassemblyTableDataQueryLocators.START_DATE)
        self.inputDate(content)

    # 结束时间
    def inputDt_end_date(self, content):
        # self.exec_script(DisassemblyTableDataQueryLocators.END_DATE_JS)
        # self.input(content, *DisassemblyTableDataQueryLocators.END_DATE)
        self.inputDate(content)

    # 查询按钮
    def btn_search(self):
        # self.click(DisassemblyTableDataQueryLocators.BTN_SEARCH)
        self.btn_query()
