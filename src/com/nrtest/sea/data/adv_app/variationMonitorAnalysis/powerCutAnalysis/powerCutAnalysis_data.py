# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: powerCutAnalysis_data.py
@time: 2018/11/2 15:33
@desc:
"""


class PowerCutAnalysis_data:
    # 高级应用→配变监测分析→停电分析→有效停电事件查询
    ValidPowerCutEventQuery_para = '99925410'
    ValidPowerCutEventQuery_tabName = '有效停电事件查询'
    ValidPowerCutEventQuery_tabName_Detail = '有效停电明细'

    # 高级应用→配变监测分析→停电分析→终端停电事件查询
    TmnlPowerCutEventQuery_para = '99925420'
    TmnlPowerCutEventQuery_tabName = '终端停电统计'
    TmnlEventSendingFunction_tabName_Day = '日终端停电明细'
    TmnlPowerCutEventQuery_tabName_Month = '月终端停电明细'

    # 高级应用→配变监测分析→停电分析→智能表停电事件查询
    IntelligentMeterPowerCutEventQuery_para = '99925430'
    IntelligentMeterPowerCutEventQuery_tabName = '智能表停电统计'
    IntelligentMeterPowerCutEventQuery_tabName_Detail = '智能表停电明细'

    # 高级应用→配变监测分析→停电分析→停电监测→重要客户实时停电监测
    ImportantClientRealTimePowerCutMonitor_para = '99925441'
    ImportantClientRealTimePowerCutMonitor_tabName = '重要客户实时停电监测'
    ImportantClientHistoryPowerCutQuery_tabName = '重要客户历史停电查询'

    # 高级应用→配变监测分析→停电分析→停电监测→疑似区域停电监测
    SuspectedAreaPowerCutMonitor_para = '99925442'
    SuspectedAreaPowerCutMonitor_tabName = '疑似区域停电监测'
    SuspectedLinePowerCutMonitor_tabName = '疑似停电线路查询'
    SuspectedObjectPowerCutMonitor_tabName = '疑似停电对象查询'

    # 高级应用→配变监测分析→停电分析→表计实时停上电信息查询
    MeterRealTimePowerCutQuery_para = '99925470'

    # 高级应用→配变监测分析→停电分析→实时停电监测
    ReadTimePowerCutMonitor_para = '99925480'
    ReadTimePowerCutMonitor_tabName = '实时停电监测'
    ReadTimePowerCutMonitor_tabName_Detail = '实时停电明细'

    # 高级应用→配变监测分析→停电分析→历史停电事件查询
    HistoryPowerCutEventQuery_para = '99925490'
    HistoryPowerCutEventQuery_tabName = '停电事件统计'
    HistoryPowerCutEventQuery_tabName_Intelligent = '智能表停电事件查询'
    HistoryPowerCutEventQuery_tabName_Tmnl = '终端停电事件查询'

    # 高级应用→配变监测分析→停电分析→终端是否具备停上电事件上送功能
    TmnlEventSendingFunction_para = '99925450'
    TmnlEventSendingFunction_tabName = '终端是否具备停上电事件上送功能'
    TmnlEventSendingFunction_tabName_Detail = '终端是否具备停上电事件上送功能明细'

    # 高级应用→配变监测分析→停电分析→线路停电统计
    LinePowerCutStatistics_para = '99925460'
