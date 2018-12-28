# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: utils.py
@time: 2018-12-28 11:34
@desc:
"""
import re


class Utils:
    @staticmethod
    def replace_chrs(src, pattern='\r\n\t'):
        """
        # 去除\r\n\t字符
        s = '\r\nabc\t123\nxyz'
        print(re.sub('[\r\n\t]', '', s))
        :param src:
        :return:
        """
        # # % 希望使用左右括号、空格以及*分割
        # # % 核心两句代码如下
        # # % 正则表达式切分字符串，但会有空串出现，注意中间需要转义
        # temp = re.split('\(|\)| |\*',src)
        # # %使用过滤器筛掉空串得到了迭代器，再重新构造出列表
        # temp = [item for item in filter(lambda x:x != '', temp)]
        # return ''.join(temp)
        return re.sub('[' + pattern + ']', '', src.strip())
