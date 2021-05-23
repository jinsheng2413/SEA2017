# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: data_access.py
@time: 2018/5/23 0023 14:04
@desc:测试用例数据提取的数据库访问类
"""

import os

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
        node_path = pyoracle.callfunc('pkg_nrtest.get_tree_node_path', 'str',
                                      [node_value, Setting.PROJECT_NO, by_tree_node])
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
                  AND tab_name = :3 ' + (
            " AND use_share_xpath !='00'" if script_type == '01' else '') + ' ORDER BY element_sn'
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
        sql = 'SELECT encode_no, encode_pwd, staff_no, staff_name FROM tst_account WHERE encode_no IS NOT NULL'
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql)
        user_accounts = []
        for account in dataSet:
            user_accounts.append({'username': account[0], 'password': account[1],
                                  'staff_no': account[2], 'staff_name': account[3]})
            # print(user_accounts[-1], ',')
        # return user_accounts
        return [
            {'username': 'MTAwNzI4NzI=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10072872',
             'staff_name': '郑伟仁'},
            {'username': 'Z2xt', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'glm', 'staff_name': '缑工'},
            {'username': 'YWRtaW4=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'admin',
             'staff_name': 'administrator'},
            {'username': 'anVoYW5qaQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'juhanji',
             'staff_name': '巨汉基'},
            {'username': 'Y3lm', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'cyf', 'staff_name': '陈越峰'},
            {'username': 'emhvdWh1aQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'zhouhui',
             'staff_name': '周晖'},
            {'username': 'MTEw', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '110', 'staff_name': '张延生'},
            {'username': 'MDgxNw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '0817', 'staff_name': '孙玉涛'},
            {'username': 'd3Nkeg==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'wsdz', 'staff_name': '万胜'},
            {'username': 'emhhbmd5YW5saQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'zhangyanli',
             'staff_name': '张艳丽'},
            {'username': 'MTAwNDUwMTU=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10045015',
             'staff_name': '徐臣'},
            {'username': 'bGl1eGlhb3RpYW4=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'liuxiaotian',
             'staff_name': '刘晓天'},
            {'username': 'bGloYWl5YW5n', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'lihaiyang',
             'staff_name': '李海洋'},
            {'username': 'bmluZ2Jv', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'ningbo', 'staff_name': '宁卜'},
            {'username': 'dHh4', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'txx', 'staff_name': '田晓溪'},
            {'username': 'eXh5ZF93aHk=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'yxyd_why',
             'staff_name': '王海燕'},
            {'username': 'd3M=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'ws', 'staff_name': 'ws'},
            {'username': 'MTAwNDU2MDI=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10045602',
             'staff_name': '岳虎'},
            {'username': 'YW15bGVl', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'amylee', 'staff_name': '李斯琪'},
            {'username': 'dXNlcmFkbWlu', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'useradmin',
             'staff_name': '国网检查账户'},
            {'username': 'MTAwODY=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10086', 'staff_name': '测试人员'},
            {'username': 'emhlamlhbmd3YW5zaGVuZw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==',
             'staff_no': 'zhejiangwansheng', 'staff_name': 'zhejiangwansheng'},
            {'username': 'emhhbmdqaWU=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'zhangjie',
             'staff_name': 'zhangjie'},
            {'username': 'Z2pjeDIwMTI=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'gjcx2012',
             'staff_name': '高级查询用户'},
            {'username': 'OTAwMTA=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '90010', 'staff_name': '部门领导'},
            {'username': 'YWRtaW5feXc=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'admin_yw',
             'staff_name': '业务配置管理员'},
            {'username': 'Y2hheHVuMQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'chaxun1',
             'staff_name': 'chaxun'},
            {'username': 'MTAwMTE4NTI=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10011852',
             'staff_name': '张翼鸣'},
            {'username': 'Y2hheHVuNA==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'chaxun4',
             'staff_name': 'chaxun'},
            {'username': 'a2VmdXpob25neGlu', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'kefuzhongxin',
             'staff_name': '客服中心'},
            {'username': 'bGlsaWFuZ2hhbw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'lilianghao',
             'staff_name': '李良浩'},
            {'username': 'MTAwMDAxMDI=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10000102',
             'staff_name': '李红武'},
            {'username': 'MTAwNDMyMTA=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10043210',
             'staff_name': '殷庆铎'},
            {'username': 'MTAwMTc2ODQ=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10017684',
             'staff_name': '汤佩霖'},
            {'username': 'MTAwNjE0MTA=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10061410',
             'staff_name': '葛剑'},
            {'username': 'MTAwMTYwNDE=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10016041',
             'staff_name': '张凌宇'},
            {'username': 'MTAwMDU1NDA=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10005540',
             'staff_name': '陈洪涛'},
            {'username': 'MTAwNDUyNTI=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10045252',
             'staff_name': '刘洋'},
            {'username': 'MTAwNDQ4OTY=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10044896',
             'staff_name': '孙贝贝'},
            {'username': 'MTAwNDMzNTY=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10043356',
             'staff_name': '谢枫'},
            {'username': 'c3Vpc2hpd2Vp', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'suishiwei',
             'staff_name': 'suishiwei'},
            {'username': 'eXh5ZF90aHQ=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'yxyd_tht',
             'staff_name': '田海亭'},
            {'username': 'MTAwNDMyMDk=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10043209',
             'staff_name': '王莉'},
            # {'username': 'MTAwMTE4NDk=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10011849', 'staff_name': '张艳丽'},
            # {'username': 'MTAwMzczMTI=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10037312', 'staff_name': '孙志杰'},
            # {'username': 'ZG5mdw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'dnfw', 'staff_name': '电能服务'},
            # {'username': 'emNqenl5aA==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'zcjzyyh', 'staff_name': '掌抄机专用用户'},
            # {'username': 'eXps', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'yzl', 'staff_name': '易忠林'},
            # {'username': 'Y2hheHVuMg==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'chaxun2', 'staff_name': 'chaxun'},
            # {'username': 'MTAwMzcyOTI=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10037292', 'staff_name': '余志森'},
            # {'username': 'MTIzNDU2Nzg5', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '123456789', 'staff_name': '临时测试'},
            # {'username': 'eXJt', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'yrm', 'staff_name': '袁瑞铭'},
            # {'username': 'Y2hheHVuMw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'chaxun3', 'staff_name': 'chaxun'},
            # {'username': 'OTAwMDA=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '90000', 'staff_name': '殷庆铎'},
            # {'username': 'eGl0b25nY2VzaGk=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'xitongceshi', 'staff_name': '系统测试'},
            # {'username': 'YWRtaW5fc2o=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'admin_sj', 'staff_name': '审计管理员'},
            # {'username': 'bHBw', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'lpp', 'staff_name': 'lv'},
            # {'username': 'ZGlhb2R1', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'diaodu', 'staff_name': '调度'},
            # {'username': 'c2hlbmppMg==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'shenji2', 'staff_name': '审计2'},
            # {'username': 'bGl1Y2hpY2hhbw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'liuchichao', 'staff_name': '刘池超'},
            # {'username': 'c3VwZXJfYWRtaW4=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'super_admin', 'staff_name': '超级管理员'},
            # {'username': 'cXE=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'qq', 'staff_name': 'qiqi'},
            # {'username': 'bGtfYWRtaW4=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'lk_admin', 'staff_name': 'likai'},
            # {'username': 'MTIz', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '123', 'staff_name': 'qiqi'},
            # {'username': 'emhlbmd0YW8=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'zhengtao', 'staff_name': '郑涛'},
            # {'username': 'enN0aWNiYw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'zsticbc', 'staff_name': 'zst'},
            # {'username': 'ZnVzaW1pbg==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'fusimin', 'staff_name': 'fusimin'},
            # {'username': 'c3VuYmlhbw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'sunbiao', 'staff_name': 'sunbiao'},
            # {'username': 'MTEwMDEyMDA=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '11001200', 'staff_name': 'zhang'},
            # {'username': 'ano=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'jz', 'staff_name': 'jz'},
            # {'username': 'd2pi', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'wjb', 'staff_name': '王进保'},
            # {'username': 'bHk=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'ly', 'staff_name': 'ly'},
            # {'username': 'Z3Vkcw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'guds', 'staff_name': '顾东生'},
            # {'username': 'eXVzaGVuZw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'yusheng', 'staff_name': 'yusheng'},
            # {'username': 'bHh5', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'lxy', 'staff_name': 'lxy'},
            # {'username': 'c2VhMjAxNg==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'sea2016', 'staff_name': 'sea2016'},
            # {'username': 'dHNk', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'tsd', 'staff_name': 'tsd'},
            # {'username': 'c2hlbmppMQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'shenji1', 'staff_name': '审计'},
            # {'username': 'MjAxNTA4MjU=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '20150825', 'staff_name': '负荷监测'},
            # {'username': 'V1RKXzE=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'WTJ_1', 'staff_name': '查询用户'},
            # {'username': 'dGlhbnll', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'tianye', 'staff_name': '田野'},
            # {'username': 'YWRtaW5feHQ=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'admin_xt', 'staff_name': '系统管理员'},
            # {'username': 'bGRjeA==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'ldcx', 'staff_name': '欢迎领导莅临'},
            # {'username': 'bGpmMQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'ljf1', 'staff_name': '李建方'},
            # {'username': 'cGFpc2Vu', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'paisen', 'staff_name': 'paisen'},
            # {'username': 'bGpm', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'ljf', 'staff_name': '李建方'},
            {'username': 'eXl6eA==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'yyzx', 'staff_name': '运行监测'},
            {'username': 'eWl6aG9uZ2xpbg==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'yizhonglin',
             'staff_name': '易忠林'},
            {'username': 'aGJ3ag==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'hbwj', 'staff_name': '华北网局'},
            {'username': 'amlhemhpcWlhbmc=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'jiazhiqiang',
             'staff_name': 'jiazhiqiang'},
            {'username': 'bHlkeg==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'lydz', 'staff_name': '林洋电子'},
            {'username': 'Z2FubGlu', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'ganlin',
             'staff_name': 'ganlin'},
            {'username': 'c3hkcQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'sxdq', 'staff_name': '三星电气'},
            {'username': 'd2VpemhlaHVh', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'weizhehua',
             'staff_name': '卫哲华'},
            {'username': 'eHVjaGVu', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'xuchen', 'staff_name': '徐晨'},
            {'username': 'MTAwMDAwMDg=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '10000008',
             'staff_name': 'dy'},
            {'username': 'dGh0', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'tht', 'staff_name': '田海亭'},
            {'username': 'd3Rq', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'wtj', 'staff_name': 'wtj'},
            {'username': 'bGl1emloYW4=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'liuzihan',
             'staff_name': '刘子寒'},
            {'username': 'Y2pnazIwMTU=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'cjgk2015',
             'staff_name': 'cjgk2015'},
            {'username': 'bGluX3RvcA==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'lin_top',
             'staff_name': '林李平'},
            {'username': 'ODAwMDE=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '80001', 'staff_name': '杜蜀薇'},
            {'username': 'c3Vpc2hpd2VpMQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'suishiwei1',
             'staff_name': '采集系统运维项目组'},
            {'username': 'dGh0X3Rlc3Q=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'tht_test',
             'staff_name': '田海亭'},
            {'username': 'eXVlaHU=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'yuehu', 'staff_name': '部门领导'},
            {'username': 'c2hpeW9uZ2Jv', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'shiyongbo',
             'staff_name': '师永博'},
            {'username': 'eXVhbmZlbmdndWFuZw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'yuanfengguang',
             'staff_name': '部门领导_袁总'},
            {'username': 'c2VhMjAxNQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'sea2015',
             'staff_name': 'sea2015'},
            {'username': 'eHVnYW95dQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'xugaoyu',
             'staff_name': '许高宇'},
            {'username': 'dHhm', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'txf', 'staff_name': '陶晓峰'},
            {'username': 'Y2hlbmhvbmd0YW8=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'chenhongtao',
             'staff_name': '陈洪涛'}
            # {'username': 'c3VuZ2FuZw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'sungang', 'staff_name': '孙刚'},
            # {'username': 'VmluY2VudDAxMjE=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'Vincent0121', 'staff_name': '陈宁飞'},
            # {'username': 'YWRtaW5p', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'admini', 'staff_name': '有序用电测试用户'},
            # {'username': 'bGNj', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'lcc', 'staff_name': 'lcc'},
            # {'username': 'ZnVmZW5n', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'fufeng', 'staff_name': '付峰'},
            # {'username': 'MDAwMTIzNDU=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '00012345', 'staff_name': '陆洋'},
            # {'username': 'MTIzNDI1NDY=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '12342546', 'staff_name': 'zhengxiaodong'},
            # {'username': 'aHlm', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'hyf', 'staff_name': 'hyf'},
            # {'username': 'Z3VvY2h1bmJpYW8wNDE2', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'guochunbiao0416', 'staff_name': '郭春彪'},
            # {'username': 'eGlheWluZw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'xiaying', 'staff_name': '夏迎'},
            # {'username': 'd2VpdG9uZ2ppYQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'weitongjia', 'staff_name': '魏彤珈'},
            # {'username': 'emhhbmdwZW5n', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'zhangpeng', 'staff_name': '张鹏'},
            # {'username': 'MjAxNTEyMTU=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '20151215', 'staff_name': '四表集抄省级管理'},
            # {'username': 'bGl6aGVuZ2d1YW5n', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'lizhengguang', 'staff_name': '李征光'},
            # {'username': 'dHk=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'ty', 'staff_name': '田野'},
            # {'username': 'bGl1eWFu', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'liuyan', 'staff_name': '刘岩'},
            # {'username': 'd3V6aHV5dW4=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'wuzhuyun', 'staff_name': '吴竹筠'},
            # {'username': 'eGlvbmdnYW4=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'xionggan', 'staff_name': '熊敢'},
            # {'username': 'Y2pnaw==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'cjgk', 'staff_name': 'cjgk'},
            # {'username': 'MDMwNDUx', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': '030451', 'staff_name': '刘啸'},
            # {'username': 'cGdiX2RyaA==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'pgb_drh', 'staff_name': '杜瑞红'},
            # {'username': 'bGl1bmluZ25pbmc=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'liuningning', 'staff_name': '刘宁宁'},
            # {'username': 'dGVzdF9neWs=', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'test_gyk', 'staff_name': 'jj'},
            # {'username': 'bG9seTMyMQ==', 'password': 'NOzIzJv2mQTdZwfDP+jc0A==', 'staff_no': 'loly321', 'staff_name': 'loly'}
        ]

    @staticmethod
    def encode_account(js):
        sql = 'SELECT staff_no FROM tst_account WHERE encode_no IS NULL'
        pyoracle = PyOracle.getInstance()
        dataSet = pyoracle.query(sql)
        fun_base64 = execjs.compile(js)  # 执行JavaScript脚本
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
