# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: socket_client_tcp.py
@time: 2019/5/23 0023 9:25
@desc:
"""
from socket import *
buffer_size = 1024
ip_port = ('127.0.0.1',8080)
udp_client = socket(AF_INET,SOCK_DGRAM)

while True:
    cmd = input('>>:').strip()
    if not cmd:continue
    if cmd == 'quit':break
    udp_client.sendto(cmd.encode('utf-8'),ip_port)
    cmd_res,addr = udp_client.recvfrom(buffer_size)
    print('命令执行的结果',cmd_res.decode('gbk'))


udp_client.close()