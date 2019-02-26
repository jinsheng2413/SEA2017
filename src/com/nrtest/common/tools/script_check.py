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

from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.setting import Setting


def find_not_equal_input(dirname):
    """
    检查self.inputXXX_abc(para['ABC'])方法名是否与参数一致
    正解：self.inputStr_cons_no(para['CONS_NO'])
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


def find_atail_file_not_equal_file_name(dirname):
    """
    检查@file内容是否与文件名一致
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
                        if temp.startswith('@author:'):
                            author = temp.split(':')[1].strip()
                        if temp.startswith('@file:'):
                            file_name = temp.split(':')[1].strip()
                            if file_name != filename:
                                with codecs.open(filelistlog, 'a+', encoding='utf-8') as fo:
                                    fo.write(package + '\r')
                                    fo.write(author + '~~~  ' + temp.strip() + '\r')


def find_not_standard_input(dirname):
    """
    检查元素操作方法名是否符合规范：inputDt\inputChk\inputSel\inputStr
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
                            if not (temp.startswith('self.inputDt') \
                                    or temp.startswith('self.inputChk') \
                                    or temp.startswith('self.inputSel') \
                                    or temp.startswith('self.inputStr')):
                                defs.append(temp.split('(')[0].split('.')[1] + '\r')
                if bool(defs):
                    with codecs.open(filelistlog, 'a+', encoding='utf-8') as fo:
                        fo.write('\r********')
                        fo.write(package + '\r')
                        fo.writelines(defs)
                        fo.write('\r')

def find_not_startwith_test(dirname):
    """
    检查testcase路径下是否存在不符合test_打头的.py文件
    """
    filelistlog = Setting.LOG_PATH + "filelistlog.log"  # 保存文件路径
    postfix = set(['py'])  # 设置要保存的文件格式
    exclude_files = ['bg.py', 'demo.py', 'gt.py', 'pbs5000.py', '__init__.py', 'gt_for_menu_list.py', 'test.py']
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


def append_remark(def_name):
    filelistlog = Setting.LOG_PATH + "filelistlog.log"  # 保存文件路径
    with codecs.open(filelistlog, 'a+', encoding='utf-8') as fo:
        fo.write('******************************' + def_name.__doc__.strip() + '******************************\r')


def checkParaWithDB(dirname):
    """
    检查测试用例中，实际引用的页面元素与数据库对应配置（菜单编号+Tab页名称）情况比对
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
                    data_file = {}
                    defs = []
                    menu_tab = {}
                    pkg = ''
                    for line in lines:
                        if bool(pkg):
                            fns = line.strip().replace(' ', '').split(',')
                            for fn in fns:
                                data_file.setdefault(fn.strip(), pkg)
                            pkg = ''

                        if line.strip().startswith('from'):
                            temp = line.strip().replace('from', '').split('import')
                            if len(temp) == 2:
                                if temp[1].strip() == '\\':
                                    pkg = temp[0].strip()
                                else:
                                    pkg = ''
                                    fns = temp[1].replace(' ', '').split(',')
                                    for fn in fns:
                                        data_file.setdefault(fn.strip(), temp[0].strip())

                        if line.strip().startswith('menuPage'):
                            temp = line.strip().replace(' ', '')
                            if temp.find('openMenu(') > 0:
                                menu = temp.replace(')', '').split('openMenu(')[1].split('.')
                                data_class = menu[0]
                                menu_tab.setdefault('MENU', menu[1])
                                menu_tab.setdefault('FN', data_file.get(data_class) + '\t' + data_class)

                            elif temp.find('clickTabPage(') > 0:
                                tab = temp.replace(')', '').split('(')[1].split('.')
                                menu_tab.setdefault('TAB', tab[1])

                        temp = line.strip().replace(' ', '')

                        # if temp.startswith('self.') and temp.find('para') > 0 and temp.find('[') > 0:
                        if (temp.find('openLeftTree') >= 0 or temp.find('self.input') >= 0) and temp.find('#') == -1 and temp.find(
                                'para') > 0 and temp.find('[') > 0:
                            ls = temp.split('\'')
                            para = ls[1].split('\'')[0]
                            defs.append(para + '\r')

                if bool(menu_tab):
                    # MENU->para_lowPowerFaultDeal
                    # TAB->para_lowPowerFaultDeal_deal
                    temp = menu_tab['FN'].split('\t')
                    menu_tab.pop('FN')
                    class_name = temp[1]
                    is_changed = False
                    into_class = False
                    file_path = Setting.BASE_PATH + Setting.PATTERN + 'src' + Setting.PATTERN + temp[0].replace('.', Setting.PATTERN) + '.py'
                    if not os.path.isfile(file_path):
                        menu_tab.setdefault('FILE', file_path)
                    else:
                        with codecs.open(file_path, 'r', 'utf-8') as file:
                            lines = file.readlines()
                            for line in lines:
                                temp = line.strip()
                                if temp.startswith('class'):
                                    if temp.find(class_name) > 0:
                                        into_class = True
                                    elif into_class:
                                        break
                                elif into_class:
                                    if temp.startswith(menu_tab['MENU']):
                                        menu_tab['MENU'] = temp.replace(' ', '').split('=')[1].replace('\'', '')
                                        if 'TAB' not in menu_tab:
                                            is_changed = True
                                            break

                                    if 'TAB' in menu_tab and temp.startswith(menu_tab['TAB']):
                                        menu_tab['TAB'] = temp.replace(' ', '').split('=')[1].replace('\'', '')
                                        is_changed = True
                                        break
                if is_changed:
                    # if filename == 'test_ReadCompleteRate.py':
                    #     a = 'abc'
                    if 'MENU' not in menu_tab:
                        print(filename)
                    try:
                        tab_name = menu_tab['TAB'] if 'TAB' in menu_tab else '01'
                        menu_xpah_list = DataAccess.get_menu_xpath_list(menu_tab['MENU'], tab_name, None)
                        if bool(menu_xpah_list):
                            unused = []  # 未使用的配置项；
                            unsetup = []  # 未配置的元素；
                            db_setup = []
                            for row in menu_xpah_list:
                                db_setup.append(row[0] + '\r')
                                if row[0] + '\r' not in defs:
                                    unused.append(row[0] + '->' + ('None' if row[1] is None else row[1]) + '\r')

                            for xpath in defs:
                                if xpath not in db_setup:
                                    unsetup.append(xpath)
                    except Exception as ex:
                        print(menu_tab['MENU'] + '\r')
                        print(tab_name + '\r')
                        print(filename)

                if bool(unused) or bool(unsetup):
                    with codecs.open(filelistlog, 'a+', encoding='utf-8') as fo:
                        fo.write('\r********')
                        fo.write(package + '\r')
                        for key, val in menu_tab.items():
                            fo.writelines(key + '->' + val + '\r')
                        if bool(unused):
                            fo.write('\r已配置，但没有使用的页面元素：\r')
                            fo.writelines(unused)
                        if bool(unsetup):
                            fo.write('\r未配置，但脚本中已引用的页面元素：\r')
                            fo.writelines(unsetup)
                        # fo.writelines(defs)
                        fo.write('\r')


def not_find_BeautifulReport(dirname):
    """
    test_query前没有配置@BeautifulReport.add_test_img()
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
                    prior_temp = ''
                    for i, line in enumerate(lines):
                        temp = line.strip().replace(' ', '')
                        if temp.startswith('@data(*DataAccess') and not prior_temp.startswith('@BeautifulReport'):
                            with codecs.open(filelistlog, 'a+', encoding='utf-8') as fo:
                                fo.write('\r********')
                                fo.write(package + '\r')
                                fo.write('\r')
                        else:
                            prior_temp = temp


def not_find_test_comment(dirname):
    """
    test_query下没配置注释,或找不到test_query方法
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
                    find_test_query = False
                    for i, line in enumerate(lines):
                        temp = line.strip().replace(' ', '')
                        if temp.find('test_query') > 0:
                            find_test_query = True
                        elif find_test_query:
                            if not temp.startswith('"""') or (temp.startswith('"""') and len(temp) == 3):
                                with codecs.open(filelistlog, 'a+', encoding='utf-8') as fo:
                                    fo.write('\r********')
                                    fo.write(package + '\r')
                                    fo.write('\r')
                            break
                    if not find_test_query:
                        with codecs.open(filelistlog, 'a+', encoding='utf-8') as fo:
                            fo.write('\r****test funName is not "test_query"****')
                            fo.write(package + '\r')
                            fo.write('\r')


if __name__ == '__main__':
    # # 指定根目录
    # dirpath = os.path.dirname(os.path.realpath(__file__))
    dirpath = r'D:\PycharmProjects\SEA2017\src\com\nrtest\sea\testcase'
    append_remark(find_not_equal_input)
    find_not_equal_input(dirpath)

    append_remark(find_atail_file_not_equal_file_name)
    find_atail_file_not_equal_file_name(dirpath)

    append_remark(find_not_standard_input)
    find_not_standard_input(dirpath)

    append_remark(find_not_startwith_test)
    find_not_startwith_test(dirpath)

    append_remark(checkParaWithDB)
    checkParaWithDB(dirpath)

    append_remark(not_find_BeautifulReport)
    not_find_BeautifulReport(dirpath)

    append_remark(not_find_test_comment)
    not_find_BeautifulReport(dirpath)
