# -*- coding:utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: countServeDeploy_page.py
@time: 2018/11/16 16:11
@desc:
"""

from com.nrtest.common.base_page import Page


# 系统管理→系统配置管理→计算服务配置
class CountServeDeployPage(Page):
    # JOB名称
    def inputSel_job_name(self, option):
        self.selectDropDown(option)

    # 服务名称
    def inputSel_service_name(self, option):
        self.selectDropDown(option)

    # 统计分类
    def inputChk_stat_type(self, option):
        self.clickRadioBox(option)

    # 查询按钮
    def btn_search(self):
        self.btn_query()
