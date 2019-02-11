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

    @staticmethod
    def map_module(package, file_name):
        """
        根据package与类文件，引入模块
        :param package: 类路径
        :param file_name: 类存放文件名
        :return:
        """
        module_name = file_name.split('.')[0]
        moduleObj = __import__(package + '.' + module_name, fromlist=True)
        return moduleObj

    @staticmethod
    def map_module_by_file_path(file_path):
        """
        根据package与类文件，引入模块
        :param file_path: 用例文件路径：package + file_name, 中间用.分割
        :return:
        """
        path = file_path[:-3] if file_path.endswith('.py') else file_path
        path = path.replace('/', '.')
        moduleObj = __import__(path, fromlist=True)
        return moduleObj

    @staticmethod
    def map_class(package, file_name, class_name, instance=True):
        """
        根据package与类文件，导入class对象
        例如，直接实例化类对象，然后调用对象函数
        testClass = Utils.map_class(package, file_name, 'TestClass')
        testClass.test_me()

        :param package: 类路径
        :param file_name: 类存放文件名
        :param class_name: class对象名
        :param instance:True-实例化类为对象实例，False-类对象
        :return:
        """
        module = Utils.map_module(package, file_name)
        if instance:
            # 导入并实例化对象
            return getattr(module, class_name)()
        else:
            # 只导入对象
            return getattr(module, class_name)

    @staticmethod
    def map_class_By_file_path(file_path, class_name, instance=True):
        """
        根据package与类文件，导入class对象
        :param package: 类路径
        :param file_name: 类存放文件名
        :param class_name: class对象名
        :return:
        """
        path = file_path[:-3] if file_path.endswith('.py') else file_path
        path = path.replace('/', '.')
        module = Utils.map_module_by_file_path(path)
        if instance:
            # 导入并实例化对象
            return getattr(module, class_name)()
        else:
            # 只导入对象
            return getattr(module, class_name)

    @staticmethod
    def map_class_by_module(module, class_name, instance=False):
        """
        根据package与类文件，导入class对象
        :param module: 模块实例
        :param class_name: class对象名
        :return:
        """
        if instance:
            # 导入并实例化对象
            return getattr(module, class_name)()
        else:
            # 只导入对象
            return getattr(module, class_name)
