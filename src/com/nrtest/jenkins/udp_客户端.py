# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: udp_客户端.py
@time: 2019/5/23 0023 8:35
@desc:
"""
from socket import *
ip_port = ('127.0.0.1',8080)
buffer_size = 1024

udp_client = socket(AF_INET,SOCK_DGRAM)
while True:
    msg = input('>>:').strip()
    udp_client.sendto(msg.encode('utf-8'),ip_port)
    data,addr = udp_client.recvfrom(buffer_size)
    print(data.decode('utf-8'))

