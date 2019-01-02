# -*- coding: utf-8 -*-

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
from com.nrtest.sea.data.adv_app.costControlManage.costControlManage_data import CostControlManage_data
from com.nrtest.sea.pages.adv_app.costControlManage.eleParaManLocators_pages import EleParaManPage, EleParaManLocators
from com.nrtest.sea.task.commonMath import *


# 高级应用--》费控管理--》本地费控--》电价参数管理
@ddt
class TestDemo(unittest.TestCase, EleParaManPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(CostControlManage_data.eleParaMan_para)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
        cls.closePages(cls)

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
        # 去除查询干扰数据(要传入对应的page页面类)
        # self.clear_values(EleParaManPage)
        # 回收左边树
        self.recoverLeftTree()

    def custQuery(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        # 开始时间
        self.inputStr_startTimeOne(para['START_TIME'])
        # 结束时间
        self.inputStr_EndTimeOne(para['END_TIME'])
        # 是否已生成参数
        self.inputSel_ComeIntoPara_One(para['COME_INTO_PARA'])

        self.btn_qryOne()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(EleParaManLocators.TAB_ONE)
        self.assertTrue(result)

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        # 开始时间
        self.inputStr_startTimeTwo(para['START_TIME'])
        # 结束时间
        self.inputStr_endTimeTwo(para['END_TIME'])
        # 是否已生成参数
        self.inputSel_ComeIntoPara_Two(para['COME_INTO_PARA'])
        self.btn_qryOne()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(EleParaManLocators.TAB_ONE)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(CostControlManage_data.eleParaMan_para))
    def test_query(self, para):
        self.query(para)
