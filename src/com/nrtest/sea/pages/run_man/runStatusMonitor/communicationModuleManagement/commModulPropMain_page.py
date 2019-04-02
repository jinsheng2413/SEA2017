# -*- coding: utf-8 -*-
"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: commModulPropMain_page.py
@time: 2018/11/2 0002 11:27
@desc:
"""

from com.nrtest.common.base_page import Page


# 运行管理→采集信道管理→通信模块管理→通信模块属性维护
class CommunicationModuleBaseInformationMantainPage(Page):
    # 模块厂商
    def inputSel_module_factory(self, item):
        # self.click(CommunicationModuleBaseInformationMantainLocators.QRY_MODULE_FACTORY)
        # locator = self.get_select_locator(CommunicationModuleBaseInformationMantainLocators.QRY_MODULE_FACTORY_VALUE,
        #                                   item)
        # self.click(locator)
        self.selectDropDown(item)

    # 模块版本
    def inputSel_module_ver(self, item):
        self.selectDropDown(item)

    # 模块属性标识
    def inputStr_module_attr_id(self, value):
        self.input(value)

    # 模块类型
    def inputSel_module_type(self, item):
        self.selectDropDown(item)

    # 选择指定行
    def inputRow_select_row(self, row_item):
        self.select_row(row_item)

    # 查询
    def btn_qry(self):
        self.btn_query(True)


class ModuleAttributeRelationshipMantainPage(Page):
    # 终端地址
    def inputStr_tmnl_addr(self, value):
        self.input(value)  # , *ModuleAttributeRelationshipMantainLocators.QRY_TMNL_ADDR)

    # 终端厂家
    def inputSel_tmnl_factory(self, item):
        # self.input(name, *ModuleAttributeRelationshipMantainLocators.QRY_TMNL_FACTORY)
        self.selectDropDown(item)

    # 维护状态
    def inputChk_mainten_status(self, items):
        self.clickCheckBox_new(items, is_multi_tab=True)

    # 表计类型
    def inputChk_meter_type(self, index):
        self.clickRadioBox(index)

    # 选择指定行
    def inputRow_select_row(self, row_item):
        self.select_row(row_item)

    # 查询
    def btn_qry(self):
        self.btn_query(True)
