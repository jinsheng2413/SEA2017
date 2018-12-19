# -*- coding:utf-8 -*-

"""
@author: 吴竹筠
@license: (C) Copyright 2018, Nari.
@file: testcase_terParaSet.py
@time: 2018/11/6 0006 11:23
@desc:
"""
import unittest

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.fieldMan.termParaSet_data import TermParaSet_data
from com.nrtest.sea.pages.run_man.fieldMan.termParaSet_pages import TermParaSetPage
from com.nrtest.sea.task.commonMath import *


# 运行管理-现场管理-终端运行参数设置
@ddt
class TestDemo(unittest.TestCase, TermParaSetPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号,Ture的作用：利用中文名称点击菜单）
        cls.driver = openMenu(TermParaSet_data.TermParaSet_para)

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
        openLeftTree(para['TREE_NODE'])  # 'ORG_NO'])
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])
        self.inputSel_tmnl_factory(para['TMNL_FACTORY'])
        self.inputSel_task_status(para['TASK_STATUS'])
        self.inputSel_tmnl_protory(para['TMNL_PROTORY'])

        self.btn_qry()
        self.sleep_time(2)

        # 校验
        # result = self.assert_context(*)
        # self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(TermParaSet_data.TermParaSet_para))
    def test_query(self, para):
        self.query(para)
