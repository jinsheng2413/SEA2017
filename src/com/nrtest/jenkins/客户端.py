# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: 客户端.py
@time: 2019/5/21 0021 15:30
@desc:
"""
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8000)) # 拨通电话

phone.send('hello'.encode('utf-8'))#发消息
print('-----------.')
data = phone.recv(1024)
print('收到服务端发来的消息：', data)
