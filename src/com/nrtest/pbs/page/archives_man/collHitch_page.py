# -*- coding:utf-8 -*-

"""
@author: 邵茜
@license: (C) Copyright 2019, Nari.
@file: collHitch_page.py
@time: 2019/3/15 14:18
@desc:
"""
from com.nrtest.pbs.locators.archives_man.collHitch_locators import CollHitch_locators
from com.nrtest.pbs.tree.tree_page import TreePBSPage


# 档案管理--采集点挂接


class CollHitchPage(TreePBSPage):
    # 输入框
    def input_name(self, value):
        self.input(value, *CollHitch_locators.INPUT_NAME)

    # 查询
    def btn_qry(self):
        self.click(CollHitch_locators.BTN_QUERY)
