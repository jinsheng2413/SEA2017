# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: createFile.py
@time: 2018/11/6 0006 9:21
@desc:
"""


class Create:
    def ctInputStr(self, name, chinese):
        st = 'QRY_{0}  = (By.XPATH,"//div[@class=\"x-form-item \"]//label[contains(text(),\'{1}\')]/../../div[1]/div[1]//input")'.format(
            name, chinese)
        return st

    # def InputSel(self,name,ch):

    def op(self):
        f = open(h, 'w')
        f.write('------------------------------------')
        print(h)
        f.close()
