# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: 验证客户端合法性-client.py
@time: 2019/5/30 0030 8:58
@desc:
"""
from socket import *
import hmac,os
secret_key = b'guochunbiao bang bang bang'
def conn_author(conn):
    """
    认证服务器合法性
    :param conn:
    :return:
    """
    print('开始验证连接的合法性')
    msg = conn.recv(32)
    h = hmac.new(secret_key,msg)#加盐
    digest = h.digest()#得到他的数字形式
    conn.sendall(digest)

def client_handle(ip_port,buffer_size= 1024):
    tcp_socket_client = socket(AF_INET,SOCK_STREAM)
    tcp_socket_client.connect(ip_port)

    conn_author(tcp_socket_client)

    while True:
        data = input('>>>:').strip()
        if not data:continue
        if data == 'quit':break

        tcp_socket_client.sendall(data.encode('utf-8'))
        respone = tcp_socket_client.recv(buffer_size)
        print(respone.decode('utf-8'))
    tcp_socket_client.close()
if __name__ == '__main__':
    ip_port = ('127.0.0.1',8080)
    buffer_size = 1024
    client_handle(ip_port,buffer_size)

