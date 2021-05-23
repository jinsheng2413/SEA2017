# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: 验证客户端合法性-server.py
@time: 2019/5/30 0030 8:58
@desc:
"""
from socket import *
import hmac,os
secret_key = b'guochunbiao bang bang bang'
def conn_author(conn):
    """
    认证客户端合法性
    :param conn:
    :return:
    """
    print('开始验证连接的合法性')
    msg = os.urandom(32) #生成32位的随机数
    conn.sendall(msg)
    h = hmac.new(secret_key,msg)#加盐
    digest = h.digest()#得到他的数字形式
    respone = conn.recv(len(digest))
    return hmac.compare_digest(digest,respone)


def data_handle(conn,buffer_size=1024):
    if not conn_author(conn):
        print('链接不合法 关闭')
        conn.close()
        return
    print('连接合法  通信')
    while True:
        data = conn.recv(buffer_size)
        if not data:break
        conn.sendall(data.upper())

def server_handle(ip_port,buffer_siaze,backlog=5):
    """
    只处理连接
    :param ip_port:
    :param buffer_siaze:
    :param backlog:
    :return:
    """
    tcp_socket_server = socket(AF_INET,SOCK_STREAM)
    tcp_socket_server.bind(ip_port)
    tcp_socket_server.listen(backlog)
    while True:
        conn,addr = tcp_socket_server.accept()
        print('新链接[%s:%s]'%(conn,addr))
        data_handle(conn,buffer_size)

if __name__=='__main__':
    ip_port = ('127.0.0.1',8080)
    buffer_size = 1024
    server_handle(ip_port,buffer_size)
