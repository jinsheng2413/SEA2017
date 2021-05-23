# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: socket_server_tcp.py
@time: 2019/5/23 0023 9:25
@desc:
"""
# from socket import *
# import subprocess
# ip_port = ('127.0.0.1',8080)
# buffer_size = 1024
# tcp_server = socket(AF_INET,SOCK_STREAM)
# tcp_server.bind(ip_port)
# tcp_server.listen(5)
# while True:
#     conn,addr = tcp_server.accept()
#     print('新的客户端连接',addr)
#     while True:
#      #收
#      try:
#         cmd = conn.recv(buffer_size)
#         if not cmd:break
#         print('收到的客户端命令',cmd)
#         #执行命令，得到命令运行的结果cmd_res
#         res = subprocess.Popen(cmd.decode('utf-8'),shell=True,
#                                stdout=subprocess.PIPE,
#                                stderr=subprocess.PIPE,
#                                stdin=subprocess.PIPE)
#         err = res.stderr.read()
#         if  err:
#             cmd_res = err
#         else:
#             cmd_res = res.stdout.read()
#         if not cmd_res:
#             cmd_res = '执行成功'.encode('gbk')
#         conn.send(cmd_res)
#      except BaseException as e:
#          print(e)
#          break
#     conn.close()
#
# # tcp_server.close()
#low版解决粘包版
# from socket import *
# import subprocess
# ip_port = ('127.0.0.1',8080)
# buffer_size = 1024
# back_log=5
#
# tcp_server = socket(AF_INET,SOCK_STREAM)
# tcp_server.bind(ip_port)
# tcp_server.listen(back_log)
# while True:
#     conn,addr = tcp_server.accept()
#     print('新的客户端连接',addr)
#     while True:
#      #收
#      try:
#         cmd = conn.recv(buffer_size)
#         if not cmd:break
#         print('收到的客户端命令',cmd)
#         #执行命令，得到命令运行的结果cmd_res
#         res = subprocess.Popen(cmd.decode('utf-8'),shell=True,
#                                stderr=subprocess.PIPE,
#                                stdout=subprocess.PIPE,
#                                stdin=subprocess.PIPE)
#         err = res.stderr.read()
#         if  err:
#             cmd_res = err
#         else:
#             cmd_res = res.stdout.read()
#         if not cmd_res:
#             cmd_res = '执行成功'.encode('gbk')
#         length = len(cmd_res)
#         conn.send(str(length).encode('utf-8'))
#         client_ready = conn.recv(buffer_size)
#         if client_ready == b'ready':
#
#             conn.send(cmd_res)
#
#      except BaseException as e:
#          print(e)
#          break
    # conn.close()

from socket import *
import struct
import subprocess
ip_port = ('127.0.0.1',8080)
buffer_size = 1024
back_log=5

tcp_server = socket(AF_INET,SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)
while True:
    conn,addr = tcp_server.accept()
    print('新的客户端连接',addr)
    while True:
     #收
     try:
        cmd = conn.recv(buffer_size)
        if not cmd:break
        print('收到的客户端命令',cmd)
        #执行命令，得到命令运行的结果cmd_res
        res = subprocess.Popen(cmd.decode('utf-8'),shell=True,
                               stderr=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE)
        err = res.stderr.read()
        if  err:
            cmd_res = err
        else:
            cmd_res = res.stdout.read()
        if not cmd_res:
            cmd_res = '执行成功'.encode('gbk')
        length = len(cmd_res)
        data_length = struct.pack('i',length)
        conn.send(data_length)
        conn.send(cmd_res)

     except BaseException as e:
         print(e)
         break
    conn.close()
