# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: fcntl.py
@time: 2019/5/27 0027 16:30
@desc:
"""


def fcntl(fd, op, arg=0):
    return 0


def ioctl(fd, op, arg=0, mutable_flag=True):
    if mutable_flag:
        return 0
    else:
        return ""


def flock(fd, op):
    return


def lockf(fd, operation, length=0, start=0, whence=0):
    return


