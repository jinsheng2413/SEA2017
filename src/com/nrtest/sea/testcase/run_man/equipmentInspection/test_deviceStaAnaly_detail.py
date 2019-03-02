# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test_deviceStaAnaly_detail.py
@time: 2019-02-14 15:53:58
@desc:
"""

from unittest import TestCase

from ddt import ddt, data

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.assert_result import AssertResult
from com.nrtest.common.data_access import DataAccess
from com.nrtest.sea.data.run_man.equipmentInspection.equipmentInspection_data import EquipmentInspection_data
from com.nrtest.sea.pages.other.menu_page import MenuPage
from com.nrtest.sea.pages.run_man.equipmentInspection.deviceStaAnaly_page import DeviceStaAnaly_detail_Page


# 运行管理→设备巡检→设备巡检合格情况统计:设备巡检指标参数明细
@ddt
class TestDeviceStaAnalyDetail(TestCase, DeviceStaAnaly_detail_Page):

    @classmethod
    def setUpClass(cls):
        # 打开菜单（需要传入对应的菜单编号）
        menuPage = MenuPage.openMenu(EquipmentInspection_data.deviceStaAnaly_para)
        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)
        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码
        menuPage.clickTabPage(EquipmentInspection_data.deviceStaAnaly_detail_tab)
        # 菜单页面上如果没日期型的查询条件时，请注释下面代码
        menuPage.remove_dt_readonly()

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
        每个测试用例测试结束后的操作，在这里做相关清理工作
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
        # 节点名
        self.openLeftTree(para['TREE_NODE'])

        # 终端厂家
        self.inputSel_tmnl_manufactory(para['TMNL_MANUFACTORY'])

        # 包含仪器
        self.inputChk_instrument(para['INSTRUMENT'])

        # 参数指标项
        self.inputSel_para_tpitmnl__nape(para['PARA_TPITMNL__NAPE'])

        # 结束日期
        self.inputDt_end_date(para['END_DATE'])

        # 开始日期
        self.inputDt_start_date(para['START_DATE'])

        # 巡检类型
        self.inputSel_polling_type(para['POLLING_TYPE'])

        # 日月
        self.inputChk_day_month(para['DAY_MONTH'])

        # 电表资产编号
        self.inputStr_meter_asset_no(para['METER_ASSET_NO'])

        # 终端地址
        self.inputStr_tmnl_addr(para['TMNL_ADDR'])

        # 终端资产编号
        self.inputStr_tmnl_asset_no(para['TMNL_ASSET_NO'])

        # 查询
        self.btn_qry()

    def assert_query_result(self, para):
        """
        查询结果校验（包括跳转）
        :param para:
        """
        self.assertTrue(AssertResult(self).check_query_result(para))

    def assert_query_criteria(self, para):
        """
        查询条件校验
        :param para:
        """
        result = self.check_query_criteria(para)
        self.assertTrue(result)

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(EquipmentInspection_data.deviceStaAnaly_para,
                                  EquipmentInspection_data.deviceStaAnaly_detail_tab))
    def test_query(self, para):
        """运行管理→设备巡检→设备巡检合格情况统计:设备巡检指标参数明细
        """
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_result(para)
        self.end_case()

    @BeautifulReport.add_test_img()
    @data(*DataAccess.getCaseData(EquipmentInspection_data.deviceStaAnaly_para,
                                  EquipmentInspection_data.deviceStaAnaly_detail_tab, valCheck=True))
    def _test_checkValue(self, para):
        self.start_case(para, __file__)
        self.query(para)
        self.assert_query_criteria(para)
        self.end_case()
