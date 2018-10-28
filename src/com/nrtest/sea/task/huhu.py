# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: huhu.py
@time: 2018/8/26 0026 17:22
@desc:
"""
import os

path = "D:/pdg/"
dirs = os.listdir(path)
i = 0
for g in dirs:
    i = i + 1
    res = os.path.isfile(path + str(i) + ".jpg")
    if res is True:
        print(str(i) + ".jpg " + "已经存在")
        continue
