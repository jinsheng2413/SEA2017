# -*- coding:utf-8 -*-

'''
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: UserDataQueryLocators.py
@time: 2018/8/7 0002 09:00
'''

from selenium.webdriver.common.by import By


# 统计查询→综合查询→用户数据查询
class UserDataQueryLocators:
    # 页面元素
    # 用户编号
    QRY_USERNUM = (By.XPATH, '//input[@id="consNoForQuery"]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//table[@id="consDataQueryBtn"]//button[contains(text(),"查询")]')
    # 操作对象选择区
    # 国网冀北电力有限公司
    TREE_JIBEI = (By.XPATH, '//img[@class="x-tree-ec-icon x-tree-elbow-end-plus"]')
    # 唐山供电公司
    TREE_TANGSHAN = (By.XPATH, '//span[contains(text(),"唐山供电公司")]/../../img[@class="x-tree-ec-icon x-tree-elbow-plus"]')
    # 直属用户
    TREE_DIRECTLYUSER = (By.XPATH, '(//ul[@class="x-tree-node-ct"])[2]/li[1]/div/img[1]')
    # 电网_国各庄
    TREE_GUOGEZHUANG = (By.XPATH, '//span[contains(text(),"电网_国各庄")]')
    # 基本档案
    BTN_BASICFILE = (By.XPATH, '//span[contains(text(),"基本档案")]')
    # 数据展示
    BTN_DATASHOW = (By.XPATH, '//span[contains(text(),"数据展示")]')
    # 数据展示→电能示值
    # 实时
    BTN_ELECTRICENERGY_REALTIME = (By.XPATH, '(//label[contains(text(),"实时")]/../input)[1]')
    # 冻结
    BTN_ELECTRICENERGY_FROZEN = (By.XPATH, '(//label[contains(text(),"冻结")]/../input)[1]')
    # 电表
    SEL_ELECTRICENERGY_ELECTRICITYMETER = (By.XPATH, '//input[@name="meterShowValue_meterCombox"]')
    # 查询日期_开始
    QRY_ELECTRICENERGY_STARTTIME = (By.XPATH, '//input[@id="ext-comp-2110"]')
    # 查询日期_结束
    QRY_ELECTRICENERGY_ENDTIME = (By.XPATH, '//input[@id="ext-comp-2111"]')
    # 查询按钮
    BTN_ELECTRICENERGY_SEARCH = (By.XPATH, '(//table[@id="ext-comp-2160"]//button[contains(text(),"查询")])[1]')
    # 数据展示→电压曲线
    # 电压曲线
    BTN_VOLTAGECURVE = (By.XPATH, '//span[contains(text(),"电压曲线")]')
    # 实时
    BTN_VOLTAGECURVE_REALTIME = (By.XPATH, '(//label[contains(text(),"实时")]/../input)[2]')
    # 冻结
    BTN_VOLTAGECURVE_FROZEN = (By.XPATH, '(//label[contains(text(),"冻结")]/../input)[2]')
    # 电表
    SEL_VOLTAGECURVE_ELECTRICITYMETER = (By.XPATH, '//input[@name="voltCurve_meterCombox"]')
    # 查询日期
    QRY_VOLTAGECURVE_TIME = (By.XPATH, '//input[@class=" x-form-text x-form-field x-trigger-noedit x-form-focus"]')
    # 查询按钮
    BTN_VOLTAGECURVE_SEARCH = (By.XPATH, '(//table[@id="ext-comp-2160"]//button[contains(text(),"查询")])[2]')
    # 数据展示→电流曲线
    # 电流曲线
    BTN_CURRENTCURVE = (By.XPATH, '//span[contains(text(),"电流曲线")]')
    # 实时
    BTN_CURRENTCURVE_REALTIME = (By.XPATH, '(//label[contains(text(),"实时")]/../input)[3]')
    # 冻结
    BTN_CURRENTCURVE_FROZEN = (By.XPATH, '(//label[contains(text(),"冻结")]/../input)[3]')
    # 电表
    SEL_CURRENTCURVE_ELECTRICITYMETER = (By.XPATH, '//input[@name="elecCurve_meterCombox"]')
    # 查询日期
    QRY_CURRENTCURVE_TIME = (By.XPATH, '//input[@class=" x-form-text x-form-field x-trigger-noedit "]')
    # 查询按钮
    BTN_CURRENTCURVE_SEARCH = (By.XPATH, '(//table[@id="ext-comp-2160"]//button[contains(text(),"查询")])[3]')
    # 数据展示→功率曲线
    # 功率曲线
    BTN_POWERCURVE = (By.XPATH, '//span[contains(text(),"功率曲线")]')
    # 实时
    BTN_POWERCURVE_REALTIME = (By.XPATH, '(//label[contains(text(),"实时")]/../input)[4]')
    # 冻结
    BTN_POWERCURVE_FROZEN = (By.XPATH, '(//label[contains(text(),"冻结")]/../input)[4]')
    # 电表
    SEL_POWERCURVE_ELECTRICITYMETER = (By.XPATH, '//input[@name="powerCurve_meterCombox"]')
    # 查询日期
    QRY_POWERCURVE_TIME = (By.XPATH, '//input[@class=" x-form-text x-form-field x-trigger-noedit x-form-focus"]')
    # 查询按钮
    BTN_POWERCURVE_SEARCH = (By.XPATH, '(//table[@id="ext-comp-2160"]//button[contains(text(),"查询")])[4]')
    # 数据展示→功率因数曲线
    # 功率因数曲线
    BTN_POWERFACTORCURVE = (By.XPATH, '//span[contains(text(),"功率因数曲线")]')
    # 电表
    SEL_POWERFACTORCURVE_ELECTRICITYMETER = (By.XPATH, '//input[@name="factorCurve_meterCombox"]')
    # 查询日期
    QRY_POWERFACTORCURVE_TIME = (By.XPATH, '//input[@class=" x-form-text x-form-field x-trigger-noedit x-form-focus"]')
    # 查询按钮
    BTN_POWERFACTORCURVE_SEARCH = (By.XPATH, '(//table[@id="ext-comp-2160"]//button[contains(text(),"查询")])[5]')
    # 数据展示→电量
    # 电量
    BTN_ELECTRICQUANTITY = (By.XPATH, '//span[contains(text(),"电量")]')
    # 电表
    SEL_ELECTRICQUANTITY_ELECTRICITYMETER = (By.XPATH, '//input[@name="elecQuant_meterCombox"]')
    # 查询日期_开始
    QRY_ELECTRICQUANTITY_STARTTIME = (By.XPATH, '//input[@name="ext-comp-2395"]')
    # 查询日期_结束
    QRY_ELECTRICQUANTITY_ENDTIME = (By.XPATH, '//input[@name="ext-comp-2396"]')
    # 查询按钮
    BTN_ELECTRICQUANTITY_SEARCH = (By.XPATH, '(//table[@id="ext-comp-2160"]//button[contains(text(),"查询")])[6]')
    # 数据展示→负荷
    # 负荷
    BTN_LOAD = (By.XPATH, '//span[contains(text(),"负荷")]')
    # 电表
    SEL_LOAD_ELECTRICITYMETER = (By.XPATH, '//input[@name="load_meterCombox"]')
    # 查询日期_开始
    QRY_LOAD_STARTTIME = (By.XPATH, '//input[@name="ext-comp-3012"]')
    # 查询日期_结束
    QRY_LOAD_ENDTIME = (By.XPATH, '//input[@name="ext-comp-3013"]')
    # 查询按钮
    BTN_LOAD_SEARCH = (By.XPATH, '(//table[@id="ext-comp-2160"]//button[contains(text(),"查询")])[7]')
    # 数据展示→用电异常
    # 用电异常
    BTN_ABNORMALELECTRICITY = (By.XPATH, '//span[contains(text(),"用电异常")]')
    # 电表
    SEL_ABNORMALELECTRICITY_ELECTRICITYMETER = (By.XPATH, '//input[@name="elecAlarm_meterCombox"]')
    # 查询日期_开始
    QRY_ABNORMALELECTRICITY_STARTTIME = (By.XPATH, '//input[@name="ext-comp-3055"]')
    # 查询日期_结束
    QRY_ABNORMALELECTRICITY_ENDTIME = (By.XPATH, '//input[@name="ext-comp-3056"]')
    # 查询按钮
    BTN_ABNORMALELECTRICITY_SEARCH = (By.XPATH, '(//table[@id="ext-comp-2160"]//button[contains(text(),"查询")])[8]')
