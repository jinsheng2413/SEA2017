# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: 服务端.py
@time: 2019/5/21 0021 15:30
@desc:
"""
import socket
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#socket.SOCK_STREAM代表tcp协议，socket.AF_INET基于网络层 买手机
phone.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
phone.bind(('127.0.0.1',8000))#绑定电话卡
phone.listen(5)#代表只能有5个电话链接////开机

conn,addr = phone.accept()#收到一个来链接和电话

msg = conn.recv(1024)#收消息
print('客户端发来的信息是：',msg.decode())
conn.send(msg.upper())#发消息

conn.close()
phone.close()