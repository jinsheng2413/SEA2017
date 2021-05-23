# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: ntp_server.py
@time: 2019/5/23 0023 8:56
@desc:
"""
from socket import *
import time
ip_port = ('127.0.0.1',8080)
buffer_size = 1024

udp_server = socket(AF_INET,SOCK_DGRAM)#数据报
udp_server.bind(ip_port) #绑定ip地址
while True:
    data,addr = udp_server.recvfrom(buffer_size) #收消息
    print(data)
    if not data:
        fmt = '%Y_%m_%d %X'
    else:
        fmt = data.decode('utf-8')

    back_time = time.strftime(fmt)
    udp_server.sendto(back_time.encode('utf-8'),addr) #发消息
