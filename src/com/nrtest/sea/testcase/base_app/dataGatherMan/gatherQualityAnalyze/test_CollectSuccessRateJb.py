# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_demo.py
@time: 2018/9/10 0010 9:21
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.dataGatherMan.gatherQualityAnalyze.GatherQualityAnalyze_data import \
    GatherQualityAnalyze_data
from com.nrtest.sea.pages.base_app.dataGatherMan.gatherQualityAnalyze.collectSuccessRateJb_page import \
    CollectSuccessRateJbPage, CollectSuccessRateJbLocators
from com.nrtest.sea.task.commonMath import *

CollectSuccessRateJbPage


# 基本应用→数据采集管理→采集质量分析→采集成功率(冀北)

@ddt
class TestDemo(unittest.TestCase, CollectSuccessRateJbPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(GatherQualityAnalyze_data.collectSuccessRateJb_para)
        sleep(2)
        # cls.exec_script(cls,CollectSuccessRateJbLocators.START_DATE_JS)
        cls.remove_readonly(cls, CollectSuccessRateJbLocators.JS)

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

        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 注册菜单
        self.menu_name = para['MENU_NAME']
        # 打开左边树并选择
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        # 用户类型
        self.inputSel_user_type(para['USER_TYPE'])
        # 通信方式
        self.inputSel_conmunicationMode(para['CONMUNICATION_MODE'])
        # 终端厂家
        self.inputSel_TmnlFactory(para['TMNL_FACTORY'])
        # 芯片厂家
        self.inputSel_pieceFactory(para['PIECE_FACTORY'])
        # 通讯规约
        self.inputSel_conmunicationGlue(para['CONMUNICATION_GLUE'])
        # 时间
        self.inputStr_date(para['DATE'])
        # 相位
        self.inputSel_pieceFactory(para['PHASE'])
        print('--------------')

        self.btn_query()

    def assert_query_result(self, para):
        """
        查询结果校验（包括跳转）
        :param para:
        """
        self.assertTrue(self.check_query_result(para))

    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """
        result = self.check_query_criteria(para)
        self.assertTrue(result)

    #@BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(GatherQualityAnalyze_data.collectSuccessRateJb_para))
    def test_query(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_result(para)
        self.end_case(para)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(GatherQualityAnalyze_data.collectSuccessRateJb_para))
    def _test_checkValue(self, para):
        self.start_case(para)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case(para)
