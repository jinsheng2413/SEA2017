# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: socket_server_tcp.py
@time: 2019/5/23 0023 9:25
@desc:
"""
from socket import *
import subprocess
ip_port = ('127.0.0.1',8080)
buffer_size = 1024
udp_server = socket(AF_INET,SOCK_DGRAM)
udp_server.bind(ip_port)

while True:

    cmd,addr =  udp_server.recvfrom(buffer_size)
    # 执行命令，得到命令运行的结果cmd_res
    res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           stdin=subprocess.PIPE)
    err = res.stderr.read()
    if err:
        cmd_res = err
    else:
        cmd_res = res.stdout.read()
    if not cmd_res:
        cmd_res = '执行成功'.encode('gbk')
    udp_server.sendto(cmd_res,addr)