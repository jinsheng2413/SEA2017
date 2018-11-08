# -*- coding: utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_LosePowerMan.py
@time: 2018/10/31 0031 13:35
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.lineLossMantain.lineLossMantain_data import LineLossMantain_data
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.lineLossMantain.losePowerMan_page import LosePowerManPage, \
    LosePowerManLocators
from com.nrtest.sea.task.commonMath import *


@ddt
# 高级应用-->线损分析--》线损模型维护--》线损模型设计
class TestLosePowerMan(unittest.TestCase, LosePowerManPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(LineLossMantain_data.losePowerMan_para)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 关闭菜单页面
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

        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        '''

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        '''
        sleep(2)

        # 打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        # 考核单元名称
        self.inputStr_assessUnitName(para['ASSESS_UNIT_NAME'])
        # 考核单元分类
        self.inputSel_assessUnitClassfication(
            para['ASSESS_UNIT_CLASSFICCATION'])
        # 组合标志
        self.inputSel_CombinationSign(para['COMBINATION_SIGN'])
        # 考核单元状态
        self.inputSel_assessUnitState(para['ASSESS_UNIT_STATE'])
        # 台区状态
        self.inputSel_ZoneAreaState(para['ZONE_AREA_STATE'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*LosePowerManLocators.TAB_ONE)
        self.assertTrue(result)

    # @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LineLossMantain_data.losePowerMan_para))
    def test_query(self, para):
        self.query(para)
