# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: update_testpy.py
@time: 2018-12-19 15:15
@desc:
"""
import codecs

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
    '        self.start_case(para, __file__)\r',
    '        self.query(para)\r',
    '        self.assert_query_result(para)\r',
    '        self.end_case()\r',
    '\r',
    '    @BeautifulReport.add_test_img()\r',
    '$2, valCheck=True))\r',
    '    def _test_checkValue(self, para):\r',
    '        self.start_case(para, __file__)\r',
    '        self.query(para)\r',
    '        self.assert_query_criteria(para)\r',
    '        self.end_case()\r']

setup = ['        print(\'开始执行\')\r',
         '        # 打开菜单（需要传入对应的菜单编号）\r',
         '        menuPage = MenuPage.openMenu($',
         '        sleep(1)',
         '        super(TestCase, cls).__init__(cls, menuPage.driver, menuPage)\r',
         '        # 菜单页面没多个Tab页时，请注释clickTabPage所在行代码\r',
         '        menuPage.clickTabPage(SysConfigManData.BackgroupServeMonitor_tabName)\r',
         '        # 菜单页面上如果没日期型的查询条件时，请注释下面代码\r',
         '        menuPage.remove_dt_readonly()\r']


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
    find_setup = False
    find_def = False
    head = []
    end = []
    doc = []
    script = ''
    with codecs.open(file_name, 'r', 'utf-8') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            line = (lines[i])[:-1]  # 去除行尾的\n符
            temp = line.strip().lower()
            if temp.startswith('def') and (temp.find('input') > 0):
                if script == 'sel':
                    child = doc[-6:]
                    child.reverse()
                    pos = -1
                    for i, ln in enumerate(child):
                        if ln == '\r':
                            pos = i
                        elif pos >= 0 and ln != '\r':
                            break
                    doc.insert(pos * -1 - 1, blance + 'self.selectDropDown(' + para + ')\r')

                blance = line.split('def')[0] + '    '
                para = line.split(',')[1].split(')')[0].strip()

                if temp.find('inputstr') > 0:
                    script = 'str'
                elif temp.find('inputchk') > 0:
                    script = 'chk'
                elif temp.find('inputdt') > 0:
                    script = 'dt'
                elif temp.find('inputsel') > 0 or temp.find('inputrsel') > 0:
                    script = 'sel'
                elif temp.find('btn_') > 0:
                    script = 'btn'

                doc.append(line)
                continue

            if temp.startswith('def') and temp.find('btn_') > 0:
                if script == 'sel':
                    child = doc[-6:]
                    child.reverse()
                    pos = -1
                    for i, ln in enumerate(child):
                        if ln.find('self.') > 0 or ln.find('sleep') > 0:
                            pos = i
                        elif pos >= 0 and ln != '\r':
                            break
                    doc.insert(pos * -1, blance + 'self.selectDropDown(' + para + ')\r')
                doc.append(line)
                continue

            if temp.startswith('#') or temp == '\r':
                doc.append(line)
                continue

            if temp in (comments):
                find_comment = not find_comment
                doc.append(line)
                continue

            if find_comment:
                doc.append(line)
                continue
            if script in ('str', 'chk', 'dt') and temp.find('self.input') >= 0:
                line = line.replace(',', ') #', 1)

                # doc.append(line)
            elif script == 'sel' and line != '\r':
                for c in line:
                    if c != ' ':
                        break
                line = line.replace(c, '# ' + c, 1)

            doc.append(line)

        for i in range(5):
            if doc[-1] == '\r':
                doc.pop()
            else:
                break
        doc.append(blance + 'self.btn_query()\r')
        with open(temp_test_logfile, 'w', encoding='utf-8') as fo:
            fo.writelines(doc)


if __name__ == '__main__':
    # 指定testcase的根目录
    file = r'D:\PycharmProjects\SEA2017\src\com\nrtest\sea\pages\adv_app\costControlManage\costControlManage_page.py'
    upgrade_test_file(file)
