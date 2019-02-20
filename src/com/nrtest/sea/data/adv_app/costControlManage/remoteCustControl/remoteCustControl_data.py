# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: remoteCustControl_data.py
@time: 2018/9/29 0029 15:40
@desc:
"""


class RemoteCustControl_data:
    # 高级应用→费控管理→远程费控→远程费控执行统计
    prePaidStatus_para = '99922230'
    Tab_ByAction = '按指令执行统计'
    Tab_ByUser = '按用户执行统计'

    # 高级应用→费控管理→远程费控→新远程费控执行统计
    NewPrePaidStatus_para = '99922280'
    NewTab_ByAction = '按指令执行统计'
    NewTab_ByUser = '按用户执行统计'

    # 高级应用→费控管理→远程费控→专变用户远程费控执行
    CtrlExecutSpec_para = '99922220'

    # 高级应用→费控管理→远程费控→新专变用户远程费控执行
    para_NewSpecRemoteCtrlExecut = '99922240'
    para_NewSpecRemoteCtrlExecut_high_sheet = '高压用户跳闸控制列表'
    para_NewSpecRemoteCtrlExecut_high_info = '高压用户跳闸控制汇总信息'
    # 高级应用→费控管理→远程费控→新低压用户远程费控执行
    para_NewRemoteCtrlExecut = '99922250'
    para_NewRemoteCtrlExecut_low_sheet = '低压用户费控列表'
    para_NewRemoteCtrlExecut_low_info = '低压用户费控汇总信息'
