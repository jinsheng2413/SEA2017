# -*- coding: utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: commModulPropMain_page.py
@time: 2018/11/2 0002 11:27
@desc:
"""

from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.run_man.runStatusMonitor.communicationModuleManagement.commModulPropMain_locators import \
    ModuleAttributeRelationshipMantainLocators


# 运行管理--》采集信道管理--》通信模块管理--》通信模块属性维护
class CommunicationModuleBaseInformationMantainPage(Page):
    # 模块厂商
    def inputSel_moduleFactory(self, item):
        # self.click(
        #     *CommunicationModuleBaseInformationMantainLocators.QRY_MODULE_FACTORY)
        # locator = self.get_select_locator(CommunicationModuleBaseInformationMantainLocators.QRY_MODULE_FACTORY_VALUE,
        #                                   item)
        # self.click(*locator)
        self.selectDropDown(item)

    # 模块版本
    def inputSel_moduleVer(self, item):
        self.selectDropDown(item)

    # 模块属性标识
    def inputStr_moduleAttrbuteSign(self, value):
        self.input(value)  # , *CommunicationModuleBaseInformationMantainLocators.QRY_MODULE_ATTRBUTE_SIGN)

    # 模块类型
    def inputSel_moduleType(self, item):
        # self.click(
        #     *CommunicationModuleBaseInformationMantainLocators.QRY_MODULE_TYPE)
        # locator = self.get_select_locator(
        #     CommunicationModuleBaseInformationMantainLocators.QRY_MODULE_TYPE_VALUE, item)
        # self.click(*locator)
        self.selectDropDown(item)

    # 查询
    def btn_qry(self):
        # self.click(*CommunicationModuleBaseInformationMantainLocators.BTN_QRY)
        self.btn_query(True)


class ModuleAttributeRelationshipMantainPage(Page):
    # 终端地址
    def inputStr_tmnlAddr(self, value):
        self.input(value)  #, *ModuleAttributeRelationshipMantainLocators.QRY_TMNL_ADDR)

    # 终端厂家
    def inputSel_tmnlFactory(self, item):
        # self.input(name, *ModuleAttributeRelationshipMantainLocators.QRY_TMNL_FACTORY)
        self.selectDropDown(item)

    # 维护状态
    def inputChk_mainten_status(self, items):
        self.clickCheckBox(items, ModuleAttributeRelationshipMantainLocators.QRY_MAINTEN_STATUS)

    # 查询
    def btn_qry(self):
        # self.click(*ModuleAttributeRelationshipMantainLocators.BTN_QRY)
        self.btn_query(True)
