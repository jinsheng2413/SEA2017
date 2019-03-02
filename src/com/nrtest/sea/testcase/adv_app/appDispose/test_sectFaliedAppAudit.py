# -*- coding: utf-8 -*-"""@author: 韩笑@license: (C) Copyright 2018, Nari.@file: test_sectFaliedAppAudit.py@time: 2019-02-18 18:06:03@desc:"""from unittest import TestCasefrom ddt import ddt, datafrom com.nrtest.common.BeautifulReport import BeautifulReportfrom com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccessfrom com.nrtest.sea.data.adv_app.appDispose.appDispose_data import AppDispose_datafrom com.nrtest.sea.pages.adv_app.appDispose.sectFaliedAppAudit_page import SectFaliedAppAuditPagefrom com.nrtest.sea.pages.other.menu_page import MenuPage# 高级应用→工单处理→抄表失败工单审核@ddtclass TestSectFaliedAppAudit(TestCase, SectFaliedAppAuditPage):    @classmethod    def setUpClass(cls):        # 打开菜单（需要传入对应的菜单编号）        menuPage = MenuPage.openMenu(AppDispose_data.SectFaliedAppAudit_para)        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码        # menuPage.clickTabPage()        # 菜单页面上如果没日期型的查询条件时，请注释下面代码        menuPage.remove_dt_readonly()    @classmethod    def tearDownClass(cls):        print("执行结束")        # 关闭菜单页面        cls.closePages(cls)    def setUp(self):        """        测试固件的setUp()的代码，主要是测试的前提准备工作        :return:        """    def tearDown(self):        """        每个测试用例测试结束后的操作，在这里做相关清理工作        :return:        """        # 回收左边树        self.recoverLeftTree()    def query(self, para):        """        :param para: Dict类型的字典，不是dict        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值        key值要与tst_case_detail表中的XPATH_NAME的值保持一致        """        # 选择节点        self.openLeftTree(para['TREE_NODE'])        # 时间范围        self.inputChk_date_range(para['DATE_RANGE'])        if para['DATE_RANGE'] != '当月':            # 开始日期            self.inputDt_start_date(para['START_DATE'])            # 结束日期            self.inputDt_end_date(para['END_DATE'])        # 抄表段号        self.inputStr_mr_sect_no(para['MR_SECT_NO'])        # 工单状态        self.inputSel_app_status(para['APP_STATUS'])        # 审核状态        self.inputSel_check_status(para['CHECK_STATUS'])        # 查询        self.btn_qry()    def assert_query_result(self, para):        """        查询结果校验（包括跳转）        :param para:        """        self.assertTrue(AssertResult(self).check_query_result(para))    def assert_query_criteria(self, para):        """        查询条件校验        :param para:        """        result = self.check_query_criteria(para)        self.assertTrue(result)    @BeautifulReport.add_test_img()    @data(*DataAccess.getCaseData(AppDispose_data.SectFaliedAppAudit_para))    def test_query(self, para):        """高级应用→工单处理→抄表失败工单审核        """        self.start_case(para, __file__)        self.query(para)        self.assert_query_result(para)        self.end_case()    @BeautifulReport.add_test_img()    @data(*DataAccess.getCaseData(AppDispose_data.SectFaliedAppAudit_para, valCheck=True))    def _test_checkValue(self, para):        self.start_case(para, __file__)        self.query(para)        self.assert_query_criteria(para)        self.end_case()