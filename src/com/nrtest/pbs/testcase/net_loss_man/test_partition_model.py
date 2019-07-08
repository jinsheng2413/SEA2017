# -*- coding: utf-8 -*-"""@author: 郭春彪@license: (C) Copyright 2018, Nari.@file: test_partition_model.py@time: 2019-07-08 09:11:34@desc:"""from unittest import TestCasefrom ddt import ddt, datafrom com.nrtest.common.BeautifulReport import BeautifulReportfrom com.nrtest.common.assert_result import AssertResultfrom com.nrtest.common.data_access import DataAccessfrom com.nrtest.pbs.page.net_loss_man.partition_model_page import PartitionModelPagefrom com.nrtest.sea.pages.other.menu_page import MenuPagefrom com.nrtest.pbs.data.net_loss_man.netLossMan_data import NetLossMan_data# 网损管理→分区模型@ddtclass TestPartitionModel(TestCase, PartitionModelPage):    @classmethod    def setUpClass(cls):        # 打开菜单（需要传入对应的菜单编号）        menuPage = MenuPage.openMenu(NetLossMan_data.partitionModel_para)        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)        cls.goto_frame(cls)        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码        # menuPage.clickTabPage()        # 菜单页面上如果没日期型的查询条件时，请注释下面代码        # menuPage.remove_dt_readonly()    @classmethod    def tearDownClass(cls):        print('执行结束')        # 刷新浏览器        # cls.closePages(cls)        cls.goto_home_page(cls)    def setUp(self):        """        测试固件的setUp()的代码，主要是测试的前提准备工作        :return:        """    def tearDown(self):        """        每个测试用例测试结束后的操作，在这里做相关清理工作        :return:        """       # 回收左边树        self.recoverLeftTree()    def query(self, para):        """        :param para: Dict类型的字典，不是dict        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值        key值要与tst_case_detail表中的XPATH_NAME的值保持一致        """        # 节点名        self.openLeftTree(para['TREE_NODE'])        # 地区名称        self.inputSel_area_name(para['AREA_NAME'])        # 关口属性        self.inputSel_barrier_properties(para['BARRIER_PROPERTIES'])        # 地区分量        self.inputSel_area_weight(para['AREA_WEIGHT'])        # 查询        self.btn_qry()    def assert_query_result(self, para):        """        查询结果校验（包括跳转）        :param para:        """        self.assertTrue(AssertResult(self).check_query_result(para))    def assert_query_criteria(self, para):        """        查询条件校验        :param para:        """        self.assertTrue(self.check_query_criteria(para))    @BeautifulReport.add_test_img()    @data(*DataAccess.getCaseData(NetLossMan_data.partitionModel_para))    def test_query(self, para):        """网损管理→分区模型        """        self.start_case(para, __file__)        self.query(para)        self.assert_query_result(para)        self.end_case()    @BeautifulReport.add_test_img()    @data(*DataAccess.getCaseData(NetLossMan_data.partitionModel_para, valCheck=True))    def _test_checkValue(self, para):        self.start_case(para, __file__)        self.query(para)        self.assert_query_criteria(para)        self.end_case()