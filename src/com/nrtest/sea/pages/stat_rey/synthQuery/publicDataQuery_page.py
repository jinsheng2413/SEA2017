# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: PublicDataQueryPage.py
@time: 2018-08-15 16:40
@desc:
'''

from com.nrtest.sea.locators.stat_rey.synthQuery.publicDataQuery_locators import PublicDataQueryLocators
from com.nrtest.common.base_page import Page

#统计查询→综合查询→配变数据查询
class PublicDataQueryPage(Page):
# 页面元素
    # 配变用户
    def inputstr_publicconsno(self,content):
        self.input(content,*PublicDataQueryLocators.QRY_PUBLICCONSNO)
    # 配变表号
    def inputstr_publicnum(self,content):
        self.input(content,*PublicDataQueryLocators.QRY_PUBLICNUM)
    # 查询按钮
    def btn_search(self):
        self.click(*PublicDataQueryLocators.BTN_SEARCH)
    # 基本档案
    def btn_basicfile(self):
        self.click(*PublicDataQueryLocators.BTN_BASICFILE)
    # 数据展示
    def btn_datashow(self):
        self.click(*PublicDataQueryLocators.BTN_DATASHOW)
# 操作对象选择区
#国网冀北电力有限公司
    def inputNode_jibei(self):
        self.click(*PublicDataQueryLocators.TREE_JIBEI)
    #唐山供电公司
    def inputNode_tangshan(self):
        self.click(*PublicDataQueryLocators.TREE_TANGSHAN)
    #直属用户
    def inputNode_directlyuser(self):
        self.click(*PublicDataQueryLocators.TREE_DIRECTLYUSER)
    #电网_狮子湾农改
    def inputNode_shiziwan(self):
        self.click(*PublicDataQueryLocators.TREE_SHIZIWAN)
# 数据展示
# 电压曲线
    # 下拉菜单
    def inputsel_voltagecurve_group(self):
        self.click(*PublicDataQueryLocators.INPUTSEL_VOLTAGECURVE_GROUP)
    # 查询日期
    def inputDt_voltagecurve_time(self):
        self.click(*PublicDataQueryLocators.INPUTDT_VOLTAGECURVE_TIME)
    # 查询按钮
    def btn_voltagecurve_search(self):
        self.click(*PublicDataQueryLocators.BTN_VOLTAGECURVE_SEARCH)
# 电流曲线
    # 电流曲线
    def btn_currentcurve(self):
        self.click(*PublicDataQueryLocators.BTN_CURRENTCURVE)
    # 下拉菜单
    def inputsel_currentcurve_group(self):
        self.click(*PublicDataQueryLocators.INPUTSEL_CURRENTCURVE_GROUP)
    # 查询日期
    def inputDt_currentcurve_time(self):
        self.click(*PublicDataQueryLocators.INPUTDT_CURRENTCURVE_TIME)
    # 查询按钮
    def btn_currentcurve_search(self):
        self.click(*PublicDataQueryLocators.BTN_CURRENTCURVE_SEARCH)
# 功率曲线
    # 功率曲线
    def btn_powercurve(self):
        self.click(*PublicDataQueryLocators.BTN_POWERCURVE)
    # 下拉菜单
    def inputsel_powercurve_group(self):
        self.click(*PublicDataQueryLocators.INPUTSEL_POWERCURVE_GROUP)
    # 查询日期
    def inputDt_powercurve_time(self):
        self.click(*PublicDataQueryLocators.INPUTDT_POWERCURVE_TIME)
    # 查询按钮
    def btn_powercurve_search(self):
        self.click(*PublicDataQueryLocators.BTN_POWERCURVE_SEARCH)
# 功率因数曲线
    # 功率因数曲线
    def btn_powerfactorcurve(self):
        self.click(*PublicDataQueryLocators.BTN_POWERFACTORCURVE)
    # 查询日期
    def inputDt_powerfactorcurve_time(self):
        self.click(*PublicDataQueryLocators.INPUTDT_POWERFACTORCURVE_TIME)
    # 查询按钮
    def btn_powerfactorcurve_search(self):
        self.click(*PublicDataQueryLocators.BTN_POWERFACTORCURVE_SEARCH)
