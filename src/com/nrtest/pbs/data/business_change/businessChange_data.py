# -*- coding: utf-8 -*-

"""
@author: 韩笑
@license: (C) Copyright 2018, Nari.
@file: businessChange_data.py
@time: 2019-03-11 10:48
@desc:
"""


class BusinessChange_data:
    # 业务变更→更换电表
    ChangeTableOperate_para = '0000501'
    ChangeTableOperate_tabName_operate = '换表操作'
    ChangeTableOperate_tabName_record = '换表记录'

    # 业务变更→满码处理
    FullSizeProcess_para = '0000502'
    FullSizeProcess_tabName_operate = '满码处理操作'
    FullSizeProcess_tabName_record = '满码记录查询'
    FullSizeProcess_tabName_qry = '满码处理查询'

    # 业务变更→更换CTPT
    ChangeCTPT_para = '0000503'
    ChangeCTPT_tabName_operate = '换CTPT操作'
    ChangeCTPT_tabName_record = '换CTPT记录'

    # 业务变更→手工录入计划值
    HandworkEnterPlanValue_para = '0000504'

    # 业务变更→重处理
    AgainDispose_para = '0000505'

    # 业务变更→重计算
    AgainCount_para = '0000506'

    # 业务变更→数据修正
    DataAmend_para = '0000507'
    DataAmend_tabName_operate = '数据修正操作'
    DataAmend_tabName_record = '数据修正记录'

    # 业务变更→实用工具
    PracticalTool_para = '0000508'

    # 业务变更→电量追补
    PowerRepair_para = '0000509'