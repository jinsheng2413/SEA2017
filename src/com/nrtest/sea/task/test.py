# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test.py
@time: 2018/8/26 0026 17:55
@desc:
'''
import os
from time import sleep

import requests

fobj = open('C:/Users/Administrator/Desktop/接口/tte.txt', 'r')
i = 0
for eachline in fobj:
    i = i + 1
    path = "D:/pdg/"
    # path存放图片的路径
    res = os.path.isfile(path + str(i) + ".jpg")
    if res is True:
        print(path + str(i) + ".jpg " + "已经存在")
        continue
    name = i
    r = requests.get(eachline)  # create HTTP response object
    with open(path + str(i) + '.jpg', 'wb') as f:
        f.write(r.content)
    # 延迟时间
    sleep(2)
