# -*- coding:utf-8 -*-


"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_scriptCheckTaskSet.py
@time: 2018/11/19 0019 14:59
@desc:
"""
from com.nrtest.sea.data.sys_mam.archivesVerficationMan.archivesVerficationMan_data import ArchivesVerficationMan_data
from com.nrtest.sea.pages.sys_mam.archivesVerficationMan.scriptCheckTaskSet_page import ScriptCheckTaskSetPage,ScriptCheckTaskSetLocators
from com.nrtest.sea.task.commonMath import *
from com.nrtest.common.data_access import DataAccess
from ddt import ddt, data
from time import sleep
from com.nrtest.common.BeautifulReport import BeautifulReport
import unittest
# 系统管理--》档案核查管理--》脚本核查任务编制
@ddt
class TestScriptCheckTaskSet(unittest.TestCase,ScriptCheckTaskSetPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        # 打开菜单（需要传入对应的菜单编号）
        cls.driver = openMenu(ArchivesVerficationMan_data.scriptCheckTaskSet_para)
        sleep(2)
        cls.exec_script(cls,ScriptCheckTaskSetLocators.SCRIPT_TYPE_JS)
        cls.exec_script(cls, ScriptCheckTaskSetLocators.TASK_STATUS_JS)



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

        #打开左边树并选择
        self.driver = openLeftTree(para['ORG_NO'])
        #脚本类型
        self.inputSel_scriptType(para['SCRIPT_TYPE'])
        #脚本名称
        self.inputStr_scriptName(para['SCRIPT_NAME'])
        #创建员工
        self.inputStr_creatStall(para['CREATE_STALL'])
        #任务状态
        self.inputSel_taskStatus(para['TASK_STATUS'])

        self.btn_qry()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*ScriptCheckTaskSetLocators.TAB_ONE)
        self.assertTrue(result)

    #@BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(ArchivesVerficationMan_data.scriptCheckTaskSet_para))
    def test_query(self, para):
        self.query(para)



