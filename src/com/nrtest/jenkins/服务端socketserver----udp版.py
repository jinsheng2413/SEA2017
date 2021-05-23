# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: 服务端socketserver版.py
@time: 2019/5/29 0029 10:59
@desc:
"""
import socketserver
ip_port = ('127.0.0.1',8080)
buffer_size = 1024
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)#(data,self.socket),client_addr
        print('受到客户端的消息是',self.request[0])
        self.request[1].sendto(self.request[0].upper(),self.client_address)


if __name__=='__main__':
    s = socketserver.ThreadingUDPServer(ip_port,MyServer)#多线程
    #s = socketserver.ForkingTCPServer(ip_port, MyServer)#多进程
    s.serve_forever()
