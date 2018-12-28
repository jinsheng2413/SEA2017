# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: gh.py
@time: 2018/12/25 0025 13:39
@desc:
"""

# 匿名函数，想要调用必须赋一个变量
func = lambda x, y: x / y if x > y else x * y  # 匿名函数最多只支持三元运算，再复杂的判断不支持

print(func(3, 8))
print(func(16, 8))
