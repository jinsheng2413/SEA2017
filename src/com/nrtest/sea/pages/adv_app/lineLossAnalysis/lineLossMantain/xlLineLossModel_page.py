# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: xlLineLossModel_page.py
@time: 2019-02-20 11:42:54
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→线损分析→线损模型维护→线路线损模型:变电站线损模型
class XlLineLossModel_loss_Page(Page):
    # 变电站名称
    def inputSel_substation_name(self, option):
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# 高级应用→线损分析→线损模型维护→线路线损模型:主变线损模型
class XlLineLossModel_main_Page(Page):
    # 变电站名称
    def inputSel_substation_name(self, option):
        self.selectDropDown(option)

    # 主变
    def inputSel_miain_transformer(self, option):
        self.selectDropDown(option)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: xl_line_loss_model_page.py
@time: 2019-02-20 12:30:37
@desc:
"""

from com.nrtest.common.base_page import Page


# 高级应用→线损分析→线损模型维护→线路线损模型:母线电量平衡模型
class XlLineLossModel_ele_Page(Page):
    # 变电站名称
    def inputSel_substation_name(self, option):
        self.selectDropDown(option, is_multi_elements=True, is_multi_tab=True)

    # 电压等级
    def inputSel_ele_grade(self, option):
        self.selectDropDown(option)

    # 主变
    def inputSel_miain_transformer(self, option):
        self.selectDropDown(option, is_multi_tab=True, is_multi_elements=True)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
