# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: synthQuery_data.py
@time: 2018/9/29 15:18
@desc:
"""


class SynthQuery_data:
    # 统计查询→综合查询→供电单位数据查询
    OrgNoDataQuery_para = '99941500'
    # 统计查询→综合查询→抄表段数据查询
    sectDataQuery_para = '99941600'
    sectDataQuery_tabName = '基本档案'
    sectDataQuery_tabName_data = '数据展示'
    # 统计查询→综合查询→批量数据查询
    BatchDataQuery_para = '99941700'

    # 统计查询→综合查询→全事件电表事件查询
    AllEventMeterEventQuery_para = '99941702'
    # 统计查询→综合查询→线路拓扑图
    LineTopologyDiagram_para = '99941A20'
    # 统计查询→综合查询→台区拓扑图
    TgTopologyDiagram_para = '99941B00'
    # 统计查询→综合查询→销户和拆表数据查询
    DisassemblyTableDataQuery_para = '99941704'
    # 统计查询→综合查询→抄表数据查询
    MeterDataQuery_para = '99941910'
    MeterDataQuery_detail_tab = '抄表明细'
    MeterDataQuery_count_tab = '抄表失败统计'
    MeterDataQuery_fialDetail_tab = '抄表失败明细'
    # 统计查询→综合查询→抄表成功率查询（河北）
    MeterSuccessRateQuery_para = '99941930'
    MeterSuccessRateQuery_tabName = '按地区、厂家统计'
    MeterSuccessRateQuery_tabName_time = '按时间统计'
    MeterSuccessRateQuery_tabName_huaBei = '按华北要求统计'
    MeterSuccessRateQuery_tabName_failed = '连续抄表失败明细'
    # 统计查询→综合查询→多表合一抄表数据查询
    MultipleTableDataQuery_para = '99941A00'
    MultipleTableDataQuery_tabName = '用户抄表数据'
    MultipleTableDataQuery_tabName_tmnl = '终端抄表数据'
    # 统计查询→综合查询→全事件配置率统计
    AllEventDistributionRateStatistics_para = '99941945'
    AllEventDistributionRateStatistics_tabName = '全事件配置率统计'
    AllEventDistributionRateStatistics_tabName_detail = '全事件未配置明细'
    # 统计查询→综合查询→巡检仪数据查询
    PatrolDataQuery_para = '99941K00'
    PatrolDataQuery_tabName = '基本档案'
    PatrolDataQuery_tabName_curve = '曲线数据'
    PatrolDataQuery_tabName_anomalous = '异常事件查询'
    PatrolDataQuery_tabName_current = '电流回路状态'
    PatrolDataQuery_tabName_contrast = '曲线对比'
    # 统计查询→综合查询→自动化抄表可用率
    AutomatedMeterAvailability_para = '99941C00'
    AutomatedMeterAvailability_tabName = '全项采集成功率'
    AutomatedMeterAvailability_tabName_detail = '全项失败明细'
    # 统计查询→综合查询→白名单查询
    WhiteListQuery_para = '99941O00'
    # 统计查询→综合查询→巡检仪综合查询
    PatrolIntegratedQuery_para = '99941S00'
    PatrolIntegratedQuery_tabName = '巡检仪运行指标'
    PatrolIntegratedQuery_tabName_detail = '巡检仪运行指标明细'
    # 统计查询→综合查询→四表合一抄表成功率
    FourTableMeterReadSuccessRate_para = '99941800'
    FourTableMeterReadSuccessRate_tabName = '四表合一抄表成功率'
    FourTableMeterReadSuccessRate_tabName_failed = '四表合一抄表失败明细'
    # 统计查询→综合查询→采集点综合查询
    CPSynthQuery_para = '99941D00'
    # 统计查询→综合查询→黑名单查询
    BlackListQuery_para = '99941P00'
    # 统计查询→综合查询→抄表数据查询（冀北）
    realData_para = '99941L00'
    realData_rdetail_tab = '抄表明细'
    realData_fdetail_tab = '抄表失败明细'
    # 统计查询→综合查询→掌机工单查询
    allCollectSuccessRate_para = '99941920'

    # 统计查询→综合查询→用户数据查询
    ConsDataQuery_para = '99941100'
    ConsDataQuery_tab_info = '基本档案'
    ConsDataQuery_tab_display = '数据展示'

    # 统计查询→综合查询→终端数据查询
    TmnlDataQuery_para = '99941200'
    TmnlDataQuery_Doc = '基本档案'
    TmnlDataQuery_DataDisp = '数据展示'

    # 统计查询--综合查询--配变数据查询
    CollcateDataQuery_para = '99941300'
    CollcateDataQuery_Doc = '基本档案'
    CollcateDataQuery_Data = '数据展示'

    # 统计查询--综合查询--线路数据查询
    lineDataQuery_para = '99941400'
    # 统计查询→综合查询→专公变明细查询(江西)
    FailListJx_para = '99941I00'
    # 统计查询--综合查询--专公变综合查询
    onlyChangeSysthesisQuery_para = '99941R00'
    onlyChangeSysthesisQuery_loadCount_tab = '负荷统计'
    onlyChangeSysthesisQuery_eleMap_tab = '电量曲线图'
    onlyChangeSysthesisQuery_dayReadData_tab = '日抄表数据'
    onlyChangeSysthesisQuery_loadDayData_tab = '负荷日数据'
    onlyChangeSysthesisQuery_realTtimeReadData_tab = '实时抄表数据'
    onlyChangeSysthesisQuery_tmnlEvent_tab = '终端事件'
    onlyChangeSysthesisQuery_cp_tab = '采集点信息'
    onlyChangeSysthesisQuery_cons_doc_tab = '用户档案'
    onlyChangeSysthesisQuery_TransLoadRateMonitor_tab = '变压器负载率监控'

    # 统计查询--综合查询--农排用户信息接入统计
    agriculturaiRowSta_para = '99941Q00'
    agriculturaiRowSta_stat = '农排用户信息接入统计'
    agriculturaiRowSta_detail = '农排用户接入明细'
    # 统计查询--综合查询--实时数据查询
    realtimeData_para = '99941M00'
    # 统计查询→综合查询→用户数据
    consDataQry_para = '99941110'
    consDataQry_file_tab = '基本档案'
    consDataQry_display_tab = '数据展示'
    # 统计查询→综合查询→抄表数据查询(国网)
    realTimeReadMeterQry_gw_para = '99941801'
    realTimeReadMeterQry_gw_detail = '抄表明细'
    realTimeReadMeterQry_gw_failstat = '抄表失败统计'
    realTimeReadMeterQry_gw_faildetail = '抄表失败明细'

    # 统计查询--综合查询--单户综合查询
    consIntrgratedQuery_para = '99941940'

    consIntrgratedQuery_dayDataQry_tab = '日抄表数据'
    consIntrgratedQuery_realTimeDataQry_tab = '实时抄表数据'
    consIntrgratedQuery_eleMap_tab = '电量曲线图'
    consIntrgratedQuery_tmnlEvent_tab = '终端事件'
    consIntrgratedQuery_cons_doc_tab = '用户档案'
    consIntrgratedQuery_cp_tab = '采集点信息'
    consIntrgratedQuery_LoadCurve_tab = '负荷曲线数据'
    consIntrgratedQuery_LoadStat_tab = '负荷统计'
    consIntrgratedQuery_LoadDay_tab = '负荷日数据'
    consIntrgratedQuery_dayCapacitor_tab = '测量点日电容器累计补偿的无功电能量'
    consIntrgratedQuery_monthFreeze_tab = '测量点月冻结视在功率越限及负载率'
    consIntrgratedQuery_phaseAngle_tab = '测量点电流电压相位角'
    # 统计数据
    consIntrgratedQueryMeasurementPointVoltage_tab = '测量点电压统计'
    consIntrgratedQueryMeasurementPointCurrentOverLimit_tab = '测量点电流越限统计'
    consIntrgratedQueryMeasurementPointTotalTime_tab = '测量点不平衡度越限累计时间统计'
    ConsIntrgratedQueryMeasurementPointTotalTime2_tab = '测量点功率因数区段累计时间统计'
    consIntrgratedQueryMeasurementPointTotalActivePower_tab = '测量点总及分相有功功率统计'
    consIntrgratedQueryMeasurementPointDcSimulation_tab = '测量点直流模拟量越限统计'
    consIntrgratedQueryMeasurementPointMaxNumAndTime_tab = '测量点最大需量及发生时间统计'
    consIntrgratedQueryMeasurementPointTmnlStat_tab = '终端统计数据'
    consIntrgratedQueryMeasurementPointSumGroupStat_tab = '总加组统计数据'
