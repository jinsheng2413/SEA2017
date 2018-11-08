# -*- coding: utf-8 -*-
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.stat_rey.synthQuery.userDataQuery_locators import UserDataQueryLocators


# 统计查询→综合查询→用户数据查询
class UserDataQueryPage(Page):
    # 页面元素
    # 用户编号
    def inputStr_usernum(self, content):
        self.input(content, *UserDataQueryLocators.QRY_USERNUM)

    # 查询按钮
    def btn_search(self):
        self.click(*UserDataQueryLocators.BTN_SEARCH)

    # 操作对象选择区
    # 国网冀北电力有限公司
    def inputNode_jibei(self):
        self.click(*UserDataQueryLocators.TREE_JIBEI)

    # 唐山供电公司
    def inputNode_tangshan(self):
        self.click(*UserDataQueryLocators.TREE_TANGSHAN)

    # 直属用户
    def inputNode_directlyuser(self):
        self.click(*UserDataQueryLocators.TREE_DIRECTLYUSER)

    # 电网_国各庄
    def inputNode_guogezhuang(self):
        self.click(*UserDataQueryLocators.TREE_GUOGEZHUANG)

    # 基本档案
    def btn_basicfile(self):
        self.click(*UserDataQueryLocators.BTN_BASICFILE)

    # 数据展示
    def btn_datashow(self):
        self.click(*UserDataQueryLocators.BTN_DATASHOW)

    # 数据展示→电能示值
    # 实时
    def btn_electricenergy_realtime(self):
        self.click(*UserDataQueryLocators.BTN_ELECTRICENERGY_REALTIME)

    # 冻结
    def btn_electricenergy_frozen(self):
        self.click(*UserDataQueryLocators.BTN_ELECTRICENERGY_FROZEN)

    # 电表
    def inputsel_electricenergy_electricitymeter(self):
        self.click(*UserDataQueryLocators.SEL_ELECTRICENERGY_ELECTRICITYMETER)

    # 查询日期_开始
    def inputDt_electricenergy_starttime(self, content):
        self.click(content, *UserDataQueryLocators.QRY_ELECTRICENERGY_STARTTIME)

    # 查询日期_结束
    def inputDt_electricenergy_endtime(self, content):
        self.click(content, *UserDataQueryLocators.QRY_ELECTRICENERGY_ENDTIME)

    # 查询按钮
    def btn_electricenergy_search(self):
        self.click(*UserDataQueryLocators.BTN_ELECTRICENERGY_SEARCH)

    # 数据展示→电压曲线
    # 电压曲线
    def btn_voltagecurve(self):
        self.click(*UserDataQueryLocators.BTN_VOLTAGECURVE)

    # 实时
    def btn_voltagecurve_realtime(self):
        self.click(*UserDataQueryLocators.BTN_VOLTAGECURVE_REALTIME)

    # 冻结
    def btn_voltagecurve_frozen(self):
        self.click(*UserDataQueryLocators.BTN_VOLTAGECURVE_FROZEN)

    # 电表
    def inputsel_voltagecurve_electricitymeter(self):
        self.click(*UserDataQueryLocators.SEL_VOLTAGECURVE_ELECTRICITYMETER)

    # 查询日期
    def inputDt_electricenergy_time(self, content):
        self.click(content, *UserDataQueryLocators.QRY_VOLTAGECURVE_TIME)

    # 查询按钮
    def btn_voltagecurve_search(self, content):
        self.click(content, *UserDataQueryLocators.BTN_VOLTAGECURVE_SEARCH)

    # 数据展示→电流曲线
    # 电流曲线
    def btn_currentcurve(self):
        self.click(*UserDataQueryLocators.BTN_CURRENTCURVE)

    # 实时
    def btn_currentcurve_realtime(self):
        self.click(*UserDataQueryLocators.BTN_CURRENTCURVE_REALTIME)

    # 冻结
    def btn_currentcurve_frozen(self):
        self.click(*UserDataQueryLocators.BTN_CURRENTCURVE_FROZEN)

    # 电表
    def inputsel_currentcurve_electricitymeter(self):
        self.click(*UserDataQueryLocators.SEL_CURRENTCURVE_ELECTRICITYMETER)

    # 查询日期
    def inputDt_currentcurve_time(self, content):
        self.click(content, *UserDataQueryLocators.QRY_CURRENTCURVE_TIME)

    # 查询按钮
    def btn_currentcurve_search(self):
        self.click(*UserDataQueryLocators.BTN_CURRENTCURVE_SEARCH)

    # 数据展示→功率曲线
    # 功率曲线
    def btn_powercurve(self):
        self.click(*UserDataQueryLocators.BTN_POWERCURVE)

    # 实时
    def btn_powercurve_realtime(self):
        self.click(*UserDataQueryLocators.BTN_POWERCURVE_REALTIME)

    # 冻结
    def btn_powercurve_frozen(self):
        self.click(*UserDataQueryLocators.BTN_POWERCURVE_FROZEN)

    # 电表
    def inputsel_powercurve_electricitymeter(self):
        self.click(*UserDataQueryLocators.SEL_POWERCURVE_ELECTRICITYMETER)

    # 查询日期
    def inputDt_powercurve_time(self, content):
        self.click(content, *UserDataQueryLocators.QRY_POWERCURVE_TIME)

    # 查询按钮
    def btn_powercurve_search(self):
        self.click(*UserDataQueryLocators.BTN_POWERCURVE_SEARCH)

    # 数据展示→功率因数曲线
    # 功率因数曲线
    def btn_powerfactorcurve(self):
        self.click(*UserDataQueryLocators.BTN_POWERFACTORCURVE)

    # 电表
    def inputsel_powerfactorcurve_electricitymeter(self):
        self.click(*UserDataQueryLocators.SEL_POWERFACTORCURVE_ELECTRICITYMETER)

    # 查询日期
    def inputDt_powerfactorcurve_time(self, content):
        self.click(content, *UserDataQueryLocators.QRY_POWERFACTORCURVE_TIME)

    # 查询按钮
    def btn_powerfactorcurve_search(self):
        self.click(*UserDataQueryLocators.BTN_POWERFACTORCURVE_SEARCH)

    # 数据展示→电量
    # 电量
    def btn_electricquantity(self):
        self.click(*UserDataQueryLocators.BTN_ELECTRICQUANTITY)

    # 电表
    def inputsel_electricquantity_electricitymeter(self):
        self.click(*UserDataQueryLocators.SEL_ELECTRICQUANTITY_ELECTRICITYMETER)

    # 查询日期_开始
    def inputDt_electricquantity_starttime(self, content):
        self.click(content, *UserDataQueryLocators.QRY_ELECTRICQUANTITY_STARTTIME)

    # 查询日期_结束
    def inputDt_electricquantity_endtime(self, content):
        self.click(content, *UserDataQueryLocators.QRY_ELECTRICQUANTITY_ENDTIME)

    # 查询按钮
    def btn_electricquantity_search(self):
        self.click(*UserDataQueryLocators.BTN_ELECTRICQUANTITY_SEARCH)

    # 数据展示→负荷
    # 负荷
    def btn_load(self):
        self.click(*UserDataQueryLocators.BTN_LOAD)

    # 电表
    def inputsel_load_electricitymeter(self):
        self.click(*UserDataQueryLocators.SEL_LOAD_ELECTRICITYMETER)

    # 查询日期_开始
    def inputDt_load_starttime(self, content):
        self.click(content, *UserDataQueryLocators.QRY_LOAD_STARTTIME)

    # 查询日期_结束
    def inputDt_load_endtime(self, content):
        self.click(content, *UserDataQueryLocators.QRY_LOAD_ENDTIME)

    # 查询按钮
    def btn_load_search(self):
        self.click(*UserDataQueryLocators.BTN_LOAD_SEARCH)

    # 数据展示→用电异常
    # 用电异常
    def btn_abnormalelectricity(self):
        self.click(*UserDataQueryLocators.BTN_ABNORMALELECTRICITY)

    # 电表
    def inputsel_abnormalelectricity_electricitymeyer(self):
        self.click(
            *UserDataQueryLocators.SEL_ABNORMALELECTRICITY_ELECTRICITYMETER)

    # 查询日期_开始
    def inputDt_abnormalelectricity_startime(self, content):
        self.click(
            content, *UserDataQueryLocators.QRY_ABNORMALELECTRICITY_STARTTIME)

    # 查询日期_结束
    def inputDt_abnormalelectricity_endtime(self, content):
        self.click(
            content, *UserDataQueryLocators.QRY_ABNORMALELECTRICITY_ENDTIME)

    # 查询按钮
    def btn_abnormalelectricity_search(self):
        self.click(*UserDataQueryLocators.BTN_ABNORMALELECTRICITY_SEARCH)
