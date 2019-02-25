# -*- coding: utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_LosePowerMan.py
@time: 2018/10/31 0031 13:35
@desc:
"""
from time import sleep
from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.lineLossMantain.lineLossMantain_data import LineLossMantain_data
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.lineLossMantain.losePowerMan_page import LosePowerManPage
from com.nrtest.sea.pages.other.menu_page import MenuPage


@ddt
# 高级应用→线损分析→线损模型维护→线损模型设计
class TestLosePowerMan(TestCase, LosePowerManPage):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）ljf
        menuPage = MenuPage.openMenu(LineLossMantain_data.losePowerMan_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)


    @classmethod
    def tearDownClass(cls):
        print('执行结束')
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
        # 选择节点
        self.openLeftTree(para['TREE_NODE'])

        # 考核单元名称
        self.inputStr_chkunit_name(para['CHKUNIT_NAME'])

        # 考核单元分类
        self.inputSel_chkunit_type(para['CHKUNIT_TYPE'])
        sleep(0.5)
        para_value = self.get_para_value(para['CHKUNIT_TYPE'])
        if para_value == '台区':
            # 台区编号
            self.inputStr_tg_no(para['TG_NO'])

            # 台区状态
            self.inputSel_tg_status(para['TG_STATUS'])
        elif para_value == '线路':
            # 线路编号
            self.inputStr_line_no(para['LINE_NO'])

        # 组合标志
        self.inputSel_combination_flag(para['COMBINATION_FLAG'])

        # 考核单元状态
        self.inputSel_chkunit_status(para['CHKUNIT_STATUS'])

        # 未覆盖
        self.inputChk_uncover(para['UNCOVER'])

        # 查询
        self.btn_qry()

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
    @data(*DataAccess.getCaseData(LineLossMantain_data.losePowerMan_para))
    def test_query(self, para):
        """高级应用→线损分析→线损模型维护→线损模型设计
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LineLossMantain_data.losePowerMan_para, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
