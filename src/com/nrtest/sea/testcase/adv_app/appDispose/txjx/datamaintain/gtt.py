# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: gtt.py
@time: 2018/12/4 0004 16:39
@desc:
"""
str = []
en = []

i = 0
l = 0
res = open(
    'D:/pythonworkspace/SEA2017/src/com/nrtest/sea/testcase/adv_app/appDispose/txjx/datamaintain/test_CheckpointdataPage.py',
    'r', encoding='utf-8')
for item in res.readlines():
    print(item)
    if i == 1 and l != 1:
        if '#' in item and '查询按钮' not in item:
            str.append((item[item.index('#') + 1:])[:-1].replace(' ', ''))
        if 'input' in item:
            en.append(item[item.index("[") + 2:item.index("]") - 1])
    if 'query' in item:
        i = 1
    if 'btn_' in item:
        l = 1

result = dict(zip(en, str))
print(result)
# y.update(result)
