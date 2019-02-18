# -*- coding: utf-8 -*-"""@author: 韩笑@license: (C) Copyright 2018, Nari.@file: test_strategicArchivesQueryMeter.py@time: 2019-02-18 16:36:22@desc:"""from unittest import TestCasefrom ddt import ddt, datafrom com.nrtest.common.BeautifulReport import BeautifulReportfrom com.nrtest.common.data_access import DataAccessfrom com.nrtest.sea.data.base_app.terminalMan.terminalMan_data import TerminalMan_datafrom com.nrtest.sea.pages.base_app.terminalMan.strategicArchivesQuery_page import StrategicArchivesQueryMeterPagefrom com.nrtest.sea.pages.other.menu_page import MenuPage# 基本应用→终端管理→关口档案维护:电表档案查询@ddtclass test_StrategicArchivesQuery(TestCase, StrategicArchivesQueryMeterPage):    @classmethod    def setUpClass(cls):        # 打开菜单（需要传入对应的菜单编号）        menuPage = MenuPage.openMenu(TerminalMan_data.strategicArchivesQuery_para)        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码        menuPage.clickTabPage(TerminalMan_data.strategicArchivesQuery_tabName_meter)        # 菜单页面上如果没日期型的查询条件时，请注释下面代码        menuPage.remove_dt_readonly()    @classmethod    def tearDownClass(cls):        print("执行结束")        # 关闭菜单页面        cls.closePages(cls)    def setUp(self):        """        测试固件的setUp()的代码，主要是测试的前提准备工作        :return:        """    def tearDown(self):        """        每个测试用例测试结束后的操作，在这里做相关清理工作        :return:        """        # 回收左边树        self.recoverLeftTree()    def query(self, para):        """        :param para: Dict类型的字典，不是dict        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值        key值要与tst_case_detail表中的XPATH_NAME的值保持一致        """        # 节点名        self.openLeftTree(para['TREE_NODE'])        # 直属        self.inputChk_directly(para['DIRECTLY'])        # 电表厂家        self.inputSel_meter_factory(para['METER_FACTORY'])        # 规约类型        self.inputSel_protocol_type(para['PROTOCOL_TYPE'])        # 电表地址        self.inputStr_meter_addr(para['METER_ADDR'])        # 电表名称        self.inputStr_meter_name(para['METER_NAME'])        # 终端地址        self.inputStr_tmnl_addr(para['TMNL_ADDR'])        # 查询        self.btn_qry()    def assert_query_result(self, para):        """        查询结果校验（包括跳转）        :param para:        """        self.assertTrue(self.check_query_result(para))    def assert_query_criteria(self, para):        """        查询条件校验        :param para:        """        result = self.check_query_criteria(para)        self.assertTrue(result)    @BeautifulReport.add_test_img()    @data(*DataAccess.getCaseData(TerminalMan_data.strategicArchivesQuery_para,                                  TerminalMan_data.strategicArchivesQuery_tabName_meter))    def test_query(self, para):        """基本应用→档案管理→关口档案维护:电表档案查询        """        self.start_case(para, __file__)        self.query(para)        self.assert_query_result(para)        self.end_case()    @BeautifulReport.add_test_img()    @data(*DataAccess.getCaseData(TerminalMan_data.strategicArchivesQuery_para,                                  TerminalMan_data.strategicArchivesQuery_tabName_meter, valCheck=True))    def _test_checkValue(self, para):        self.start_case(para, __file__)        self.query(para)        self.assert_query_criteria(para)        self.end_case()