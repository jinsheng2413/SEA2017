# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: userCollectStatistics_page.py
@time: 2018/10/24 14:12
@desc:
"""

from com.nrtest.common.base_page import Page


# 统计查询→综合查询→采集建设情况→采集覆盖情况→用户采集覆盖率统计
class UserCollectStatisticsPage(Page):
    # 用户类型
    def inputSel_cons_type(self, options):
        self.selectCheckBox(options)

    # 统计月份
    def inputDt_date(self, content):
        # self.exec_script(UserCollectStatisticsLocators.DATE_JS)
        # self.input(content, *UserCollectStatisticsLocators.DATE)
        self.inputDate(content)

    # 统计口径
    def inputSel_statistics_caliber(self, options):
        self.selectDropDown(options)

    # 查询按钮
    def btn_search(self):
        # self.click(UserCollectStatisticsLocators.BTN_SEARCH)
        self.btn_query()
