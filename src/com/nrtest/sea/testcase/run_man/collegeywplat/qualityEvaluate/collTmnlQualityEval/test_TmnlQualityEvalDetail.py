# -*- coding: utf-8 -*-

"""
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: test_Tmnl.py
@time: 2018/11/12 9:20
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.operOrganMan.operOrganMan_data import OperOrganManData
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.run_man.operOrganMan.qualityEvaluate.collTmnlQualityEval_page import \
    TmnlQualityEvalDetailPage


# 运行管理→采集运维平台→采集终端质量评价
# 终端质量评价明细
@ddt
class TestTmnlQualityEvalDetail(TestCase, TmnlQualityEvalDetailPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(OperOrganManData.para_CollTmnlQualityEval)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        menuPage.clickTabPage(OperOrganManData.para_TmnlQualityEval_detail)
        menuPage.remove_dt_readonly()

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 关闭页面
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

        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])

        # 用户类型
        self.inputSel_cons_type(para['CONS_TYPE'])
        # 故障严重程度
        self.inputSel_fault_level(para['FAULT_LEVEL'])
        # 终端厂家
        self.inputSel_tmnl_fac(para['TMNL_FAC'])
        # 故障类别
        self.inputSel_fault_type(para['FAULT_TYPE'])
        # 故障开始日期
        self.inputDt_Start_Date(para['START_DATE'])
        # 故障开始日期
        self.inputDt_End_Date(para['END_DATE'])

        self.btn_qry()
        self.sleep_time(2)

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

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(OperOrganManData.para_CollTmnlQualityEval, OperOrganManData.para_TmnlQualityEval_detail))
    def test_query(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(OperOrganManData.para_CollTmnlQualityEval, OperOrganManData.para_TmnlQualityEval_detail, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()

    # def test_test(self):
    #     # 供电单位
    #     openLeftTree('13401')
    #     # 终端类型
    #     self.inputRSel_tmnl_type('全部')
    #     # 终端厂家
    #     self.inputRSel_tmnl_fac('宁波三星')
    #     # 查询日期
    #     self.inputDt_query_date('2018-09')
    #
    #     self.btn_query()
    #     self.sleep_time(2)
    #     # 校验
    #     result = self.assert_context(TmnlClockStaticLocators.TABLE_DATA)
    #     self.assertTrue(result)
