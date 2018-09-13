# -*- coding:utf-8 -*-

'''
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: dictionary.py
@time: 2018/9/12 0012 8:56
@desc:
'''

class Dict(dict):
    def __missing__(self, key):
        return ''