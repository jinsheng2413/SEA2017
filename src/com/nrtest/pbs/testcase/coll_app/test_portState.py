# -*- coding: utf-8 -*-"""@author: 邵茜@license: (C) Copyright 2018, Nari.@file: test_collSuccRate.py@time: 2019-03-06 14:44:46@desc:"""from unittest import TestCasefrom ddt import ddt, datafrom com.nrtest.common.BeautifulReport import BeautifulReportfrom com.nrtest.common.data_access import DataAccessfrom com.nrtest.pbs.data.coll_app.collOperMain_data import CollOperMain_datafrom com.nrtest.pbs.page.coll_app.collPortMonitor_page import CollPortMonitorPagefrom com.nrtest.sea.pages.other.menu_page import MenuPage# 采集运维--采集通道监视--通道状态查询@ddtclass test_CollSuccRate(TestCase, CollPortMonitorPage):    @classmethod    def setUpClass(cls):        # 打开菜单（需要传入对应的菜单编号）        menuPage = MenuPage.openMenu(CollOperMain_data.collPortMonitor_para)        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)        menuPage.intoPBSIframe()        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码        menuPage.clickTabPage(CollOperMain_data.portState_tab)        # 菜单页面上如果没日期型的查询条件时，请注释下面代码    @classmethod    def tearDownClass(cls):        print("执行结束")        cls.iframe_back(cls, num=1)        # 关闭菜单页面        cls.main_page(cls)    def setUp(self):        """        测试固件的setUp()的代码，主要是测试的前提准备工作        :return:        """    def tearDown(self):        """        每个测试用例测试结束后的操作，在这里做相关清理工作        :return:        """        # 回收左边树        # self.closeLeftTree()    def query(self, para):        """        :param para: Dict类型的字典，不是dict        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值        key值要与tst_case_detail表中的XPATH_NAME的值保持一致        """        # 节点名        self.inputSel_area_name(para['AREA_NAME'])        # 通道类型        self.inputSel_channel_type(para['CHANNEL_TYPE'])        # 端口状态        self.inputSel_port_state(para['PORT_STATE'])        # 网络状态        self.inputSel_network_state(para['NETWORK_STATE'])        # 查询        self.btn_qry()    def assert_query_result(self, para):        """        查询结果校验（包括跳转）        :param para:        """        # self.assertTrue(AssertResult(self).check_query_result(para))    def assert_query_criteria(self, para):        """        查询条件校验        :param para:        """        self.assertTrue(self.check_query_criteria(para))    @BeautifulReport.add_test_img()    @data(*DataAccess.getCaseData(CollOperMain_data.collPortMonitor_para,                                  CollOperMain_data.portState_tab))    def test_query(self, para):        """采集运维→采集监视        """        self.start_case(para, __file__)        self.query(para)        self.assert_query_result(para)        self.end_case()    @BeautifulReport.add_test_img()    @data(*DataAccess.getCaseData(CollOperMain_data.collPortMonitor_para,                                  CollOperMain_data.portState_tab, valCheck=True))    def _test_checkValue(self, para):        self.start_case(para, __file__)        self.query(para)        self.assert_query_criteria(para)        self.end_case()