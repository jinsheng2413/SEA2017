# -*- coding: utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_loseCountPowerMan.py
@time: 2018/11/2 0002 9:05
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.adv_app.lineLossAnalysis.lineLossMantain.lineLossMantain_data import LineLossMantain_data
from com.nrtest.sea.pages.adv_app.lineLossAnalysis.lineLossMantain.loseCountPowerMan_page import LoseCountPowerManPage, \
    LoseCountPowerManLocators
from com.nrtest.sea.task.commonMath import *


@ddt
class TestLoseCountPowerMan(unittest.TestCase, LoseCountPowerManPage):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(
            LineLossMantain_data.loseCountPowerMan_para, True)

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
        '''

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        '''
        sleep(2)
        # 打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        # 台区运行状态
        self.inputSel_zoneAreaRunStatus(para['ZONE_AREA_RUN_STATUS'])
        # 台区编码
        self.inputStr_zoneAreaCode(para['ZONE_AREA_CODE'])
        # 台区名称
        self.inputStr_zoneAreaName(para['ZONE_AREA_NAME'])
        # 责任人人工号
        self.inputStr_responsibilierNo(para['RESPONSIBLLIER_NO'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*LoseCountPowerManLocators.TAB_ONE)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(LineLossMantain_data.loseCountPowerMan_para))
    def test_query(self, para):
        self.query(para)
