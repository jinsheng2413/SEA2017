# -*- coding:utf-8 -*-

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
from com.nrtest.sea.pages.base_app.archivesMan.archivesAutoReview_page import ArchivesAutoReviewPage, \
    ArchivesAutoReviewLocators
from com.nrtest.sea.task.commonMath import *


# 基本应用--》档案管理--》电表批量导出（冀北）
@ddt
class TestArchivesAutoRevie(unittest.TestCase, ArchivesAutoReviewPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(ArchivesMan_data.archivesAutoReview_para)
        sleep(2)
        cls.exec_script(cls, ArchivesAutoReviewLocators.DATE_JS)

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
        # 去除查询干扰数据(要传入对应的page页面类)
        self.clear_values(ArchivesAutoReviewPage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        """

        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        """

        # 选择导入电表信息
        self.inputSel_leadInto_meter_info(para['LEADINTO_METER'])
        # 输入日期
        self.inputStr_date(para['DATE'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ArchivesAutoReviewLocators.TAB_ONE)
        self.assertTrue(result)

    @data(*DataAccess.getCaseData(ArchivesMan_data.archivesAutoReview_para))
    def test_query(self, para):
        self.query(para)
