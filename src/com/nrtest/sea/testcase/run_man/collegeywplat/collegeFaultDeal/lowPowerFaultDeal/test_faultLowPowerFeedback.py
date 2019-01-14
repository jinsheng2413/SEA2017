# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_faultHandler.py
@time: 2018/11/12 0012 9:31
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.collegeywplat.acquistionFaultHandling.acquistionFaultHandling_data import \
    AcquistionFaultHandling_data
from com.nrtest.sea.pages.run_man.collegeywplat.lowPowerFaultDeal.lowPowerFaultDeal_page import FaultLowPowerFeedbackPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


# 运行管理-->采集运维平台-->采集故障处理-->低压故障处理
# 故障反馈低压
@ddt
class TestFaultLowPowerFeedback(TestCase,FaultLowPowerFeedbackPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(AcquistionFaultHandling_data.para_lowPowerFaultDeal)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        menuPage.clickTabPage(AcquistionFaultHandling_data.para_lowPowerFaultDeal_feedback)
        menuPage.remove_dt_readonly()


    @classmethod
    def tearDownClass(cls):
        print("执行结束")
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
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 打开左边树并选择
        self.openLeftTree(para['TREE_NODE'])

        #故障开始日期
        self.inputDt_fault_start_date(para['FAULT_START_DATE'])
        #故障结束日期
        self.inputDt_fault_end_date(para['FAULT_END_DATE'])
        #流程状态
        self.inputSel_process(para['PROCESS_STATUS'])
        #故障来源
        self.inputDt_fault_from(para['FAULT_FROM'])
        #故障严重程度
        self.inputSel_fault_severity(para['FAULT_SEVERITY'])
        # 故障类型
        self.inputChk_fault_type(para['FAULT_TYPE'])

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
    @data(*DataAccess.getCaseData(AcquistionFaultHandling_data.para_lowPowerFaultDeal, AcquistionFaultHandling_data.para_lowPowerFaultDeal_feedback))
    def test_query(self, para):
        """运行管理-->采集运维平台-->采集故障处理-->低压故障处理:故障反馈低压
        对查询结果有无、数据链接跳转等校验
        :param para: 用例数据
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(AcquistionFaultHandling_data.para_lowPowerFaultDeal, AcquistionFaultHandling_data.para_lowPowerFaultDeal_feedback, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
