# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: fr.py
@time: 2018/12/18 0018 19:32
@desc:
"""
import os

path = r'D:\pythonworkspace\SEA2017\src\com\nrtest\sea\testcase\base_app\dataGatherMan\gatherQualityAnalyze'


def list_dir(path):
    lis = []
    print('--------------------')
    for root, dirs, files in os.walk(path):
        # for name in dirs:
        #     lis.append(os.path.join(root,name))
        for name in files:
            if name.startswith('test'):
                lis.append(os.path.join(root, name))
                # print(type(os.path.join(root, name)))
    lis2 = set([])
    for elePath in lis:
        with open(elePath, 'rt', encoding='utf-8') as data:
            if '郭春彪' in ''.join(data.readlines()):
                lis2.add(elePath)

    return lis


print('++++++++++++++', list_dir(r'D:\pythonworkspace\SEA2017\src\com\nrtest\sea\testcase\adv_app\lineLossAnalysis'))
