# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: fr.py
@time: 2019/5/17 0017 11:17
@desc:
"""
class Staticmethod:
    def __init__(self,func):
        self.func = func
    def __get__(self, instance, owner):
         def wrapper(*args,**kwargs):
             print('这里可以添加功能')
             return self.func(*args,**kwargs)

         return wrapper
class Room:
  style = '别墅'
  def __init__(self,name,owner,width,length):
    self.name = name
    self.owner = owner
    self.width = width
    self.length = length

  @Staticmethod
  def shower(op):
    print("洗澡")
    print(op)

Room.shower('323')
r1 = Room('别墅','alex',10,10)
r1.shower('asxas')  #这么调用也没有问题


