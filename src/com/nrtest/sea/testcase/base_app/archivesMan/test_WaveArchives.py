# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_demo.py
@time: 2018/9/10 0010 9:21
@desc:
"""
import unittest
from time import sleep

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.base_app.archivesMan.archivesMan_data import ArchivesMan_data
from com.nrtest.sea.pages.base_app.archivesMan.waveArchives_pages import WaveArchives_Page, WaveArchives_Locators
from com.nrtest.sea.task.commonMath import *


# 基本应用--》档案管理--》载波档案矫正
@ddt
class TestWaveArchives(unittest.TestCase, WaveArchives_Page):

    @classmethod
    def setUpClass(cls):
        print('开始执行')
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(ArchivesMan_data.waveArchives_para)
        sleep(2)
        cls.exec_script(cls, WaveArchives_Locators.START_DATE_JS)

    @classmethod
    def tearDownClass(cls):
        print('执行结束')
        # 刷新浏览器
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
        # 去除查询干扰数据(要传入对应的page页面类)
        # self.clear_values(WaveArchives_Page)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 输入台区编号
        self.inputStr_zone_no(para['ZONE_NO'])
        # 输入台区名称
        self.inputStr_zone_name(para['ZONE_NAME'])
        # 输入统计时间
        self.inputStr_Count_time(para['COUNT_TIME'])
        # 输入统计分类
        self.inputSel_countType(para['COUNT_TYPE'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*WaveArchives_Locators.TAB_ONE)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(ArchivesMan_data.waveArchives_para))
    def test_query(self, para):
        self.query(para)
