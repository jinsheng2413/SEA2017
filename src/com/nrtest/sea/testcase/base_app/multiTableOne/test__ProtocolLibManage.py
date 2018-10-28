# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_demo.py
@time: 2018/9/10 0010 9:21
@desc:
"""
import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.multiTableOne.multiTableOne import MultiTableOne
from com.nrtest.sea.pages.base_app.multiTableOne.protocolLibManage_page import ProtocolLibManageLocatorsPage, \
    ProtocolLibManageLocators
from com.nrtest.sea.task.commonMath import *


@ddt
class TestDemo(unittest.TestCase, ProtocolLibManageLocatorsPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(MultiTableOne.protocolLibManage_para)
        sleep(2)
        cls.exec_script(cls, ProtocolLibManageLocators.START_DATE_JS)
        cls.exec_script(cls, ProtocolLibManageLocators.END_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        # 刷新浏览器
        cls.refreshPage(cls)

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 协议名称
        self.inputStr_protocolName(para['PROTOCOL_NAME'])
        # 厂商名称
        self.inputStr_manufacturerName(para['MANUFACTURER_NAME'])
        # 协议类型
        self.inputStr_protocolType(para['PROTOCOL_TYPE'])
        # 表记类型
        self.inputStr_surfaceType(para['SURFACE_TYPE'])
        # 维护时间
        self.inputStr_maintenanceTmie(para['MANUFACTURER_TMIE'])
        # 结束时间
        self.inputStr_endTime(para['END_TIME'])
        # 有效标志
        self.inputSel_effectiveSign(para['EFFECTIVE_SIGN'])
        # 协议版本号
        self.inputStr_protocolVersionNo(para['PROTOCOL_VERSION_NO'])
        # 协议代码
        self.inputStr_protocolCode(para['PROTOCOL_CODE'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ProtocolLibManageLocators.TAB_ONE)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(MultiTableOne.protocolLibManage_para))
    def test_query(self, para):
        self.query(para)
