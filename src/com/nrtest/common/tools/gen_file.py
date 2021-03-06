# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: gen_file.py
@time: 2019-01-28 23:18
@desc:
"""

import time

from com.nrtest.common.data_access import DataAccess

# 作者
author = '郭春彪'

# 文件名，不同单词之间用下划线隔开
file_name = 'area_buy_ele'

# 存放菜单编号的数据文件类名
# 路径
data_file = 'D:\pythonworkspace\SEA2017\src\com\nrtest\pbs\data\net_loss_man\netLossMan_data'

# 菜单编号
menu_no = '00001305'

# Tab页名【中文】，没Tab页时，填空串：''
tab_name = ''

# Tab页名【英文】 ，不填时，名称格式与存放菜单编号的变量名类同
en_tab_name = ''

# 生成文件存放路径
filelistlog = r"D:\pythonworkspace\SEA2017\src\com\nrtest\pbs\page\net_loss_man\area_buy_ele._page.py"

# 当前执行想要生成的文件：01-生成Page文件；02-生成test文件
page_type = '01'


class GenFile():
    def __init__(self, script_type='01'):
        self.script_type = script_type
        self.el_setup = DataAccess.get_el_script_setup(script_type)

    # 01	作者
    def get_author(self, line):
        return line.format(author)

    # 02	文件名
    def get_file_name(self, line):
        if self.script_type == '01':
            return line.format(file_name.lower() + '_page.py')
        else:
            return line.format('test_' + file_name.lower() + '.py')

    # 03	时间
    def get_dt(self, line):
        dt = time.strftime('%Y-%m-%d %H:%M:%S')
        return line.format(dt)

    def _format_name(self, file, first_char_lower=False):
        items = file.split('_') if bool(file) else file_name.split('_')
        for idx, item in enumerate(items):
            temp = item.lower()
            items[idx] = temp if (idx == 0 and first_char_lower) else temp.capitalize()

        return ''.join(items)

    def _get_test_class_name(self, file=''):
        # return 'test_' + self._format_name(file)
        return 'Test' + self._format_name(file)

    # 04	get_check_code&page的class名
    def get_test_class(self, line, file=''):
        return line.format(self._get_test_class_name(file), self.get_page_class_name(file))

    # 05	菜单编号
    def get_menu_no(self, file=''):
        data_import = self.get_menu_import()
        data_class = data_import.split('import')[-1].strip()
        menu = data_class + '.' + self._format_name(file, True) + '_para'
        return menu, menu.split('.')[-1] + ' = \'' + menu_no + '\'\r'

    # 06	Tab页名称
    def get_tab_name(self, file=''):
        if bool(tab_name) and tab_name != '01':
            data_import = self.get_menu_import()
            data_class = data_import.split('import')[-1].strip()
            tab = data_class + '.' + self._format_name(file, True) + ('_' + en_tab_name if bool(en_tab_name) else '')
            return tab, (tab.split('.')[-1] + ' = \'' + tab_name + '\'\r') if bool(tab_name) else ''
        else:
            return '', ''

    # 07 菜单编号和Tab页名称
    def get_menu_no_and_table_name(self, line, file=''):
        menu, pa = self.get_menu_no(file)
        tab, pa1 = self.get_tab_name(file)
        if bool(tab_name) and tab_name != '01':
            para = menu + ', ' + tab
        else:
            para = menu
        return line.format(para)

    # 08	菜单路径
    def get_menu_path(self):
        menu_path = DataAccess.getMenu(menu_no)
        ls_menu = menu_path.split(',')
        menu_path = ls_menu[0]
        items = menu_path.split(';')
        # 菜单路径
        return ls_menu[-1] + '→' + '→'.join(items[1:]) + (':' + tab_name if bool(tab_name) else '')

    # 09	page的class名
    def get_page_class_name(self, file=''):
        return self._format_name(file) + 'Page'

    # 10	查询条件
    def get_querys(self):
        lines = []
        # xpath, xpath_name, use_share_xpath
        menu_xpath_list = DataAccess.get_menu_xpath_list(menu_no, tab_name, self.script_type)
        for qry_xpath in menu_xpath_list:
            if qry_xpath[0] != 'TREE_NODE' and qry_xpath[2] == '00':
                raise Exception('该节点配置错误:{},use_share_xpath不能为00'.format(','.join(qry_xpath)))

            if qry_xpath[0] == 'TREE_NODE':
                if self.script_type == '01':
                    continue
                el_scripts = self.el_setup['00']
            else:
                el_scripts = self.el_setup[qry_xpath[2]]
            fun_name = qry_xpath[0].lower()
            if self.script_type == '01':
                lines.append(' ' * 4 + '# ' + qry_xpath[1] + '\r')
                lines.append(el_scripts[0].format(fun_name))
                lines.append(el_scripts[1])
                lines.append('\r')
            else:
                lines.append(' ' * 8 + '# ' + qry_xpath[1] + '\r')
                if qry_xpath[0] == 'TREE_NODE':
                    lines.append(el_scripts[0].format(qry_xpath[0]))
                else:
                    lines.append(el_scripts[0].format(fun_name, fun_name.upper()))
                lines.append('\r')

        return lines

    # 11   菜单编号、Tab页存放类引入
    def get_menu_import(self):
        data_import = data_file.replace('/', '.')
        data_import = data_import.replace('\\', '.')
        data_import = data_import.replace('..', '.')
        data_import = data_import.replace('\n', '.n')
        data_import = data_import.replace('\t', '.t')
        data_import = data_import.replace('\r', '.r')
        data_import = data_import.replace('\f', '.f')
        if data_import.find('.') > 0:
            if data_import.find('.src.'):
                data_import = data_import.split('.src.')[-1]
            ls_data_import = data_import.split('.')
            return 'from ' + '.'.join(ls_data_import[:-1]) + ' import ' + ls_data_import[-1]
        else:
            return data_file

    def gen_file(self):
        # line_flag, script, script_line
        template = DataAccess.get_template(self.script_type)
        lines = []
        for idx, row in enumerate(template):
            line_flag = row[0]
            script = row[1] + '\r' if bool(row[1]) else '\r'
            line = ''
            if bool(line_flag):
                # 01	作者
                if line_flag == '01':
                    line = self.get_author(script)
                # 02	文件名
                elif line_flag == '02':
                    line = self.get_file_name(script)
                # 03	时间
                elif line_flag == '03':
                    line = self.get_dt(script)
                # 04	get_check_code&page的class名
                elif line_flag == '04':
                    line = self.get_test_class(script)
                # 05	菜单编号
                elif line_flag == '05':
                    line, menu = self.get_menu_no()
                    line = script.format(line)
                    print(' ' * 4 + '# ' + self.get_menu_path().split(':')[0])
                    print(' ' * 4 + menu)

                # 06	Tab页名称
                elif line_flag == '06':
                    line, tab = self.get_tab_name()
                    line = script.format(line)
                    if not bool(tab_name) or tab_name == '01':
                        pos = line.find('menuPage')
                        line = line[:pos] + '# ' + line[pos:]
                    print(' ' * 4 + tab)

                # 07 菜单编号和Tab页名称
                elif line_flag == '07':
                    line = self.get_menu_no_and_table_name(script)

                # 08	菜单路径
                elif line_flag == '08':
                    line = script.format(self.get_menu_path())

                # 09	page的class名
                elif line_flag == '09':
                    line = script.format(self.get_page_class_name())

                # 11   菜单编号、Tab页存放类引入
                elif line_flag == '11':
                    line = script.format(self.get_menu_import())


                if bool(line):
                    lines.append(line)
                elif line_flag == '10':  # 10	查询条件
                    line = self.get_querys()
                    lines = lines + line
            else:
                lines.append(script)

        with open(filelistlog, 'a+', encoding='utf-8') as fo:
            fo.writelines(lines)

if __name__ == '__main__':
    genPageFile = GenFile(page_type)
    genPageFile.gen_file()