# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_OutMemberMan_Troop.py
@time: 2018/11/13 0013 10:16
@desc:
"""
import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.collegeywplat.collegeywplat_data import Collegeywplat_data
from com.nrtest.sea.pages.collegeywplat.outMemberMan_page import OutNameTroopMemberPage, OutNameTroopMemberLocators
from com.nrtest.sea.task.commonMath import *


# 运行管理-->采集运维平台-->组织运维管理
@ddt
class TestOutMemberManTroop(unittest.TestCase,OutNameTroopMemberPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(Collegeywplat_data.outMemberMan_para)
        clickTabPage(Collegeywplat_data.outMemberMan_tab_TroopMenber)
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
        '''

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        '''
        clickTabPage(Collegeywplat_data.outMemberMan_tab_TroopMenber)
        #打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        #外包队伍名称
        self.inputStr_outName(para['OUT_NAME'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*OutNameTroopMemberLocators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(Collegeywplat_data.outMemberMan_para,Collegeywplat_data.outMemberMan_tab_TroopMenber))
    def test_query(self, para):
        self.query(para)



