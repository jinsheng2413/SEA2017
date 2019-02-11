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
    检查self.inputXXX_abc(para['ABC'])方法名是否与参数一致
    正解：self.inputStr_cons_no(para['CONS_NO'])
    :param dirname:
    """
    filelistlog = Setting.LOG_PATH + "filelistlog.log"  # 保存文件路径
    postfix = set(['py'])  # 设置要保存的文件格式
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


def find_not_startwith_test(dirname):
    """
    检查testcase路径下是否存在不符合test_打头的.py文件
    :param dirname:
    :return:
    """
    filelistlog = Setting.LOG_PATH + "filelistlog.log"  # 保存文件路径
    postfix = set(['py'])  # 设置要保存的文件格式
    exclude_files = ['bg.py', 'demo.py', 'gt.py', 'pbs5000.py', '__init__.py']
    find_file_list = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            if not filename.startswith('test_') \
                    and filename not in exclude_files \
                    and filename.split('.')[-1] in postfix:  # 匹配后缀，只保存所选的文件格式。若要保存全部文件，则注释该句
                find_file_list.append(os.path.join(maindir, filename) + '\r')

    if bool(find_file_list):
        with codecs.open(filelistlog, 'a+', encoding='utf-8') as fo:
            fo.writelines(find_file_list)


if __name__ == '__main__':
    # # 指定根目录
    # dirpath = os.path.dirname(os.path.realpath(__file__))
    dirpath = r'D:\PycharmProjects\SEA2017\src\com\nrtest\sea\testcase'
    find_not_equal_input(dirpath)
    # find_not_startwith_test(dirpath)
