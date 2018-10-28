# -*- coding:utf-8 -*-

'''
@author: 陈越峰
@license: (C) Copyright 2018, Nari.
@file: test_sysDictMan.py
@time: 2018/9/13 11:23
@desc:
'''
import unittest

from ddt import ddt, data

from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.sys_mam.sysConfigMan.sysConfigMan_data import SysConfigManData
from com.nrtest.sea.locators.sys_mam.sysConfigMan.sysDictMan_locators import SysDictManLocators
from com.nrtest.sea.pages.sys_mam.sysConfigMan.sysDictMan_page import SysDictManPage
from com.nrtest.sea.task.commonMath import *


# 系统管理--》系统配置管理--》数据字典管理
@ddt
class TestSysDict(unittest.TestCase, SysDictManPage):

    @classmethod
    def setUpClass(cls):
        print("开始执行")
        cls.driver = openMenu(SysConfigManData.para_SysDictMan)
        cls.driver.execute_script(SysDictManLocators.START_DATE_JS)
        cls.driver.execute_script(SysDictManLocators.END_DATE_JS)

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
        # self.clear_values(SysDictManPage)
        # 回收左边树
        self.recoverLeftTree()

    def query(self, para):
        '''
        :param para: Dict类型的字典，不是dict
        ddt实现参数化（tst_case_detail数据表），通过key值，出入对应的值
        key值要与tst_case_detail表中的XPATH_NAME的值保持一致
        '''

        # 分类名称
        self.inputStr_catalog_name(para['CATALOG_NAME'])
        # 生效日期
        self.inputStr_start_date(para['START_DATE'])
        # 失效日期
        self.inputStr_end_date(para['END_DATE'])
        # 维护类型
        self.inputRSel_cons_type(para['EDIT_TYPE'])
        # 维护人员
        self.inputStr_editor(para['EDITOR'])
        # 数据来源
        self.inputRSel_data_source(para['DATA_SOURCE'])

        self.btn_query()
        self.sleep_time(2)
        # 校验
        result = self.assert_context(*SysDictManLocators.TAB_ONE)
        self.assertTrue(result)

    # @ddt.data(*DataCommon.do.getCaseData())
    @data(*DataAccess.getCaseData(SysConfigManData.para_SysDictMan))
    def test_que(self, para):
        self.query(para)


if __name__ == '__main__':
    unittest.main()
