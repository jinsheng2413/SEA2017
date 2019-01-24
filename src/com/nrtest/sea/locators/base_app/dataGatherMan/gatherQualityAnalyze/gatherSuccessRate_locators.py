# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: GatherSuccessRateLocators.py
@time: 2018-09-17 13:30
@desc:
"""

from selenium.webdriver.common.by import By


# 基本应用→数据采集管理→采集质量分析→采集成功率
# 采集成功率→采集成功率
class GatherSuccessRateLocators:
    # 用户类型
    CONS_TYPE = (By.XPATH, '//label[text()="用户类型"]/../div/div/img')
    CONS_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[6]/div[%s]')
    # 通信方式
    COMM_MODE = (By.XPATH, '//label[text()="通信方式"]/../div/div/img')
    COMM_MODE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端厂家
    TMNL_FACTORY = (By.XPATH, '//label[text()="终端厂家"]/../div/div/img')
    TMNL_FACTORY_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 计量方式
    MEAS_MODE = (By.XPATH, '//label[text()="计量方式"]/../div/div/img')
    MEAS_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 所属区域
    AREA = (By.XPATH, '//label[text()="所属区域"]/../div/div/img')
    AREA_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[4]/div[%s]')
    # 芯片厂家
    CHIP_FACTORY = (By.XPATH, '//label[text()="芯片厂家"]/../div/div/img')
    CHIP_FACTORY_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[5]/div[%s]')
    # 查询日期开始
    START_DATE = (By.XPATH, '//label[text()="开始时间"]/../div/div/input')
    # 查询日期结束
    END_DATE = (By.XPATH, '//label[text()="结束时间"]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//button[contains(text(),"查询")]')

    # 【JS属性】
    # 查询日期开始，删除readonly属性
    START_DATE_JS = 'document.getElementsByTagName("input")[34].removeAttribute("readonly");'
    # 查询日期结束，删除readonly属性
    END_DATE_JS = 'document.getElementsByTagName("input")[35].removeAttribute("readonly");'

    # 【校验区】
    # 第一个单位
    BTN_FIRST_UNIT = (By.XPATH, '//a[text()="唐山供电公司"]')


# 采集成功率→采集成功率统计
class GatherSuccessRateStatLocators:
    # 用户类型
    CONS_TYPE = (By.XPATH, '(//label[text()="用户类型"])[2]/../div/div/img')
    CONS_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[5]/div[%s]')
    # 通信方式
    COMM_MODE = (By.XPATH, '(//label[text()="通信方式"])[2]/../div/div/img')
    COMM_MODE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端厂家
    TMNL_FACTORY = (By.XPATH, '(//label[text()="终端厂家"])[2]/../div/div/img')
    TMNL_FACTORY_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 芯片厂家
    CHIP_FACTORY = (By.XPATH, '(//label[text()="芯片厂家"])[2]/../div/div/img')
    CHIP_FACTORY_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 通讯规约
    TMNL_PROTOCOL = (By.XPATH, '//label[text()="通讯规约"]/../div/div/img')
    TMNL_PROTOCOL_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[4]/div[%s]')
    # 查询日期
    DATE = (By.XPATH, '//input[@id="readDate"]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//table[@id="readSuccessRateQueryBtn"]')

    # 【JS属性】
    # 采集成功率统计，查询日期，删除readonly属性
    DATE_JS = 'document.getElementById("readDate").removeAttribute("readonly");'

    # 【校验区】
    # 采集成功率统计
    CHECK_FIRST = (By.XPATH, '//div[text()="唐山供电公司(直属)"]')


# 采集成功率→数据采集成功率明细
class GatherSuccessRateDetailLocators:
    # 用户类型
    CONS_TYPE = (By.XPATH, '(//label[text()="用户类型"])[2]/../div/div/img')
    CONS_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[4]/div[%s]')
    # 芯片厂家
    CHIP_FACTORY = (By.XPATH, '(//label[text()="芯片厂家"])[2]/../div/div/img')
    CHIP_FACTORY_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 终端厂家
    TMNL_FACTORY = (By.XPATH, '(//label[text()="终端厂家"])[2]/../div/div/img')
    TMNL_FACTORY_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 通信方式
    COMM_MODE = (By.XPATH, '(//label[text()="通信方式"])[2]/../div/div/img')
    COMM_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 用户编号
    CONS_NO = (By.XPATH, '//input[@name="consNo"]')
    # 终端地址
    TMNL_ADDR = (By.XPATH, '//input[@name="tmnlAddr"]')
    # 查询日期
    DATE = (By.XPATH, '//input[@id="failDetail_statDate"]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '//table[@id="gatherFailDetailQueryBtn"]')

    # 【JS属性】
    # 采集成功率明细，查询日期，删除readonly属性
    DATE_JS = 'document.getElementById("failDetail_statDate").removeAttribute("readonly");'

    # 【校验区】
    # 第一行数据
    CHECK_FIRST = (By.XPATH, '//div[@class="x-panel-bwrap "]//div[@class="x-grid3-body"]')


# 采集成功率→连续抄表失败明细
class ContinuousFalseDetailLocators:
    # 用户类型
    CONS_TYPE = (By.XPATH, '(//label[text()="用户类型"])[2]/../div/div/img')
    CONS_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 运行状态
    RUN_STATUS = (By.XPATH, '//label[text()="运行状态"]/../div/div/img')
    RUN_STATUS_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 查询日期
    DATE = (By.XPATH, '//label[text()="日期"]/../div/div/input')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[text()="查询"])[2]')

    # 【JS属性】
    # 采集成功率明细→连续抄表失败明细，查询日期，删除readonly属性
    DATE_JS = 'document.getElementsByTagName("input")[50].removeAttribute("readonly");'


# 基本应用→数据采集管理→采集质量分析→采集成功率→按时间统计
class GatherSuccessRateTimeLocators:
    # 查询日期，开始
    START_DATE = (By.XPATH, '//input[@name="msq_startDate"]')
    # 查询日期，结束
    END_DATE = (By.XPATH, '//input[@name="msq_endDate"]')
    # 用户类型
    CONS_TYPE = (By.XPATH, '(//label[text()="用户类型"])[2]/../div/div/img')
    CONS_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[4]/div[%s]')
    # 用户范围
    CONS_RANGE = (By.XPATH, '//label[text()="用户范围"]/../div/div/img')
    CONS_RANGE_VALUE = (By.XPATH, '//div[@class="x-combo-list-inner"]/div[%s]')
    # 停电标志
    POWER_CUT_FLAG = (By.XPATH, '//label[text()="停电标志"]/../div/div/img')
    POWER_CUT_FLAG_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[2]/div[%s]')
    # 终端类型
    TMNL_TYPE = (By.XPATH, '//label[text()="终端类型"]/../div/div/img')
    TMNL_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[5]/div[%s]')
    # 通信方式
    COMM_MODE = (By.XPATH, '(//label[text()="通信方式"])[2]/../div/div/img')
    COMM_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[6]/div[%s]')
    # 规约类型
    PROTOCOL_TYPE = (By.XPATH, '//label[text()="规约类型"]/../div/div/img')
    PROTOCOL_TYPE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[7]/div[%s]')
    # 计量方式
    MEAS_MODE = (By.XPATH, '(//label[text()="计量方式"])[2]/../div/div/img')
    MEAS_MODE_VALUE = (By.XPATH, '(//div[@class="x-combo-list-inner"])[3]/div[%s]')
    # 查询按钮
    BTN_SEARCH = (By.XPATH, '(//button[contains(text(),"查询")])[2]')

    # 【JS属性】
    # 按时间统计,查询日期开始，删除readonly属性
    START_DATE_JS = 'document.getElementsByName("msq_startDate")[0].removeAttribute("readonly");'
    # 按时间统计,查询日期结束，删除readonly属性
    END_DATE_JS = 'document.getElementsByName("msq_endDate")[0].removeAttribute("readonly");'
