# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: sim_archives_man_page.py
@time: 2019-02-14 09:58:20
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→SIM卡管理→档案管理:01
class SimArchivesManPage(Page):
    # 待提交批次号
    def inputStr_batch_no(self, value):
        self.input(value)

    # 工作表名称
    def inputSel_work_table_name(self, option):
        self.selectDropDown(option)

    # 统一地区
    def inputSel_area_name(self, option):
        self.selectDropDown(option)

    # 统一运营商
    def inputSel_operator(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query(btn_name='查找')
