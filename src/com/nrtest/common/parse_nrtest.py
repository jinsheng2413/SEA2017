# -*- coding:utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: parse_nrtest.py
@time: 2018-06-05 1:46
@desc: 参考网页https://blog.csdn.net/shortwall/article/details/78615368
    [My Section]
    foodir: %(dir)s/whatever
    dir=frob

    %(dir)s 会被frob代替。
"""
import configparser
import os
import platform


class ParseNrTest(object):
    @staticmethod
    def pattern():
        return r'\\' if platform.system() == 'Windows' else r'/'

    def __init__(self, file=None):
        self.parse = configparser.ConfigParser()  # 注意大小写

        # 获取当前文件的上一级目录,并定位setup路径
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) \
               + self.pattern()[0] + ("setup") + self.pattern()[0]

        file = path + ("nari_test.conf" if file is None else file)
        # a = os.path.abspath(file)
        self.parse.read(file, encoding='utf-8')  # 配置文件的路径

    def getSections(self):
        """
            返回可用的section的列表;默认section不包括在列表中
        :return:
        """
        return self.parse.sections()

    #
    def getSection(self, section):
        """
            返回给定section中每个选项的元组对象(name, value)对的列表。
        :param section:
        :return:
        """
        return self.parse.items(section)

    def get(self, section, key):
        """
            为指定的section获取一个选项值。
        :param section:
        :param key:
        :return:
        """
        return self.parse.get(section, key)

    def getInt(self, section, key):
        """
            指定section中的选项强制转换为整数
        :param section:
        :param key:
        :return:
        """
        return self.parse.getint(section, key)

    def getBoolean(self, section, key):
        """
            强制转换为布尔型，”1”, “yes”, “true”, and “on”, 转换为True，
                          ”0”, “no”, “false”, and “off”, 转换为False. 其他返回ValueError.
        :param section:
        :param key:
        :return:
        """
        return self.parse.getboolean(section, key)

    def getOptions(self, section):
        """
            提取某section下的键值KEY（等号左边）
        :param section:
        :return:
        """
        return self.parse.options(section)

    def getSectionVals(self, section, is_list=True):
        """
            提取某section下的键值值（等号右边边）
        :param section:
        :param is_list: 默认返回LIST值，其他返回元组
        :return:
        """
        values = []
        options = self.getOptions(section)
        for option in options:
            values.append(self.get(section, option))
        return values if is_list else tuple(values)


if __name__ == '__main__':
    nrTest = ParseNrTest()
    print(nrTest.pattern())
