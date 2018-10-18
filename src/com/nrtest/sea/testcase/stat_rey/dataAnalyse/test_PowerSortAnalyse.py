# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_demo.py
@time: 2018/9/10 0010 9:21
@desc:
'''
from com.nrtest.sea.data.stat_rey.dataAnalyse.loadrankanalyse_para import LoadRankAnalyse_para
from com.nrtest.sea.pages.stat_rey.dataAnalyse.powerSortAnalyse_page import PowerSortAnalysePage,PowerSortAnalyseLocators
from com.nrtest.sea.task.commonMath import *
from com.nrtest.common.data_access import DataAccess
from ddt import ddt, data
import unittest


@ddt
class TestPowerSortAnalyse(unittest.TestCase,PowerSortAnalysePage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(LoadRankAnalyse_para.powerSortAnalyse_para)
        sleep(2)
        cls.exec_script(cls,PowerSortAnalyseLocators.START_DATE_JS)
        cls.exec_script(cls,PowerSortAnalyseLocators.END_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print("执行结束")
        # 刷新浏览器
        cls.refreshPage(cls)

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

        #打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        #开始时间
        self.inputStr_start_time(para['START_TIME'])
        #结束时间
        self.inputStr_end_time(para['END_TIME'])
        #数量排名
        self.inputStr_rankingNumber(para['RANKING_NUMBER'])
        #用户类型
        self.inputSel_userType(para['USER_TYPE'])


        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*PowerSortAnalyseLocators.TAB_ONE)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(LoadRankAnalyse_para.powerSortAnalyse_para))
    def test_query(self, para):
        self.query(para)



