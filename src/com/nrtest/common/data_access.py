# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: data_access.py
@time: 2018/5/23 0023 14:04
@desc:测试用例数据提取的数据库访问类
"""

import os

import execjs

from com.nrtest.common.db_driver import PyOracle
from com.nrtest.common.dictionary import Dict
from com.nrtest.common.setting import Setting
from com.nrtest.common.utils import Utils

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


# 或者os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'

class DataAccess:
    @staticmethod
    def get_province():
        """
        提取项目所属现场版本
        :return:
        """
        pyoracle = PyOracle.getInstance()
        fun_name = 'pkg_nrtest.get_province'
        menu_path = pyoracle.callfunc(fun_name, 'str', [Setting.PROJECT_NO])
        return menu_path

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
    # def getLeftTree(treeNo):
    def get_org_path(org_name):
        pyoracle = PyOracle.getInstance()
        org_path = pyoracle.callfunc('pkg_nrtest.get_org_path', 'str', [org_name, Setting.PROJECT_NO])
        return org_path

    @staticmethod
    def get_org_node_by_name(org_name):

        sql = 'SELECT org_no FROM tst_org  WHERE org_name = :1 AND  project_no = :2'
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql, [org_name, Setting.PROJECT_NO])
        return '{"NODE_FLAG":"01", "NODE_VALUE":"%s"}' % dataSet[0][0]

    @staticmethod
    def getTreeNode(node, by_tree_node=False):
        """
        应用于PBS等左边树管理
        :param node_no:
        :param by_tree_node:True-经tst_tree_node表提取节点；False-经tst_org表提取节点
        :return:
        """
        node_value = node['NODE_VALUE']
        if by_tree_node:
            by_tree_node = 'Y'
        else:
            by_tree_node = 'N' if node['NODE_FLAG'] == '01' else 'Y'
        pyoracle = PyOracle.getInstance()
        node_path = pyoracle.callfunc('pkg_nrtest.get_tree_node_path', 'str', [node_value, Setting.PROJECT_NO, by_tree_node])
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
        # print(tst_case)
        try:
            rslt = []
            for row in tst_case:
                temp = Utils.replace_chrs(row[0])
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
    def refresh_dynamic_date():
        pyoracle = PyOracle.getInstance()
        para = [Setting.PROJECT_NO]
        pyoracle.callproc('pkg_nrtest.refresh_dynamic_date', para)

    @staticmethod
    def get_case_result(tst_case_id):
        """
        用于默认刷新admin用户下的‘00000’用户组的测试用例
        :param tst_case_id: 测试用例ID
        :return:
        """
        # tab确定哪个显示区、列明、点击的那一列
        # sql = 'select assert_type, nvl(tab_column_name, column_name) AS tab_column_name , column_name, expected_value, row_num, is_special, wait_for_target, head_row \
        #               from tst_case_result where IS_VALID = \'Y\' and tst_case_id = :id order by assert_type, exec_order'
        # pyoracle = PyOracle.getInstance()
        # dataSet = pyoracle.query(sql, [tst_case_id])

        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.callFCur('pkg_nrtest.get_case_result', [tst_case_id])
        return dataSet

    @staticmethod
    def get_data_dictionary(dict_catalog, rsltType='01', is_public=False):
        """
        提取数据字典的查询条件类别
        :param dict_catalog: 查询条件分类编码
        :param rsltType:01-dict_name List；02-dict key值为dict_name; 03-dict key值为dict_no
        :return:
        """
        if is_public:
            sql = 'SELECT dict_no, dict_name FROM tst_dictionary t \
                                            WHERE project_no is null \
                                              AND dict_catalog = :1 \
                                            ORDER BY t.dict_no'
            qry = [dict_catalog]
        else:
            sql = 'SELECT dict_no, dict_name FROM tst_dictionary t \
                                WHERE project_no = :1  \
                                  AND dict_catalog = :2 \
                                ORDER BY t.dict_no'
            qry = [Setting.PROJECT_NO, dict_catalog]

        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql, qry)
        if rsltType == '01':
            rslt = []
            for idx, row in enumerate(dataSet):
                rslt.append(row[1])
        elif rsltType == '02':
            rslt = {}
            for row in dataSet:
                rslt.setdefault(row[1], row[0])
        elif rsltType == '03':
            rslt = {}
            for row in dataSet:
                rslt.setdefault(row[0], row[1])
        return rslt

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
                (locator[0] + '-->' + locator[1] if bool(locator) else locator),
                class_path,
                except_type,
                str(except_info))
        pyoracle.insert(sql, para)

    @staticmethod
    def case_exec_log(tst_case_id, start_time, end_time, config_seconds, actual_seconds):
        pyoracle = PyOracle.getInstance()
        sql = "insert into tst_case_exec (tst_case_id, computer_name, start_time, end_time, config_seconds, actual_seconds, project_no) " \
              "  values (:1, :2, to_date(:3, 'yyyy-mm-dd hh24:mi:ss'), to_date(:4, 'yyyy-mm-dd hh24:mi:ss'), :5, :6, :7)"
        para = (tst_case_id,
                os.environ['COMPUTERNAME'],
                start_time,
                end_time,
                config_seconds,
                actual_seconds,
                Setting.PROJECT_NO)
        pyoracle.insert(sql, para)

    @staticmethod
    def load_tests_ByMenuList():
        """
        指定菜单用例清单
        :return:
        """
        by_menu_list = Setting.GROUP_BY_MENU_LIST
        if not bool(by_menu_list):
            by_menu_list = Setting.GROUP_NO
        qry = [Setting.PROJECT_NO, by_menu_list]
        pyoracle = PyOracle.getInstance()
        funName = 'pkg_nrtest.load_tests_ByMenuList'
        dataSet = pyoracle.callFCur(funName, qry)
        # print(dataSet)
        return dataSet

    @staticmethod
    def get_skip_data(case_id, col_name):
        sql = 'select tres.tab_column_name,lr.tab_name ,tres.column_name,tres.row_num,lr.xpath_type,lr.xpath ,lr.target_tab_name,lr.trans_type, ' \
              'lr.target_xpath,lr.trans_value, lr.is_trans,lr.element_sn, lr.target_menu_no, m.menu_name as target_menu_name, lr.column_idx   ' \
              'from tst_case_result tres,TST_COL_LINK_RELA  lr,tst_case ca, tst_menu m    ' \
              'where tres.tst_case_id = ca.tst_case_id and tres.column_name = lr.col_name   ' \
              'and ca.menu_no = lr.menu_no and ca.tab_name = lr.tab_name and lr.target_menu_no = m.menu_no  ' \
              'and (tres.assert_type like \'2%\' or tres.assert_type like \'3%\')' \
              'and tres.tst_case_id =:case_id    ' \
              'and tres.column_name =:col_name order by lr.element_sn'

        # 'and tres.assert_type in (\'21\',\'23\',\'26\',\'27\') ' \
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql, [case_id, col_name])
        return dataSet

    @staticmethod
    def get_menu_xpath_data(menu_no, tab_name, xpath):
        """
        xpath转换为对应xpath中文名
        :param xpath:
        :param menu_no: 菜单名称
        :param tab_name:
        :return:
        """
        sql = '''select ts.xpath_name, ts.use_share_xpath, ts.option_name, ts.tag_blank_type from tst_menu_xpath_list ts  
               where ts.project_no = :project_no 
                and ts.menu_no = :menu_no 
                and ts.tab_name = :tab_name 
                and ts.xpath = :xpath'''
        # print('sql', sql)
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql, [Setting.PROJECT_NO, menu_no, tab_name, xpath])
        # print(dataSet)
        return dataSet[0]

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
    def get_data_trans(trans_type, data_before):
        """
        # 15 - 终端地址转资产号；16 - 终端资产号转地址
        """
        if trans_type in ['15']:
            sql = 'select asset_no from tst_asset_info \
                    where asset_type = :1 \
                      and asset_addr = :2'
        else:
            sql = 'select asset_addr from tst_asset_info \
                                where asset_type = :1 \
                                  and asset_no = :2'
        asset_type = '01' if trans_type in ['15', '16'] else '02'
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql, [asset_type, data_before])
        # print(dataSet)
        return dataSet[0][0]

    @staticmethod
    def get_org_type(org, by_name=True):
        """
        供电单位下钻用：获取供电单位的org_type
        """
        if by_name:
            sql = 'SELECT org_type FROM tst_org WHERE project_no = :1 \
                      AND org_name = :2 AND ROWNUM = 1'
            org = org.replace('（直属）', '(直属)')
        else:
            sql = 'SELECT org_type FROM tst_org WHERE project_no = :1 \
                                  AND org_no = :2 AND ROWNUM = 1'
        try:
            pyoracle = PyOracle.getInstance()
            dataSet = pyoracle.query(sql, [Setting.PROJECT_NO, org])
            return dataSet[0][0]
        except Exception as ex:
            print('获取"{}"--by_name:{}的org_type报错！'.format(org, by_name))
            raise ex

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

    @staticmethod
    def get_account_of_sea():
        sql = 'SELECT encode_no, encode_pwd FROM tst_account WHERE encode_no IS NOT NULL'
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql)
        user_accounts = []
        for account in dataSet:
            user_accounts.append({"username": account[0], "password": account[1]})
            # print(user_accounts[-1],',\r')
        # return user_accounts
        return [{'username': 'MTAwNzI4NzI=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'Z2xt', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'YWRtaW4=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'anVoYW5qaQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'Y3lm', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'emhvdWh1aQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTEw', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MDgxNw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'd3Nkeg==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'emhhbmd5YW5saQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTAwNDUwMTU=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'bGl1eGlhb3RpYW4=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'bGloYWl5YW5n', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'bmluZ2Jv', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'dHh4', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'eXh5ZF93aHk=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'd3M=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTAwNDU2MDI=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'YW15bGVl', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'dXNlcmFkbWlu', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTAwODY=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'emhlamlhbmd3YW5zaGVuZw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'emhhbmdqaWU=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'Z2pjeDIwMTI=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'OTAwMTA=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'YWRtaW5feXc=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'Y2hheHVuMQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTAwMTE4NTI=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'Y2hheHVuNA==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'a2VmdXpob25neGlu', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'bGlsaWFuZ2hhbw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTAwMDAxMDI=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTAwNDMyMTA=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTAwMTc2ODQ=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTAwNjE0MTA=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTAwMTYwNDE=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTAwMDU1NDA=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTAwNDUyNTI=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTAwNDQ4OTY=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTAwNDMzNTY=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'c3Vpc2hpd2Vp', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'eXh5ZF90aHQ=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTAwNDMyMDk=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTAwMTE4NDk=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTAwMzczMTI=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'ZG5mdw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'emNqenl5aA==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'eXps', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'Y2hheHVuMg==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTAwMzcyOTI=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTIzNDU2Nzg5', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'eXJt', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'Y2hheHVuMw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'OTAwMDA=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'eGl0b25nY2VzaGk=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'YWRtaW5fc2o=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'bHBw', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'ZGlhb2R1', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'c2hlbmppMg==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'bGl1Y2hpY2hhbw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'c3VwZXJfYWRtaW4=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'cXE=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'bGtfYWRtaW4=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTIz', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'emhlbmd0YW8=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'enN0aWNiYw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'ZnVzaW1pbg==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'c3VuYmlhbw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MTEwMDEyMDA=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'ano=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'd2pi', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'bHk=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'Z3Vkcw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'eXVzaGVuZw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'Y2hlbnl1ZWZlbmc=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'amluc2hlbmc=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'bHh5', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'c2VhMjAxNg==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'dHNk', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'c2hlbmppMQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'MjAxNTA4MjU=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'V1RKXzE=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'dGlhbnll', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'YWRtaW5feHQ=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'bGRjeA==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'bGpmMQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'cGFpc2Vu', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'bGpm', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='},
                {'username': 'cHl0aG9uX3Rlc3Q=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A=='}]

    @staticmethod
    def encode_account(js):
        sql = 'SELECT staff_no FROM tst_account WHERE encode_no IS NULL'
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql)
        fun_base64 = execjs.compile(js)
        for account in dataSet:
            encode_no = fun_base64.call('encode_base64', account[0])
            pyoracle.update('UPDATE tst_account SET encode_no = :1 WHERE staff_no = :2', [encode_no, account[0]])
        return dataSet


if __name__ == '__main__':
    # print(DataAccess.get_xpath_menu_data('CONS_NO', '用户数据查询'))
    # 统计查询→采集建设情况→采集覆盖情况→用户采集覆盖率统计【下拉复选、单选选择】
    # print(DataAccess.getCaseData("99926400", tabName='01'))
    # print(DataAccess.refresh_all())
    # print(type(str))
    # print(DataAccess.get_case_result('999121003'))
    # val = Dict(eval(str[4]['ORG_NO']))
    # print(val['FLAG'], val['VALUE'])
    # DataAccess.refresh_all()
    # for i in  str[4:10]:
    #     print(i)
    # print(DataAccess.getTreeNode('364101038'))
    # DataAccess.getMenu('99913210')
    # print(DataAccess.get_xpath_tab_data('DATE_TIME', '999132207', '采集完整率统计'))
    # pass
    # print(DataAccess.get_menu_xpath_list('99911DB0', '01', '01'))
    DataAccess.get_account_of_sea()
    # 刷新菜单/tab对应的元素
    # DataAccess.refresh_menu_xapth('填写要刷新的菜单编号')
    # print(DataAccess.get_skip_data('999121003','备注-报文查询'))
    # print(DataAccess.get_menu_xpath_list('99912100','终端调试', '02'))
