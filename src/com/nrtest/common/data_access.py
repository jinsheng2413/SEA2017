# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: data_access.py
@time: 2018/5/23 0023 14:04
@desc:测试用例数据提取的数据库访问类
"""

import os
import re

from com.nrtest.common.db_driver import PyOracle
from com.nrtest.common.dictionary import Dict
from com.nrtest.common.setting import Setting

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


# 或者os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'

class DataAccess:

    @staticmethod
    def getMenu(menuNo):

        pyoracle = PyOracle.getInstance()
        fun_name = 'pkg_nrtest.get_menu_path'
        menu_path = pyoracle.callfunc(fun_name, 'str', [menuNo, Setting.PROJECT_NO])
        return menu_path

    @staticmethod
    def getAllMenu():
        """
        获取测试系统所有菜单
        :return:
        """
        pyoracle = PyOracle.getInstance()
        cur = pyoracle.callFCur('pkg_nrtest.get_all_menu', [Setting.DEFAULT_USER, Setting.PROJECT_NO])
        return cur

    @staticmethod
    def get_menu_setup(project_no):
        """
        用于默认刷新admin用户下的‘00000’用户组的测试用例
        :param user_no: 测试用例用户
        :param group_no: 测试用例组
        :return:
        """
        sql = 'select param_item_val as menu_level, min_limit as menu_action from tst_parameter pa \
                WHERE pa.project_no = :1 \
                  AND param_no = \'BASE\' \
                  AND param_item_no = \'START_MENU_LEVEL\''
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql, [project_no])
        menu_level = dataSet[0][0]
        # ('2:', '02')  从第2级菜单开始
        # ('2,3', '02') 只有2,3两级菜单
        menu_para = {'ACTION': dataSet[0][1]}
        if menu_level[-1] == ':':
            menu_para.setdefault('FIRST_LEVEL', 'Y')
            menu_para.setdefault('LEVELS', int(menu_level[:-1]))
        else:
            menu_para.setdefault('FIRST_LEVEL', 'N')
            menu_para.setdefault('LEVELS', menu_level.split(','))
        return Dict(menu_para)

    @staticmethod
    def getLeftTree(treeNO):
        pyoracle = PyOracle.getInstance()
        org_path = pyoracle.callfunc('pkg_nrtest.get_org_path', 'str', [treeNO, Setting.PROJECT_NO])
        return org_path

    @staticmethod
    def getTreeNode(node_no):
        """
        应用于PBS等左边树管理
        :param node_no:
        :return:
        """
        pyoracle = PyOracle.getInstance()
        node_path = pyoracle.callfunc('pkg_nrtest.get_tree_node_path', 'str', [node_no, Setting.PROJECT_NO])
        return node_path

    @staticmethod
    def getCaseData(menuNo, tabName='01', valCheck=False):
        """
        根据菜单编号提取测试用例数据
        :param menuNo: 菜单编号
        :param tabName: Tab页名
        :param valCheck: True-对元素数据有效性校验；False-测试用例数据
        :return: 返回用例数据
        """
        pyoracle = PyOracle.getInstance()
        qry = [Setting.GROUP_USER,
               Setting.GROUP_NO,
               menuNo,
               tabName,
               Setting.PROJECT_NO]

        funName = 'pkg_nrtest.get_tst_case_for_valid' if valCheck else 'pkg_nrtest.get_tst_case'
        tst_case = pyoracle.callFCur(funName, qry)
        print(tst_case)
        try:
            rslt = []
            for row in tst_case:
                temp = DataAccess.replace_chrs(row[0])
                rslt.append(Dict(eval(temp)))
            if len(rslt) == 0:
                print('没配置{}用例数据...\nqry:{}；valCheck：{}\n'.format(('查询条件校验' if valCheck else '测试'), qry, valCheck))
            else:
                print('当前用例数据：\n', rslt, '\n')
        except BaseException:
            print('获取测试用例数据失败，请检查用例用户组名称是否配置正确，用例编写是否符合要求')
        return rslt

    @staticmethod
    def refresh_case(user_no='', group_no=''):
        """
        用于默认刷新admin用户下的‘00000’用户组的测试用例
        :param user_no: 测试用例用户
        :param group_no: 测试用例组
        :return:
        """
        para = [Setting.GROUP_USER if user_no == '' else user_no,
                '00000' if group_no == '' else group_no,
                Setting.PROJECT_NO]
        pyoracle = PyOracle.getInstance()
        cases = pyoracle.callproc('pkg_nrtest.refresh_case', para)

        return cases

    @staticmethod
    def refresh_all():
        """
        用于默认刷新admin用户下的‘00000’用户组的测试用例
        :param user_no: 测试用例用户
        :param group_no: 测试用例组
        :return:
        """

        pyoracle = PyOracle.getInstance()
        para = [Setting.PROJECT_NO]
        pyoracle.callproc('pkg_nrtest.refresh_all_case', para)

    @staticmethod
    def get_case_result(tst_case_id):
        """
        用于默认刷新admin用户下的‘00000’用户组的测试用例
        :param user_no: 测试用例用户
        :param group_no: 测试用例组
        :return:
        """
        # tab确定哪个显示区、列明、点击的那一列
        sql = 'select assert_type,tab_column_name , column_name, expected_value \
                      from tst_case_result where IS_VALID = \'Y\' and tst_case_id = :id order by assert_type'
        # sql = 'select assert_type,tab_column_name , column_name, expected_value ,row_num,is_space\
        #       from tst_case_result where tst_case_id = :id order by assert_type'
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql, [tst_case_id])
        return dataSet

    @staticmethod
    def get_data_dictionary(dict_catalog):
        """
        提取数据字典的查询条件类别
        :param dict_catalog: 查询条件分类编码
        :return:
        """
        sql = 'SELECT dict_name FROM tst_dictionary t \
                WHERE project_no = :1  \
                  AND dict_catalog = :2 \
                ORDER BY t.dict_no'
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql, [Setting.PROJECT_NO, dict_catalog])

        for idx, row in enumerate(dataSet):
            dataSet[idx] = row[0]
        return dataSet

    @staticmethod
    def refresh_menu(p_menu_no=''):
        """
        刷新菜单关系（由坐标定位改为按名称定位）
        :param p_menu_no: 父节点菜单编码，该值为空刷新全部菜单，否则刷新指定菜单
        """
        pyoracle = PyOracle.getInstance()
        if p_menu_no == '':
            pyoracle.callproc('pkg_nrtest.refresh_menu')
        else:
            para = [p_menu_no, Setting.PROJECT_NO]
            pyoracle.callproc('pkg_nrtest.refresh_menu', para)

    @staticmethod
    def refresh_menu_xapth(menu_no=''):
        """
        用例数据填完后，刷新菜单/TAB对应的元素清单
        :param menu_no: 菜单编码，该值为空刷新全部菜单，否则刷新指定菜单
        """
        pyoracle = PyOracle.getInstance()
        pyoracle.callproc('pkg_nrtest.refresh_menu_xapth', [menu_no, Setting.PROJECT_NO])

    @staticmethod
    def el_operate_log(menu_no, tst_case_id, locator, class_path, except_type, except_info):
        pyoracle = PyOracle.getInstance()
        sql = 'insert into tst_operate_log (computer_name, project_no, menu_no, tst_case_id, locator, class_name, except_type, except_info) \
        values (:1, :2, :3, :4, :5, :6, :7, :8)'
        para = (os.environ['COMPUTERNAME'],
                Setting.PROJECT_NO,
                menu_no,
                tst_case_id,
                locator[0] + '-->' + locator[1],
                class_path,
                except_type,
                str(except_info))
        pyoracle.insert(sql, para)

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
    def get_skip_data(case_id, colu_name):
        sql = 'select tres.tab_column_name,lr.tab_name ,tres.column_name,tres.row_num,lr.xpath_type,lr.xpath ,lr.target_tab_name,lr.trans_type,' \
              'lr.target_xpath,lr.trans_value, lr.is_trans,lr.element_sn ' \
              'from tst_case_result tres,TST_COL_LINK_RELA  lr,tst_case case ' \
              'where tres.tst_case_id = case.tst_case_id and tres.column_name = lr.col_name and case.menu_no = lr.menu_no and case.tab_name = lr.tab_name and tres.tst_case_id =:case_id  and tres.assert_type in (\'21\',\'23\') and tres.column_name =:col_name order by lr.element_sn'
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql, [case_id, colu_name])
        return dataSet

    @staticmethod
    def get_xpath_tab_data(xpath, caseid, tab_name):
        sql = 'select ts.xpath_name from tst_menu_xpath_list ts \
              where ts.xpath =:xpath \
              and ts.menu_no in (select u.menu_no from tst_case u where u.tst_case_id =:caseid)\
              and ts.tab_name =:tabName'
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql, [xpath, caseid, tab_name])
        return dataSet

    @staticmethod
    def get_xpath_menu_data(xpath, menuName):
        sql = 'select ts.xpath_name from tst_menu_xpath_list ts \
                 where ts.xpath =:xpath \
                 and ts.menu_no in (select u.menu_no from tst_menu u where u.menu_name =:menuName)'
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql, [xpath, menuName])
        return dataSet

    @staticmethod
    def get_menu_xpath_list(menu_no, tab_name='01', script_type='01'):
        sql = 'SELECT xpath, xpath_name, use_share_xpath \
                FROM tst_menu_xpath_list  \
                WHERE project_no = :1 \
                  AND menu_no = :2 \
                  AND tab_name = :3 ' + (" AND use_share_xpath !='00'" if script_type == '01' else '') + ' ORDER BY element_sn'
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql, [Setting.PROJECT_NO, menu_no, (tab_name if bool(tab_name) else '01')])
        return dataSet

    @staticmethod
    def get_el_script_setup(script_type='01'):
        sql = 'select el_type, script_line, script \
                from tst_element_script_setup t \
                where script_type = :1 \
                ORDER BY el_type, script_line'
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql, [script_type])
        el_type = ''
        el_scripts = {}
        lines = []
        for row in dataSet:
            if bool(el_type):
                if row[0] == el_type:
                    lines.append(' ' * 8 + row[2] + '\r')
                else:
                    el_scripts.setdefault(el_type, lines)
                    el_type = row[0]
                    lines = [' ' * (4 if script_type == '01' else 8) + row[2] + '\r']
            else:
                el_type = row[0]
                lines = [' ' * (4 if script_type == '01' else 8) + row[2] + '\r']
        el_scripts.setdefault(el_type, lines)
        return el_scripts

    @staticmethod
    def get_template(script_type='01'):
        sql = 'SELECT line_flag, script, script_line FROM tst_script_template t \
                WHERE template_type = :1 \
                ORDER BY script_line'
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql, [script_type])

        return dataSet


if __name__ == '__main__':
    pass

    # print(DataAccess.get_xpath_menu_data('CONS_NO', '用户数据查询'))
    # 统计查询→采集建设情况→采集覆盖情况→用户采集覆盖率统计【下拉复选、单选选择】
    # print(DataAccess.getCaseData("99926400", tabName='01'))
    # print(DataAccess.refresh_all())
    # print(type(str))
    # print(DataAccess.get_case_result('999111003'))
    # val = Dict(eval(str[4]['ORG_NO']))
    # print(val['FLAG'], val['VALUE'])
    # DataAccess.refresh_all()
    # for i in  str[4:10]:
    #     print(i)
    # print(DataAccess.getAllMenu())
    # DataAccess.getMenu('99913210')
    # pass
    # 刷新菜单/tab对应的元素
    # DataAccess.refresh_menu_xapth('填写要刷新的菜单编号')
    print(DataAccess.get_el_script_setup('02'))
    # print(DataAccess.get_menu_xpath_list('99912100','终端调试', '02'))
