# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: update_testpy.py
@time: 2018-12-19 15:15
@desc:
"""

import codecs
import os

from com.nrtest.common.setting import Setting

menu_code = ["\r        # 注册菜单\r",
             "        self.menu_name = para['MENU_NAME']\r",
             "\r"]
test_funs = [
    '\r',
    '    def assert_query_result(self, para):\r',
    '        """\r',
    '        查询结果校验（包括跳转）\r',
    '        :param para:\r',
    '        """\r',
    '        self.assertTrue(self.check_query_result(para))\r',
    '\r',
    '    def assert_query_criteria(self, para):\r',
    '        """\r',
    '        查询条件校验\r',
    '        :param para:\r',
    '        """\r',
    '        result = self.check_query_criteria(para)\r',
    '        self.assertTrue(result)\r',
    '\r',
    '    @BeautifulReport.add_test_img()\r',
    '$1',
    '    def test_query(self, para):\r',
    '        self.start_case(para)\r',
    '        self.query(para)\r',
    '        self.assert_query_result(para)\r',
    '        self.end_case(para)\r',
    '\r',
    '    @BeautifulReport.add_test_img()\r',
    '$2, valCheck=True))\r',
    '    def _test_checkValue(self, para):\r',
    '        self.start_case(para)\r',
    '        self.query(para)\r',
    '        self.assert_query_criteria(para)\r',
    '        self.end_case(para)\r']


def append_comment(line):
    temp = ''
    while True:
        pos = line.find('    ')  # 查找四个空字符的行
        if pos > -1:
            temp += line[:pos + 4]
            line = line[pos + 4:]
        else:
            break
    pos = len(temp)
    temp = temp + '# ' + line
    return temp, pos


def upgrade_test_file(file_name):
    """
    刷新test_query方法的测试用例
    :param file_name:
    """

    # dirname = os.path.dirname(file_name)
    # temp_test_logfile = dirname + "\\temp_test.py"  # 保存文件路径
    temp_test_logfile = file_name.split('.')[0] + '.log'
    # print (temp_test_pyfile)
    comments = ['"""', "'''"]
    is_reg_menu = True
    is_deal_test = False
    find_comment = False
    find_query = False
    head = []
    end = []
    doc = []
    with codecs.open(file_name, 'r', 'utf-8') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            line = (lines[i])[:-1]  # 去除行尾的\n符
            temp = line.strip().lower()

            if is_reg_menu:
                head.append(line)
                if find_query == False and temp.startswith('def') and temp.find('query') > 0:
                    find_query = True
                if find_query:
                    if temp in (comments):
                        if find_comment:
                            doc = head + menu_code
                            is_reg_menu = False
                        else:
                            find_comment = True
                    elif temp.startswith('#') or temp.startswith('self') \
                            or temp.startswith('sleep') \
                            or line.strip().startswith('openLeftTree') > 0:
                        head.pop()
                        doc = head + menu_code
                        doc.append(line)
                        is_reg_menu = False
            else:
                if line == '\r' or temp.startswith('#'):
                    end.append(line)
                elif is_deal_test or temp.startswith('@'):
                    if not is_deal_test or temp.startswith('@'):
                        pos = line.find('@')

                    end.append(line[:pos] + '# ' + line[pos:])

                    if temp.startswith('@data'):
                        test_funs[17] = test_funs[17].replace('$1', line)
                        test_funs[25] = test_funs[25].replace('$2', line.split('))')[0])
                        is_deal_test = True
                elif line.find('openLeftTree') > 0:
                    end.append(line[:line.find("'")] + "'TREE_NODE'])\r")
                elif temp.find('assert_context') > 0:
                    new_line, pos = append_comment(line)
                    end.append(new_line)
                    is_deal_test = True
                else:
                    end.append(line)

        with open(temp_test_logfile, 'w', encoding='utf-8') as fo:
            fo.writelines(doc + end + test_funs)


if __name__ == '__main__':
    # 指定testcase的根目录
    dirpath = Setting.BASE_PATH + r'src\com\nrtest\sea\testcase'
    upgrade_test_file(os.path.realpath(dirpath + r'\demo_new\test_Metclassfiy.py'))
