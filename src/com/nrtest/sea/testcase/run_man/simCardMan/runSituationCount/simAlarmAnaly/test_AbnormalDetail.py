# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_AbnormalDetail.py
@time: 2018/11/9 0009 14:52
@desc:
"""
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.simCardMan.simCardMan_data import SimCardManData
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.run_man.simCardMan.runSituationCount.simAlarmAnaly_page import AbnormalDetailPage


# 运行管理-->SIM卡管理-->运行情况分析-->异常分析
# 异常明细
@ddt
class TestAbnormalDetail(TestCase, AbnormalDetailPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(SimCardManData.para_simAlarmAnaly)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(SimCardManData.para_simAlarmAnaly_detail)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
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
        # 月份
        self.inputDt_month_count(para['MONTH_COUNT'])
        #异常类型
        self.inputStr_except_type(para['EXCEPT_TYPE'])

        self.btn_qry()
        self.sleep_time(2)

    def assert_query_result(self, para):
        """
        查询结果校验
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
    @data(*DataAccess.getCaseData(SimCardManData.para_simAlarmAnaly,
                                  SimCardManData.para_simAlarmAnaly_detail))
    def test_query(self, para):
        """运行管理-->SIM卡管理-->运行情况分析-->异常分析:异常明细
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(SimCardManData.para_simAlarmAnaly,
                                  SimCardManData.para_simAlarmAnaly_detail, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
