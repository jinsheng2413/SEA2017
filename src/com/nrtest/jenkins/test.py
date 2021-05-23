# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: test.py
@time: 2019/4/20 0020 7:53
@desc:
"""
from socket import *
cs = socket() #创建客户端套字接
cs.connect() #尝试连接服务器
loop: #通讯循环
  cs.recv()/cs.send()  #对话（接受/发送）
cs.close() #关闭客户端套字接






