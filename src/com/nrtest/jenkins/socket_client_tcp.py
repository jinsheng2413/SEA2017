# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: socket_client_tcp.py
@time: 2019/5/23 0023 9:25
@desc:
"""
# from socket import *
#
# ip_port = ('127.0.0.1',8080)
# buffer_size = 1024
# tcp_client = socket(AF_INET,SOCK_STREAM)
# tcp_client.connect(ip_port)
# while True:
#     cmd = input('>>:').strip()
#     if not cmd:continue
#     if cmd == 'quit':break
#     tcp_client.send(cmd.encode('utf-8'))
#     cmd_res = tcp_client.recv(buffer_size)
#     print('命令执行的结果',cmd_res.decode('gbk'))
#
#
# tcp_client.close()
#解决粘包版
# from socket import *
#
# ip_port = ('127.0.0.1',8080)
# buffer_size = 1024
# tcp_client = socket(AF_INET,SOCK_STREAM)
# tcp_client.connect(ip_port)
# while True:
#     cmd = input('>>:').strip()
#     if not cmd:continue
#     if cmd == 'quit':break
#     tcp_client.send(cmd.encode('utf-8'))
#     #解决粘包
#     length = tcp_client.recv(buffer_size)
#     tcp_client.send(b'ready')
#
#     length = int(length.decode('utf-8'))
#     recv_size = 0
#     recv_msg = b''
#     while recv_size<length:
#
#          recv_msg += tcp_client.recv(buffer_size)
#          recv_size = len(recv_msg)
#     print('命令执行的结果',recv_msg.decode('gbk'))
#
#
# tcp_client.close()
#------------------------------------------------------------------------------------------------------------------------
from socket import *
from functools import partial
import struct
import json
ip_port = ('127.0.0.1',8080)
buffer_size = 1024
tcp_client = socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)
while True:
    cmd = input('>>:').strip()
    if not cmd:continue
    if cmd == 'quit':break
    tcp_client.send(cmd.encode('utf-8'))
    #解决粘包
    length_tuple = tcp_client.recv(4)
    print('--------------')

    recv_msg =''.join(iter(partial(tcp_client.recv,buffer_size),b''))
    print('命令执行的结果',recv_msg)


tcp_client.close()