# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: script_check.py
@time: 2019-01-29 22:22
@desc:
"""
import codecs
import os

from com.nrtest.common.setting import Setting


def find_not_equal_input(dirname):
    """
    检查self.inputXXX_abc[para['ABC'])方法名是否与参数一致
    :param dirname:
    """
    filelistlog = Setting.LOG_PATH + "filelistlog.log"  # 保存文件路径
    postfix = set(['py'])  # 设置要保存的文件格式
    files = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            if apath.split('\\')[-1].lower().startswith('test_') and apath.split('.')[-1] in postfix:  # 匹配后缀，只保存所选的文件格式。若要保存全部文件，则注释该句
                package = apath.split('src\\')[-1]
                with codecs.open(apath, 'r', 'utf-8') as file:
                    lines = file.readlines()
                    defs = []
                    for i, line in enumerate(lines):
                        temp = line.strip().replace(' ', '')
                        if temp.startswith('self.input'):
                            try:
                                ls = temp.split('\'')
                                para = ls[1].lower()
                                b = ls[0].split('(')[0]
                                c = b[b.find('_') + 1:].strip()
                                if c != para:
                                    defs.append(temp + '\r')
                            except:
                                defs.append('~~~~~' + temp + '\r')
                                break
                if bool(defs):
                    with codecs.open(filelistlog, 'a+', encoding='utf-8') as fo:
                        fo.write('\r********')
                        fo.write(package + '\r')
                        fo.writelines(defs)
                        fo.write('\r')


if __name__ == '__main__':
    # # 指定根目录
    # dirpath = os.path.dirname(os.path.realpath(__file__))
    find_not_equal_input(r'D:\PycharmProjects\SEA2017\src\com\nrtest\sea\testcase')
