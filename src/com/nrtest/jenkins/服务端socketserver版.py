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
        print('conn is:',self.request)#conn
        print('addr is:',self.client_address)#addr

        while True:
           try:

                #收消息
                data = self.request.recv(buffer_size)
                if not data:break
                print('受到客户端的消息是',data)

                #发消息
                self.request.sendall(data.upper())
           except Exception as e:
               print(e)
if __name__=='__main__':
    s = socketserver.ThreadingTCPServer(ip_port,MyServer)#多线程
    #s = socketserver.ForkingTCPServer(ip_port, MyServer)#多进程
    s.serve_forever()
