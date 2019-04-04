# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: assert_result.py
@time: 2019/1/15 0015 9:32
@desc:江西期间整改调试，并优化--ljf
"""
import codecs
import os
import platform
from time import sleep

from selenium.webdriver.common.by import By

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.logger import Logger
from com.nrtest.common.user_except import AssertError
from com.nrtest.common.utils import Utils

logger = Logger(logger='AssertResult').getlog()

# assert_type值共有3位：第1位：0-杂项校验；1-弹窗校验；2-菜单校验；3-Tab页校验
#                     第2位：针对杂项校验没意义，弹窗、菜单：0-普通校验；   1-多链接；      2-业务操作；
#                                              Tab页：0-普通Tab页；  1-Tab页内套Tab；2-业务操作
#                     第3位：针对杂项校验没意义，   弹窗类：0-固定弹窗标题；1-动态弹窗标题
#                                              菜单类：0-普通菜单；   1-TST_MENU中不存在的菜单页
ASSERT_TYPES = {
    # 【杂项校验】, '没查询结果', '【{}】查询条件与查询结果【{}】值不一致', '【{}】供电单位下钻出错', '目标页面元素【{}】值与期望值【{}】不一致'
    #     , '弹窗标题【{}】与期望值【{}】不一致', '菜单标题【{}】与期望值【{}】不一致'
    '011': '有无查询结果',
    '012': '查询结果期望值校验',
    '013': '供电单位下钻校验',
    '031': '目标页面元素值校验',
    # 【弹窗校验】
    '100': '固定标题弹窗校验',
    '101': '动态标题弹窗校验',
    '110': '一列多链接弹窗校验（固定）',
    '111': '一列多链接弹窗校验（动态）',
    '120': '弹窗业务操作校验（固定）',
    '121': '弹窗业务操作校验（动态）',
    # 【菜单校验】
    '200': '跳转至菜单校验]',
    '201': '跳转至类菜单校验',  # TST_MENU中不存在的菜单页
    '210': '一列多链接菜单校验',
    '220': '菜单业务操作校验',
    # 【Tab页校验】
    '300': 'Tab页校验',
    '310': 'Tab页内套多个Tab页校验',
    '320': 'Tab页业务操作校验'}


# 校验新方法
class AssertResult():
    def __init__(self, call_from):
        self.tst_inst = call_from

    def save_img(self, img_path, img_name):
        self.tst_inst.save_img(img_path, img_name)

    def popup(self, img_path, img_name, dlg_title='', *args):
        return self.tst_inst.popup(img_path, img_name, dlg_title, *args)

    def assert_context(self, locator):
        """
        断言
        :return: 布尔返回值
        """
        # 02-没查询结果的提示弹窗；
        if self.tst_inst.case_para['POPUP_TYPE'] == '02':
            is_pass = True
        else:
            el = self.tst_inst._find_displayed_element(locator)
            is_pass = bool(el)
        return is_pass

    def assertValue(self, case_result, col_pos_info):
        """
        :param case_result:以，为分隔符，第一位是显示区唯一列明，第二位是要校验值的列明，第三位是校验值
        :return:
        """
        is_find, first_row_idx, row_cnt = self.query_records(case_result[0])
        if is_find:
            match_cnt = 0
            displayLineElement = (By.XPATH,
                                  '(//*[text()="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)[{}]/td[{}]//*[contains(text(),"{}")]')

            col_name = col_pos_info['COL_NAME']
            # link_tag = col_and_link_tag[1] if assert_type[1] == '1' else None  # 一列多链接【26】
            # link = ('链接：', link_tag) if bool(link_tag) else ('', '')
            compare_result = ['--', col_name, '', '', self.assert_info, []]

            for i in range(1, row_cnt + 1):
                # 显示区结果的每一行对应列的数据的xpath
                locator = self.tst_inst.format_xpath(displayLineElement,
                                                     (case_result[0], i + first_row_idx, col_pos_info['COL_IDX'], case_result[2]))
                assert_rslt = self.assert_context(locator)
                if assert_rslt:
                    match_cnt += 1
                else:
                    logger.error('第{}行，{}列显示的值与{}不一致\r'.format(i, case_result[1], case_result[2]))
                    compare_result[-1].append([case_result[2], '第{}行，{}列与期望值不一致'.format(i, case_result[1]), '不通过'])
                    break

            is_pass = match_cnt == row_cnt
            if is_pass:
                compare_result[-1].append([case_result[2], '{}列与期望值一致'.format(case_result[1]), '通过'])
            return is_pass, compare_result, False
        else:
            raise AssertError('查询没记录，校验失败！')

    def assert_page_name(self, page_name):
        """
        判断跳转的页面的菜单名是否正确
        :param page_name:
        :return:
        """
        xpath = self.tst_inst.format_xpath(AssertResultLocators.MENU_NAME, page_name)
        return self.assert_context(xpath)

    @BeautifulReport.add_popup_img(6)
    def skip_to(self, case_result, col_pos_info, link_tag=None, is_deal_after=False, dlg_title=''):
        """
        链接跳转:跳转到另一个页面
        :param case_result: 查询结果校验列表内容：定位列名；校验列名；期望值；定位行号;是否特殊处理
        :param col_pos_info:  数据内容{'COL_IDX':0, 'EL_COL':None, 'EL_FIRST':None, 'COL_IS_HIDED':True}
        :param link_tag: 一个单元格多个链接时的链接名
        :param is_deal_after: 是否对跳转后的查询结果进行判断处理：目前仅用于供电单位下钻判断处理
        :param dlg_title: 弹窗标题
        :return:
        """
        #  IS_SKIPED：能点击，但不一定会跳转（没link时）；CLICKABLE：可点击，且不会报错
        skip_info = {'IS_SKIPED': True, 'LINK_TEXT': None, 'EL_A': None, 'CLICKABLE': False, 'EL_AFTER_A': None, 'AFTER_TEXT': '',
                     'AFTER_ACTION': '01', 'DLG_TITLE': dlg_title}
        try:
            # 按下面代码执行会报这个错：'FirefoxWebElement' object does not support indexing
            # el_link = el_data_rows[int(case_result[3])].find_elements_by_xpath('./td[{}]//a'.format(col_pos_info['COL_IDX']))

            is_multi_link = bool(link_tag)  # 判断某列是否有多个链接
            if is_multi_link:
                link_xpath = self.tst_inst.format_xpath_multi(AssertResultLocators.QUERY_RESULT_ROW_COL_LINKS,
                                                              (case_result[0], case_result[3], col_pos_info['COL_IDX'], link_tag), True)
            else:
                link_xpath = self.tst_inst.format_xpath_multi(AssertResultLocators.QUERY_RESULT_ROW_COL,
                                                              (case_result[0], int(case_result[3]) + col_pos_info['HIDE_ROWS'],
                                                               col_pos_info['COL_IDX']), True)
            el_link = self.tst_inst._find_displayed_element(link_xpath)

            if is_multi_link:
                skip_info['EL_A'] = el_link
            else:
                # font为没有链接(下划线）的跳转项
                skip_info['EL_A'] = el_link.find_element_by_xpath('.//a | .//font')

            skip_info['LINK_TEXT'] = el_link.text
            skip_info['CLICKABLE'] = bool(skip_info['EL_A'])
            self.tst_inst.scrollTo(el_link)
            if bool(skip_info['EL_A']):
                skip_info['EL_A'].click()

            # 休眠N秒，等待跳转页面加载: WAIT_FOR_TARGET
            seconds = case_result[5]
            if seconds > 0:  # 按loading元素等待，超时不抛异常
                try:
                    self.tst_inst.query_timeout(timeout_seconds=seconds)
                except:
                    pass
            else:
                sleep(abs(seconds))

            if is_deal_after:  # 目前仅用于供电单位下钻判断处理
                el_after_click = self.tst_inst._find_displayed_element(link_xpath)
                if bool(el_after_click):
                    try:
                        el_a = el_after_click.find_element_by_xpath('.//a | .//font')
                    except:
                        el_a = None
                    # AFTER_ACTION：01-没查询结果；02-查询结果有链接；03-有查询结果，但没链接；
                    skip_info['AFTER_ACTION'] = '02' if bool(el_a) else '03'
                    skip_info['EL_AFTER_A'] = el_a
                    skip_info['AFTER_TEXT'] = el_after_click.text
                else:
                    skip_info['AFTER_ACTION'] = '01'
        except Exception as ex:
            print('跳转验证失败:' + ex.__str__())
            skip_info['IS_SKIPED'] = False

        return skip_info

    def calc_col_idx(self, loc_col_name, col_name, head_idx=1, idx=1):
        """
        计算所给列名（col_name）在表格中的所处位置【该函数已移至base_page】
        --------------------loc_col_name[0]-----------------|-col_name[1]-|----[2]-------|--要定位的行号[3]--|-----[4]-----
        nvl(tab_column_name, column_name) AS tab_column_name, column_name, expected_value, row_num,          is_special
        :param loc_col_name: 能唯一定位表头的关键列名
        :param col_name: 计算列位置的列名
        :param idx: 第idx个可见对象
        :return: 返回：列位置，列是否可见以及第一列带标签的列
        """
        return self.tst_inst.calc_col_idx(loc_col_name, col_name, head_idx, idx)

    def split_double_column(self, column_idx):
        """
        表头存在多个重复列名时的定位处理：COLMUN_NAME - EXCEPTED_VALUE
        用例 ID：999262101 菜单名--非统调电厂接入统计
        :return:
        """
        ls_col_idx = [1, 1]
        if column_idx:
            ls_col_idx = column_idx.split('-')
            if not bool(ls_col_idx[0]):
                ls_col_idx[0] = 1
            elif len(ls_col_idx) == 1:
                ls_col_idx.append(1)
        return ls_col_idx

    def check_query_result(self, para):
        """
        查询结果校验处理
        :param para: 用例数据
        :return: 返回校验结果
        """
        # @TODO 启用新的校验输出格式
        if True:
            return self.check_query_result_new(para)

        esplain = {
            '11': '显示区未查询出结果',
            '12': '按条件查询出的结果与期望值不一致',
            '21': '跳转菜单页面不正确',
            '22': '跳转弹窗不正确',
            '23': '跳转tab页不正确',
            '24': '跳转弹窗的名称带的值不正确',
            '25': '跳转到新的菜单页，但不携带值错误',  # 这里的菜单是指没有menu_no的菜单 tst_case_id = 9993110012
            '26': '单列数据有两个跳转',
            '27': 'tab页套多个tab页',
            '28': '供电单位下钻后没查询结果或下钻出错',
            '31': '查询详细信息的输入框的值与期望结果不一致'
        }
        # @TODO
        # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$请删除我')
        # if True:
        #     return True

        case_id = para['TST_CASE_ID']
        ls_check_rslt = {}
        case_results = DataAccess.get_case_result(case_id)
        for i, row in enumerate(case_results):  # 根据rslt有几个值来判断要做几次校验
            self.dlg_info = None
            assert_type = row[0]
            case_result = row[1:]

            ls_col_idx = self.split_double_column(case_result[8])

            is_calc_col_idx = assert_type not in ['11', '31']
            if is_calc_col_idx:
                col_and_link_tag = self.special_deal(case_result[4], case_result[1])
                col_pos_info = self.calc_col_idx(case_result[0], col_and_link_tag[0], int(case_result[6]), int(ls_col_idx[0]))
            logger.info('*******' + case_id + '*********校验类别：{}；定位列名：{}；校验列名：{}；期望值：{}；定位行号：{};是否特殊处理：{}\r'.format(*row))
            if assert_type == '11':  # 【OK】
                locator = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT, case_result[0])
                assert_rslt = self.assert_context(locator)
            elif assert_type == '12':  # 判断值是否准确,item截取字符串，在转换成列表
                assert_rslt = self.assertValue(case_result, col_pos_info)
            elif assert_type in ('21', '23', '25', '26', '27'):  # 跳转菜单或Tab页; 23-Tab页；其他-菜单页
                # assert_rslt = self.clickSkip(case_result, para)
                # assert_rslt = self.skip_menu_tab_page(assert_type, para, case_result, col_pos_info)
                assert_rslt = self.skip_menu_tab_page(assert_type, para, case_result, col_pos_info, col_and_link_tag)
            elif assert_type in ('22', '24'):  # 跳转弹窗
                assert_rslt = self.skip_windows_page(assert_type, case_result, col_pos_info, col_and_link_tag)
            # elif assert_type == '23':  # 跳转tab页
            #     # assert_rslt = self.skip_tab_page(case_result, para)
            #     assert_rslt = self.skip_menu_tab_page(assert_type, para, case_result, col_pos_info)
            # elif assert_type == '24':
            #     # assert_rslt = self.tab_skip_into_window(case_result, col_pos_info)
            #     assert_rslt = self.skip_windows_page(assert_type, case_result, col_pos_info, True)
            # elif assert_type == '25':  # 【OK】 # 跳转到新的菜单页，但不携带值
            #     assert_rslt = self.skip_new_menu(case_result, col_pos_info)
            # elif assert_type == '26':  # 【OK】 # 单列数据有两个跳转
            #     # assert_rslt = self.skip_two_link(case_result, para)
            #
            #     # link_xpath = self.tst_inst.format_xpath_multi(AssertResultLocators.QUERY_RESULT_ROW_COL_LINKS,
            #     #                                               (case_result[0], case_result[3], col_pos_info['COL_IDX'], col_and_link_tag[1]), True)
            #     # assert_rslt = self.skip_menu_tab_page(assert_type, para, case_result, col_pos_info, True, link_xpath=link_xpath)
            #     assert_rslt = self.skip_menu_tab_page(assert_type, para, case_result, col_pos_info, col_and_link_tag)
            # elif assert_type == '27':  # 【OK】
            #     # assert_rslt = self.skip_more_tab_link(case_result, para)
            #     assert_rslt = self.skip_menu_tab_page(assert_type, para, case_result, col_pos_info)
            elif assert_type == '28':  # 供电单位层层下钻
                assert_rslt = self.check_of_org_drill_down(assert_type, case_result, col_pos_info)
            elif assert_type == '31':
                assert_rslt = self.assertInput(case_id, case_result)

            ls_check_rslt[i] = {assert_type: [assert_rslt, case_result[1]]}

        result = True
        # 处理判断结果，具体那一步出错
        ls_check_rslt_values = ls_check_rslt.values()
        for item in ls_check_rslt_values:
            for key, value in item.items():
                if not value[0]:
                    if is_calc_col_idx:
                        err_info = '校验列【{}】时报错，校验类别为：{}，错误信息：{}'.format(value[1], key, esplain[key])
                    else:
                        err_info = '校验类别为：{}，错误信息：{}'.format(key, esplain[key])
                    logger.error(err_info + '\r')  # 出错具体原因
                    print(err_info + '</br>')
                    result = False
        return result

    def check_query_result_new(self, para):
        """
        查询结果校验处理
        :param para: 用例数据
        :return: 返回校验结果
        """
        case_id = para['TST_CASE_ID']
        ls_check_rslt = []
        case_results = DataAccess.get_case_result(case_id)
        for row in case_results:  # 根据rslt有几个值来判断要做几次校验
            self.dlg_info = None
            assert_type = row[0]
            case_result = row[1:]

            # @TODO 临时转换，后续需删除
            trans = {'11': '011', '12': '012', '28': '013', '31': '031',
                     '22': '100', '24': '101', '21': '200',
                     '25': '201', '26': '210', '23': '300', '27': '310'}
            try:
                assert_type = trans[assert_type]
            except:
                pass

            self.assert_info = assert_type + '-' + ASSERT_TYPES[assert_type]

            ls_col_idx = self.split_double_column(case_result[8])

            is_calc_col_idx = assert_type not in ['011', '031']
            if is_calc_col_idx:
                col_and_link_tag = self.special_deal(case_result[4], case_result[1])
                col_pos_info = self.calc_col_idx(case_result[0], col_and_link_tag[0], int(case_result[6]), int(ls_col_idx[0]))
            logger.info('用例ID：{}；校验类别：{}；定位列名：{}；校验列名：{}；期望值：{}；定位行号：{};是否特殊处理：{}\r'.format(case_id, *row))
            if assert_type == '011':
                locator = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT, case_result[0])
                is_pass = self.assert_context(locator)
                compare_result = ['--', '--', '', '', self.assert_info, []]
                if is_pass:
                    compare_result[-1].append(['有查询结果', '有查询结果', '通过'])
                else:
                    compare_result[-1].append(['有查询结果', '没查询结果', '不通过'])
                assert_rslt = is_pass, compare_result, False

            elif assert_type == '012':  # 判断值是否准确,item截取字符串，在转换成列表
                assert_rslt = self.assertValue(case_result, col_pos_info)

            elif assert_type == '013':  # 28: 供电单位层层下钻 X
                assert_rslt = self.check_of_org_drill_down(assert_type, case_result, col_pos_info)

            elif assert_type == '031':
                assert_rslt = self.assertInput(case_id, case_result)

            elif assert_type[0] == '1':  # 弹窗校验
                assert_rslt = self.check_of_popup(assert_type, case_result, col_pos_info, col_and_link_tag)

            elif assert_type[0] in ['2', '3']:  # 菜单、Tab页校验
                assert_rslt = self.check_of_skip_menu_or_tab(assert_type, para, case_result, col_pos_info, col_and_link_tag)

            ls_check_rslt.append([assert_type, assert_rslt, case_result[1]])

        result = True
        for check_rslt in ls_check_rslt:
            assert_type = check_rslt[0]
            if isinstance(check_rslt[1], tuple):
                if not check_rslt[1][0]:
                    self.output_compare_list(*check_rslt[1][1:])
                    result = False
            elif not check_rslt[1]:  # 校验不通过
                if is_calc_col_idx:
                    err_info = '“{}”列校验时报错，校验类别：{}，校验内容：{}'.format(check_rslt[2], assert_type, ASSERT_TYPES[assert_type])
                else:
                    err_info = '查询结果校验时报错，校验类别：{}，校验内容：{}'.format(assert_type, ASSERT_TYPES[assert_type])
                logger.error(err_info + '\r')  # 出错具体原因
                print(err_info + '</br>')
                result = False
        return result

    def assertInput(self, case_id, case_result):
        """
        获取单个
        :param case_result:
        :param case_id:
        :return:
        """
        xpath = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT_BY_INPUT, (case_result[0], case_result[1]))
        el = self.tst_inst._find_displayed_element(xpath)
        val = el.get_attribute('value')
        if case_result[2] == val:
            logger.info('查询详细信息的输入框的值与期望结果一样')
            is_pass = True
        else:
            logger.error('查询详细信息的输入框的值与期望结果不一致')
            is_pass = False

        col_name = case_result[1]
        compare_result = [case_result[3], col_name, '', '', self.assert_info, []]
        compare_result[-1].append([case_result[2], val, ('通过' if is_pass else '不通过')])
        # if not is_pass:
        #     self.output_compare_list(compare_result, False)
        return is_pass, compare_result, False

    def skip_windows_page(self, assert_type, case_result, col_pos_info, col_and_link_tag):
        """
        窗口跳转
        :param case_result: 以，为分隔符，定位列名；校验列名；期望值(校验值)；定位行号;是否特殊处理；等待目标跳转对象时间
        :param col_pos_info:
        :return:
        """

        # 【滚动到链接列名所在位置】
        # 计算链接列名列序号（包括隐藏列）  --【终端信息维护】  【终端调试信息】
        # 定位列名；校验列名；期望值；定位行号;是否特殊处理
        is_find, first_row_idx, row_cnt = self.query_records(case_result[0])
        if is_find:
            col_pos_info['HIDE_ROWS'] = first_row_idx
            self.tst_inst.scrollTo(col_pos_info['EL_COL'])
            # 获取弹窗标题名
            if assert_type == '24':  # 获取弹窗的动态窗口标题名
                ls_col_idx = self.split_double_column(case_result[8])
                col_idx = self.calc_col_idx(case_result[0], case_result[2], int(case_result[6]), int(ls_col_idx[1]))['COL_IDX']
                xpath = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT_ROW_COL, (case_result[0], case_result[3], col_idx))
                dlg_title = self.tst_inst.driver.find_element(*xpath).text
            else:  # 固定窗口标题名
                dlg_title = case_result[2]

            # 跳转到目标页
            skip_info = self.skip_to(case_result, col_pos_info, dlg_title=dlg_title)
            if skip_info['CLICKABLE']:
                # 弹窗信息
                self.dlg_info = self.tst_inst.get_skip_except_info('01')
                is_skiped = dlg_title in self.dlg_info if bool(self.dlg_info) else False
            else:
                is_skiped = False
            self.tst_inst.scrollTo(col_pos_info['EL_FIRST'])
        else:
            raise AssertError('没查询结果， 跳转验证失败！！')
        return is_skiped

    def check_of_popup(self, assert_type, case_result, col_pos_info, col_and_link_tag):
        """
        弹窗校验
        :param case_result: 以，为分隔符，定位列名；校验列名；期望值(校验值)；定位行号;是否特殊处理；等待目标跳转对象时间
        :param col_pos_info:

        :return:
        """

        # 【滚动到链接列名所在位置】
        # 计算链接列名列序号（包括隐藏列）  --【终端信息维护】  【终端调试信息】
        # 定位列名；校验列名；期望值；定位行号;是否特殊处理
        is_find, first_row_idx, row_cnt = self.query_records(case_result[0])
        if is_find:
            col_pos_info['HIDE_ROWS'] = first_row_idx

            col_name = col_pos_info['COL_NAME']
            link_tag = col_and_link_tag[1] if assert_type[1] == '1' else None  # 一列多链接【26】
            link = ('链接：', link_tag) if bool(link_tag) else ('', '')
            compare_result = [case_result[3], col_name, *link, self.assert_info, []]

            self.tst_inst.scrollTo(col_pos_info['EL_COL'])

            # 获取弹窗标题名
            if assert_type[2] == '1':  # 获取弹窗的动态窗口标题名【24】
                ls_col_idx = self.split_double_column(case_result[8])  # 重复列名时，取重复列中的第idx个列

                col_idx = self.calc_col_idx(case_result[0], case_result[2], int(case_result[6]), int(ls_col_idx[1]))['COL_IDX']
                xpath = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT_ROW_COL, (case_result[0], case_result[3], col_idx))
                dlg_title = self.tst_inst.driver.find_element(*xpath).text
            else:  # 获取固定窗口标题名
                dlg_title = case_result[2]

            # 跳转到目标页
            link_tag = col_and_link_tag[1] if assert_type[1] == '1' else None  # 多链接【26】
            skip_info = self.skip_to(case_result, col_pos_info, link_tag, dlg_title=dlg_title)
            if skip_info['CLICKABLE']:
                # 取得弹窗信息，并判断是否与期望值相符
                self.dlg_info = self.tst_inst.get_skip_except_info('01')
                is_skiped = dlg_title in self.dlg_info if bool(self.dlg_info) else False
            else:
                is_skiped = False
            compare_result[-1].append([dlg_title, self.dlg_info, ('通过' if is_skiped else '不通过')])
            self.tst_inst.scrollTo(col_pos_info['EL_FIRST'])
            # if not is_skiped:
            #     self.output_compare_list(compare_result, False)
        else:
            raise AssertError('没查询结果， 跳转验证失败！！')
        return is_skiped, compare_result, False

    # def skip_new_menu(self, case_result, col_pos_info):
    #     """
    #     跳转到新的菜单，但不需要校验值
    #     :param case_result:
    #     :param col_pos_info:
    #     :return:
    #     """
    #     is_find, first_row_idx, row_cnt = self.query_records(case_result[0])
    #     if is_find:
    #         col_pos_info['HIDE_ROWS'] = first_row_idx
    #         self.skip_to(case_result, col_pos_info)
    #         res = self.assert_page_name(case_result[2])
    #         self.tst_inst.menuPage.closePage(page_name=case_result[2])
    #     else:
    #         raise AssertError('没查询结果， 跳转验证失败！！')
    #
    #     return res

    def get_data_of_skip_before(self, case_data, case_result, map_rela_rslt):
        """
        -------0--------|----1----|----2-------|----3---|----4-----|--5---|--------6-------|----7-----|------8-----|-----9-----|---10---|----11-----|-----12-------|-------13--------|----14----
        *TAB_COLUMN_NAME TAB_NAME  *COLUMN_NAME *ROW_NUM XPATH_TYPE XPATH   TARGET_TAB_NAME TRANS_TYPE TARGET_XPATH TRANS_VALUE IS_TRANS ELEMENT_SN  TARGET_MENU_NO  target_menu_name  column_idx
           是否在线   终端版本召测	查看报文	  1	       02	   终端地址	     01	            00	   TMNL_ADDR		           0	    3         99934410

        :param case_data:
        :param case_result:
        :param map_rela_rslt:
        :return:
        """
        skip_data_before = []
        for map_rela in map_rela_rslt:
            xpath_name = ''
            # 获取查询条件输入框的值
            xpath_type = map_rela[4]
            if xpath_type == '01':  # 页面元素类型：XPATH_TYPE 【01-查询条件（XPATH)】;02-表格列对应值;03-表格列名;04-读取统计数与明细对比
                # 把查询条件的xpath转换为对应查询条件中文名
                menu_xpath_data = DataAccess.get_menu_xpath_data(case_data['MENU_NO'], case_data['PAGE_TAB_NAME'], map_rela[5])
                xpath_name = menu_xpath_data[0] + '(Q)'
                if menu_xpath_data[1] in ('04', '05', '07'):
                    val = self.tst_inst.get_para_value(case_data[map_rela[5]])
                else:
                    val = self.tst_inst.get_input_val(menu_xpath_data[0], menu_xpath_data[1], menu_xpath_data[2], menu_xpath_data[3])
                skip_data_before.append([val, xpath_name])
            elif xpath_type in ['02', '04']:  # 提取跳转前的表格列对应值
                xpath_name = map_rela[5] + '(C)'
                loc_col_name = case_result[0]
                column_idx = int(map_rela[14]) if bool(map_rela[14]) else 1
                col_idx = self.calc_col_idx(loc_col_name, map_rela[5], int(case_result[6]), column_idx)['COL_IDX']  # XPATH
                locator = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT_ROW_COL, (loc_col_name, case_result[3], col_idx))
                val = self.tst_inst.driver.find_element(*locator).text
                skip_data_before.append([val, xpath_name])
            elif xpath_type == '03':
                xpath_name = map_rela[5] + '(C)'
                skip_data_before.append([case_result[1], xpath_name])
        return skip_data_before

    def get_data_of_skip_after(self, case_result, map_rela_rslt, is_menu, skip_data_before):
        """
        -------0--------|----1----|----2-------|----3---|----4-----|--5---|--------6-------|----7-----|------8-----|-----9-----|---10---|----11-----|-----12--------|------13-------|
        *TAB_COLUMN_NAME TAB_NAME  *COLUMN_NAME *ROW_NUM XPATH_TYPE XPATH   TARGET_TAB_NAME TRANS_TYPE TARGET_XPATH TRANS_VALUE IS_TRANS ELEMENT_SN  TARGET_MENU_NO  TARGET_MENU_NAME
           是否在线   终端版本召测	查看报文	  1	       02	   终端地址	     01	            00	   TMNL_ADDR		           0	    3         99934410
        :param case_result:
        :param map_rela_rslt:
        :param menu_name: True-跳转目标为菜单；False-跳转目标为Tab页
        :return:
        """
        skip_data_after = []
        for i, map_rela in enumerate(map_rela_rslt):
            xpath_type = map_rela[4]  # XPATH_TYPE
            if xpath_type == '04' and map_rela[8] is None:  # 读取跳转页的查询结果总数  TARGET_XPATH
                try:
                    # *******************@TODO 弹窗窗口的记录总数需验证测试******
                    loc = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT_TOTAL_ROW,
                                                     (case_result[2] if is_menu else self.tst_inst.menu_name))
                    total_text = Utils.replace_chrs(self.tst_inst._find_displayed_element(loc).text, ' \r\n\t')
                    val = total_text.split('/')[-1]
                    skip_data_after.append([val, '记录总数'])
                except:
                    skip_data_after.append(['0', '记录总数'])
            else:
                try:
                    menu_xpath_data = DataAccess.get_menu_xpath_data(map_rela[12], map_rela[6],
                                                                     map_rela[8])  # TARGET_MENU_NO / TARGET_TAB_NAME/  TARGET_XPATH
                    if menu_xpath_data[1] in ('04', '05', '07'):  # 单选框/复选框处理 [i][0]:值/xpath_name
                        trans_to_val = self.tst_inst.case_para[map_rela[8] + '_TRANS']
                        if bool(trans_to_val):
                            value = trans_to_val
                        else:
                            value = skip_data_before[i][0]
                        # val = self.tst_inst.get_input_val(skip_data_before[i][0], menu_xpath_data[1], menu_xpath_data[2], map_rela[13])
                        val = self.tst_inst.get_input_val(value, menu_xpath_data[1], menu_xpath_data[2], menu_xpath_data[3], map_rela[13])
                    else:
                        val = self.tst_inst.get_input_val(menu_xpath_data[0], menu_xpath_data[1], menu_xpath_data[2], menu_xpath_data[3],
                                                          map_rela[13])

                    skip_data_after.append([val, menu_xpath_data[0] + '(Q)'])
                except:
                    logger.error('跳转的新页面/窗口需配置等待加载时间或TST_COL_LINK_RELA.TARGET_XPATH={}配置错误！'.format(map_rela[8]))
                    return None
        return skip_data_after

    def skip_data_check(self, col_pos_info, map_rela_rslt, row_idx, skip_data_before, skip_data_after):

        col_idx = col_pos_info['COL_IDX'] - col_pos_info['HIDE_COLS']
        info = '跳转坐标（{}行,{}列）element_sn:{}跳转前:xpath:{}、值：{}-----跳转后:xpath:{}、值：{}'
        try:
            all_val = '全部'
            is_pass = True
            for data_before, data_after, map_rela in zip(skip_data_before, skip_data_after, map_rela_rslt):
                # bef_name = data_before[1]
                data_before = data_before[0]
                # aft_name = data_after[1]
                data_after = data_after[0]

                xpath_type = map_rela[4]
                trans_type = map_rela[7]  # 转换类型(TRANS_TYPE)：00-不转换；01-直接转换为对应值;02-包含关系;03-月时间转换为日时间
                is_skip_correct = False
                if trans_type == '01':
                    data_before = map_rela[9]

                if (all_val in data_before and all_val in data_after) or (data_before == '' and all_val in data_after) or (
                        all_val in data_before and data_after == ''):  # 处理“全部”选项
                    is_skip_correct = True
                elif data_before == data_after:
                    is_skip_correct = True
                elif (trans_type == '12' and data_after in data_before) or (
                        trans_type == '13' and data_before in data_after):  # 包含关系：12-跳转前包含跳转后的；13-跳转后包含跳转前的
                    is_skip_correct = True
                elif trans_type in ('10', '11'):  # 月时间转换为月初/月末日期
                    day_begin, day_end = Utils.get_day_range_of_month(data_before)
                    data_before = day_begin if trans_type == '10' else day_end
                    if data_before == data_after:
                        is_skip_correct = True
                elif trans_type in ('15', '16'):  # 15 - 终端地址转资产号；16 - 终端资产号转地址
                    data_before = self.data_trans(trans_type, data_before)
                elif trans_type == '14' and data_before != '0' and data_after != '没有数据':  # 基本应用→数据采集管理→采集质量分析→采集成功率:采集成功率统计  经“采集成功率”列跳转到明细页面
                    is_skip_correct = True
                elif xpath_type == '04' and data_before == '0' and data_after == '没有数据':  # 取所在跳转的统计数据值
                    data_after = '0'
                    is_skip_correct = True


                info_rlt = info.format(row_idx, col_idx, map_rela[11], map_rela[5], data_before, map_rela[8],
                                       data_after)  # ELEMENT_SN / XPATH / TARGET_XPATH
                if is_skip_correct:
                    logger.info(info_rlt)
                else:
                    is_pass = False
                    err_info = '跳转传值错误:' + info_rlt
                    logger.error(err_info)
                    print('</br>' + err_info + '</br>')
        except Exception as ex:
            print('</br>跳转数据比对：跳转前--', skip_data_before)
            print('</br>--跳转后--', skip_data_after)
            print('</br>--跳转关系', map_rela_rslt)
            raise ex
        return is_pass

    def trans_to_trs(self, skip_map_rela, is_menu_or_tab=True):
        tr6 = "<tr style='height:20.0pt'>" \
              "<td class=xl72 style='width: 15%;'>{}</td>" \
              "<td class=xl72 style='width: 15%;'>{}</td>" \
              "<td class=xl72 style='width: 15%;'>{}</td>" \
              "<td class=xl72 style='width: 15%;'>{}</td>" \
              "<td class=xl72 style='width: 30%;'>{}</td>" \
              "<td class=xl72 style='width: 10%;text-align: center'>{}</td>" \
              "</tr>"
        tr3 = "<tr style='height:20.0pt'>" \
              "<td class=xl72 style='width: 40%;'>{}</td>" \
              "<td class=xl72 style='width: 40%;'>{}</td>" \
              "<td class=xl72 style='width: 20%;text-align: center'>{}</td>" \
              "</tr>"
        trs = []
        tr = tr6 if is_menu_or_tab else tr3
        for row in skip_map_rela:
            trs.append(tr.format(*row))
        return trs

    def output_compare_list(self, compare_result, is_menu_or_tab=True):
        """
        输出跳转比对清单
        :param compare_result: 跳转比对结果
        """
        template_file = 'compare_list' if is_menu_or_tab else 'expect_popup_or_value'
        compare_list_path = os.path.dirname(__file__) + '{}{}'.format(('/' if platform.system() != 'Windows' else '\\'), template_file)

        with codecs.open(compare_list_path, 'r', 'utf-8') as file:
            body = file.readlines()

        i = 0
        for row_idx, item in enumerate(body):
            item = item.replace('\r\n', '')
            if item.find('{}') >= 0:
                body[row_idx] = item.format(compare_result[i])
                i += 1
            else:
                body[row_idx] = item

        body += self.trans_to_trs(compare_result[-1], is_menu_or_tab)
        if compare_result[1][-1] == '*':
            body.append('<tr style=\'height:20.0pt\'><td colspan={}>说明：*--取第n个重复列</td></tr>'.format(6 if is_menu_or_tab else 3))
        body.append('</table>')
        print('\n'.join(body))

    def skip_data_compare(self, col_pos_info, link_tag, map_rela_rslt, row_num, skip_data_before, skip_data_after):
        """
        跳转前后数据比对，如果一致则跳转成功，否则失败
        :param col_pos_info:
        :param link_tag: 一列有多个链接
        :param map_rela_rslt:
        :param row_num: 跳转时选择的查询结果行号
        :param skip_data_before:
        :param skip_data_after:
        :return:
        """
        col_idx = col_pos_info['COL_IDX'] - col_pos_info['HIDE_COLS']

        col_name = col_pos_info['COL_NAME']
        # compare_result = {'ROW_NUM': row_num, 'COL_NAME':col_name, 'LINK': ('链接：' if bool(link_tag) else ''), 'LINK_TAG': link_tag, 'SKIP_MAP_RELA': []}
        link = ('链接：', link_tag) if bool(link_tag) else ('', '')
        compare_result = [row_num, col_name, *link, self.assert_info, []]

        info = '跳转坐标（{}行,{}列）element_sn:{}跳转前:xpath:{}、值：{}-----跳转后:xpath:{}、值：{}'
        try:
            all_val = '全部'
            is_pass = True
            dict_trans_type = DataAccess.get_data_dictionary('TRANS_TYPE', '03', True)
            for data_before, data_after, map_rela in zip(skip_data_before, skip_data_after, map_rela_rslt):
                bef_name = data_before[1]
                data_before = data_before[0]
                aft_name = data_after[1]
                data_after = data_after[0]

                xpath_type = map_rela[4]
                trans_type = map_rela[
                    7]  # 转换类型(TRANS_TYPE)：00-不转换；01-直接转换为对应值;10-月时间转换为月初；11--月时间转换为月末；12-跳转前包含跳转后的；13-跳转后包含跳转前的；14-跳转对象有记录即可（采集成功率-->明细）；15-终端地址转资产号；16-终端资产号转地址';
                is_skip_correct = False
                xpath_trans = self.tst_inst.case_para[map_rela[5] + '_TRANS']
                if trans_type == '01':
                    bef = data_before
                    data_before = map_rela[9]
                    aft = data_after
                elif bool(xpath_trans):
                    bef = data_before
                    data_before = xpath_trans
                    aft = data_after
                else:
                    bef = data_before
                    aft = data_after

                if all_val in data_before and all_val in data_after:  # 处理“全部”选项
                    # bef = data_before
                    # aft = data_after
                    is_skip_correct = True
                elif (data_before == '' and all_val in data_after):  # 处理“全部”选项
                    bef = '\'\'→' + all_val
                    # aft = data_after
                    is_skip_correct = True
                elif (all_val in data_before and data_after == ''):  # 处理“全部”选项
                    # bef = data_before
                    aft = '\'\'→' + all_val
                    is_skip_correct = True

                elif data_before == data_after:
                    if trans_type == '01':
                        bef += '→' + map_rela[9]
                    elif bool(xpath_trans):
                        bef += '→' + xpath_trans
                    # else:
                    #     bef = data_before
                    # aft = data_after
                    is_skip_correct = True
                elif (trans_type == '12' and data_after in data_before) \
                        or (trans_type == '13' and data_before in data_after):  # 包含关系：12-跳转前包含跳转后的；13-跳转后包含跳转前的
                    # bef = data_before
                    # aft = data_after
                    is_skip_correct = True
                elif trans_type in ('10', '11'):  # 月时间转换为月初/月末日期
                    day_begin, day_end = Utils.get_day_range_of_month(data_before)
                    # bef = data_before
                    data_before = day_begin if trans_type == '10' else day_end
                    bef += '→' + data_before
                    # aft = data_after
                    if data_before == data_after:
                        is_skip_correct = True
                elif trans_type in ('15', '16'):  # 15 - 终端地址转资产号；16 - 终端资产号转地址
                    # bef = data_before
                    data_before = self.data_trans(trans_type, data_before)
                    bef += '→' + data_before
                    # aft = data_after
                    if data_before == data_after:
                        is_skip_correct = True
                elif trans_type == '14' and ((data_before == '0' and data_after == '没有数据') \
                                             or (data_before != '0' and data_after != '没有数据')):  # 基本应用→数据采集管理→采集质量分析→采集成功率:采集成功率统计  经“采集成功率”列跳转到明细页面
                    bef = data_before + '%'
                    # aft = data_after
                    is_skip_correct = True
                elif xpath_type == '04' and data_before == '0' and data_after == '没有数据':  # 取所在跳转的统计数据值
                    data_after = '0'
                    # bef = data_before
                    aft = data_after + '→0'
                    is_skip_correct = True

                # 跳转前:xpath:{map_rela[5]}、值：{}-----跳转后:xpath:{map_rela[8]}、值：{}、转换关系{}、是否通过{}
                compare_result[-1].append([bef_name, bef, aft_name, aft, dict_trans_type[trans_type], \
                                           ('通过' if is_skip_correct else '不通过')])

                info_rlt = info.format(row_num, col_idx, map_rela[11], map_rela[5], data_before, map_rela[8],
                                       data_after)  # ELEMENT_SN / XPATH / TARGET_XPATH
                if is_skip_correct:
                    logger.info(info_rlt)
                else:
                    is_pass = False
                    err_info = '跳转传值错误:' + info_rlt
                    logger.error(err_info)
            # if not is_pass:
            #     self.output_compare_list(compare_result)

        except Exception as ex:
            # print('\r跳转数据比对：跳转前--', skip_data_before, '--\r跳转后--', skip_data_after, '--\r跳转关系', map_rela_rslt)
            print('</br>跳转数据比对--跳转前：')
            for i, before in enumerate(skip_data_before):
                print(('</br>' if i % 2 == 0 else '') + str(before))
            print('</br>跳转后：')
            for i, after in enumerate(skip_data_after):
                print(('</br>' if i % 2 == 0 else '') + str(after))
            print('</br>跳转关系：')
            for i, rslt in enumerate(map_rela_rslt):
                print(('</br>' if i % 2 == 0 else '') + str(rslt))
            raise ex
        return is_pass, compare_result, True

    def data_trans(self, trans_type, data_before):
        """
        资产编号与地址之间互转
        :param trans_type: 转换类型：15 - 终端地址转资产号；16 - 终端资产号转地址
        :param data_before:
        :param asset_type: 01-终端；02-电表
        :return:
        """
        #
        return DataAccess.get_data_trans(trans_type, data_before)

    def special_deal(self, is_special, col_name):
        """
        针对一个单元格有多个链接或Tab页中有tab页的特殊处理
        :param is_special: 对column_name做分割处理
        :param col_name:
        :return: [column_name, link_tag]
        """
        if is_special == 'Y':
            col_and_link_tag = col_name.split('-')
        else:
            # col_and_link_tag = []
            # col_and_link_tag.append(col_name)
            # col_and_link_tag.append('')
            col_and_link_tag = [col_name]

        return col_and_link_tag

    def query_records(self, loc_col_name):
        # 查询结果行数
        locator = self.tst_inst.format_xpath_multi(AssertResultLocators.QUERY_RESULT, loc_col_name, True)
        els = self.tst_inst._find_elements(locator)
        is_find = False
        first_row_idx = -1
        row_cnt = 0
        if bool(els):
            for i, el in enumerate(els):
                if el.is_displayed():
                    row_cnt += 1
                    if first_row_idx == -1:
                        first_row_idx = i
                        is_find = True

        return is_find, first_row_idx, row_cnt

    def skip_menu_tab_page(self, assert_type, case_data, case_result, col_pos_info, col_and_link_tag):
        """
        :param assert_type:
        :param case_data:
        :param case_result: 查询结果校验列表内容：定位列名；校验列名；期望值；定位行号;是否特殊处理
        :param col_pos_info:
        :param col_and_link_tag:用于处理一个单元格，多链接情况
        :return:
        """

        # 查询结果行数
        is_find, first_row_idx, row_cnt = self.query_records(case_result[0])
        if is_find:
            col_pos_info['HIDE_ROWS'] = first_row_idx

            # 获取跳转映射对应关系
            map_rela_rslt = DataAccess.get_skip_data(case_data['TST_CASE_ID'], case_result[1])
            # /*带*字段来自tst_case_result， 其余来自tst_col_link_rela
            # xpath_type:页面元素类型：01-查询条件（XPATH);02-表格列对应值;03-表格列名;04-读取统计数与明细对比
            # 0源:列定位字段     1Tab页名称  2源:跳转字段名    3取值行号   4页面元素类型  5页面元素  6目标页面Tab页名称     7转换类型    8目标页面元素   9转换后的值   10是否转换   11源xpath序号
            # TAB_COLUMN_NAME*  TAB_NAME   COLUMN_NAME*    ROW_NUM*  XPATH_TYPE     XPATH    TARGET_TAB_NAME     TRANS_TYPE  TARGET_XPATH  TRANS_VALUE  IS_TRANS    ELEMENT_SN
            #                              同col_name
            # 用户编号          终端调试    备注-报文查询    1         02             用户编号    01                  01          CONS_NO                        0           1
            # 用户编号          终端调试    备注-报文查询    1         02             用户名称    01                  01          CONS_NAME                      0           2
            # 用户编号          终端调试    备注-报文查询    1         02             终端地址    01                  01          TMNL_ADDR                      0           3

            skip_data_before = self.get_data_of_skip_before(case_data, case_result, map_rela_rslt)

            # 定位列名；          校验列名；    期望值(校验值)；   定位行号;  是否特殊处理 跳转超时等待      表头行号   跳转是否为Tab页：1-是
            # TAB_COLUMN_NAME	COLUMN_NAME	EXPECTED_VALUE	ROW_NUM	 IS_SPECIAL	WAIT_FOR_TARGET	HEAD_ROW IS_TAB
            link_tag = col_and_link_tag[1] if assert_type == '26' else None
            skip_info = self.skip_to(case_result, col_pos_info, link_tag)

            # 校验页面的名称是否正确
            is_skiped = skip_info['CLICKABLE'] and self.assert_page_name(case_result[2])
            if is_skiped:
                # is_menu = assert_type != '23'  # 23-跳转目标为tab页，其他为菜单
                is_menu = case_result[7] == '0'  # is_tab：0-菜单；1-Tab页
                # 获取跳转目标页面相关元素值
                skip_data_after = self.get_data_of_skip_after(case_result, map_rela_rslt, is_menu, skip_data_before)

                if is_menu:  # 关闭菜单页
                    self.tst_inst.menuPage.closePage(case_result[2])
                else:  # 返回前一个tab页
                    self.tst_inst.clickTabPage(case_data['PAGE_TAB_NAME'])

                # 滚动到表格起始列
                row_num = case_result[3]
                first_col_idx = self.tst_inst.format_xpath_multi(AssertResultLocators.QUERY_RESULT_ROW_COL,
                                                                 (case_result[0], row_num, col_pos_info['FIRST_COL_IDX']), True)
                self.tst_inst.scrollTo(first_col_idx)

                # 校验跳转传值是否正确
                if assert_type == '25':  # 跳转到新的菜单页, 但该菜单页在tst_menu中不存在
                    is_pass = True
                else:
                    is_pass = self.skip_data_check(col_pos_info, map_rela_rslt, row_num, skip_data_before, skip_data_after)
                return is_pass
            else:
                logger.error('跳转“{}”到页面失败'.format(case_result[2]))
                return False
        else:
            raise AssertError('没查询结果， 跳转验证失败！！')

    def check_of_skip_menu_or_tab(self, assert_type, case_data, case_result, col_pos_info, col_and_link_tag):  # , is_menu=True, link_xpath=None):
        """
        菜单或Tab页跳转校验
        :param assert_type: 跳转类别，其中201-TST_MENU中不存在的菜单页，不做跳转前后值比较
        :param case_data:
        :param case_result: 查询结果校验列表内容：定位列名；校验列名；期望值；定位行号;是否特殊处理
        :param col_pos_info:
        :param col_and_link_tag:用于处理一个单元格，多链接情况
        :return:
        """

        # 查询结果行数
        is_find, first_row_idx, row_cnt = self.query_records(case_result[0])
        if is_find:
            col_pos_info['HIDE_ROWS'] = first_row_idx

            # 获取跳转映射对应关系
            map_rela_rslt = DataAccess.get_skip_data(case_data['TST_CASE_ID'], case_result[1])
            # /*带*字段来自tst_case_result， 其余来自tst_col_link_rela
            # xpath_type:页面元素类型：01-查询条件（XPATH);02-表格列对应值;03-表格列名;04-读取统计数与明细对比
            # 0源:列定位字段     1Tab页名称  2源:跳转字段名    3取值行号   4页面元素类型  5页面元素  6目标页面Tab页名称     7转换类型    8目标页面元素   9转换后的值   10是否转换   11源xpath序号
            # TAB_COLUMN_NAME*  TAB_NAME   COLUMN_NAME*    ROW_NUM*  XPATH_TYPE     XPATH    TARGET_TAB_NAME     TRANS_TYPE  TARGET_XPATH  TRANS_VALUE  IS_TRANS    ELEMENT_SN
            #                              同col_name
            # 用户编号          终端调试    备注-报文查询    1         02             用户编号    01                  01          CONS_NO                        0           1
            # 用户编号          终端调试    备注-报文查询    1         02             用户名称    01                  01          CONS_NAME                      0           2
            # 用户编号          终端调试    备注-报文查询    1         02             终端地址    01                  01          TMNL_ADDR                      0           3

            data_of_skip_before = self.get_data_of_skip_before(case_data, case_result, map_rela_rslt)

            # 定位列名；          校验列名；    期望值(校验值)；   定位行号;  是否特殊处理 跳转超时等待      表头行号   跳转是否为Tab页：1-是
            # TAB_COLUMN_NAME	COLUMN_NAME	EXPECTED_VALUE	ROW_NUM	 IS_SPECIAL	WAIT_FOR_TARGET	HEAD_ROW IS_TAB
            link_tag = col_and_link_tag[1] if assert_type[1] == '1' else None  # 一列多链接【26】
            skip_info = self.skip_to(case_result, col_pos_info, link_tag)

            # 校验页面的名称是否正确 @TODO Tab页跳转校验有待优化
            is_skiped = skip_info['CLICKABLE'] and self.assert_page_name(case_result[2])
            if is_skiped:  # 跳转成功
                is_menu = assert_type[0] == '2'  # 2-菜单；3-弹窗
                # 获取跳转目标页面相关元素值
                data_of_skip_after = self.get_data_of_skip_after(case_result, map_rela_rslt, is_menu, data_of_skip_before)

                if is_menu:  # 关闭跳转的菜单页
                    self.tst_inst.menuPage.closePage(case_result[2])
                else:  # 返回跳转前的源tab页
                    self.tst_inst.clickTabPage(case_data['PAGE_TAB_NAME'])

                # 滚动到表格起始列
                row_num = case_result[3]
                loc_first_visiable_col = self.tst_inst.format_xpath_multi(AssertResultLocators.QUERY_RESULT_ROW_COL,
                                                                          (case_result[0], row_num, col_pos_info['FIRST_COL_IDX']), True)
                self.tst_inst.scrollTo(loc_first_visiable_col)

                # 校验跳转传值是否正确
                if assert_type == '201':  # 201-TST_MENU中不存在的菜单页； # 跳转到新的菜单页, 但该菜单页在tst_menu中不存在
                    col_name = col_pos_info['COL_NAME']
                    link_tag = col_and_link_tag[1] if assert_type[1] == '1' else None  # 一列多链接【26】
                    link = ('链接：', link_tag) if bool(link_tag) else ('', '')
                    compare_result = [row_num, col_name, *link, self.assert_info, []]
                    compare_result[-1].append([case_result[2], case_result[2], '通过'])
                    is_pass = (True, compare_result, False)
                else:
                    is_pass = self.skip_data_compare(col_pos_info, link_tag, map_rela_rslt, row_num, data_of_skip_before, data_of_skip_after)
                return is_pass
            else:
                logger.error('跳转到“{}”页面/TAB页失败！'.format(case_result[2]))

                col_name = col_pos_info['COL_NAME']
                link_tag = col_and_link_tag[1] if assert_type[1] == '1' else None  # 一列多链接【26】
                link = ('链接：', link_tag) if bool(link_tag) else ('', '')
                compare_result = [case_result[3], col_name, *link, self.assert_info, []]
                compare_result[-1].append([case_result[2], '页面/TAB页跳转失败', '不通过'])
                return (False, compare_result, False)
        else:
            raise AssertError('没查询结果， 无法验证跳转！')

    def check_of_org_drill_down(self, assert_type, case_result, col_pos_info):
        """
        供电单位下钻校验
        :param assert_type:
        :param case_result:
        :param col_pos_info:
        :return:
        """
        # 查询结果行数
        is_find, first_row_idx, row_cnt = self.query_records(case_result[0])
        if is_find:
            col_pos_info['HIDE_ROWS'] = first_row_idx

            # 下钻前的供电单位名称
            original_org_name = self.tst_inst.get_input_val(case_result[2], tag_blank_type='01')
            # compare_result = ['--', original_org_name, '', '', self.assert_info, []]
            try:
                is_skiped = True
                while True:
                    # 定位列名；校验列名；期望值(校验值)；定位行号;是否特殊处理
                    skip_info = self.skip_to(case_result, col_pos_info, is_deal_after=True)
                    link_text = skip_info['LINK_TEXT']
                    org_name = self.tst_inst.get_input_val(case_result[2])
                    if skip_info['CLICKABLE'] and skip_info['IS_SKIPED']:
                        if org_name == original_org_name or link_text != org_name:  # 校验下钻传值是否正确
                            raise AssertError('“{}”下钻失败， “{}”不是期望的供电单位！'.format(link_text, org_name))
                            # compare_result[-1].append([link_text, org_name, '不通过'])
                            # break
                        # 跳转后的相关判断处理
                        after_text = skip_info['AFTER_TEXT']
                        # 获取供电单位类别
                        org_type = DataAccess.get_org_type(after_text)

                        # AFTER_ACTION：01-没查询结果；02-查询结果有链接；03-有查询结果，但没链接；
                        after_action = skip_info['AFTER_ACTION']
                        if org_type > '04' or after_action == '03':  # 跳转后没值或到县级以下供电单位（如：供电所）时，停止跳转
                            # is_skiped = True
                            break
                        elif after_action == '01':  # 校验列没有链接；
                            raise AssertError('“{}”下钻后没查询结果，没法下钻！'.format(link_text))
                            # compare_result[-1].append([link_text, '没查询结果，没法下钻', '不通过'])
                            # break
                        elif after_action == '02' and link_text == skip_info['EL_AFTER_A'].text:
                            raise AssertError('“{}”下钻不了！'.format(link_text))
                            # compare_result[-1].append([link_text, '下钻不了', '不通过'])
                            # break
                    else:
                        # DataAccess.el_operate_log(self.tst_inst.menu_no, self.tst_inst.tst_case_id, None, self.tst_inst.class_name, '跳转失败' + assert_type,
                        #                           '“{}”没查询结果，无法继续下钻！'.format(org_name))
                        # is_skiped = False
                        # compare_result[-1].append([org_name, '没查询结果或其他原因，没法下钻', '不通过'])
                        # break
                        raise AssertError('“{}”没查询结果或其他原因，没法下钻！'.format(org_name))
            except AssertError as ae:
                raise ae
            except Exception as ec:
                raise ec
            finally:
                org_node = DataAccess.get_org_node_by_name(original_org_name)
                self.tst_inst.openLeftTree(org_node)
                self.tst_inst.btn_qry()

            return is_skiped
        else:
            raise AssertError('没查询结果， 下钻跳转验证失败！！')


class AssertResultLocators:
    # 弹窗的关闭xpath
    WINDOWS_CLOSE = (By.XPATH, '//*[text()="{}"]/../div[1]')

    # 弹窗标题
    DLG_TITLE = (By.XPATH, '//div[@class=" x-window x-resizable-pinned"]//span[@class="x-window-header-text" and text()="{}"]')

    # 菜单页的名称
    MENU_NAME = (By.XPATH, '//span[@class="x-tab-strip-inner"]/span[contains(text(),"{}")]')

    # 【显示区】
    # 判断是否有查询结果
    QUERY_RESULT = (By.XPATH,
                    '(//div[text() ="{}"]/ancestor::div[contains(@class,"x-grid-with-col-lines") and not(contains(@class, "x-hide-display"))]//div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)')

    # 定位查询结果的某行某列
    QUERY_RESULT_ROW_COL = (By.XPATH,
                            '(//div[text() ="{}"]/ancestor::div[contains(@class,"x-grid-with-col-lines") and not(contains(@class, "x-hide-display"))]//div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)[{}]//td[{}]')

    QUERY_RESULT_ROW_COL_LINKS = (By.XPATH,
                                  '(//div[text() ="{}"]/ancestor::div[contains(@class,"x-grid-with-col-lines") and not(contains(@class, "x-hide-display"))]//div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)[{}]//td[{}]//*[contains(text(),"{}")]')

    # 查询结果非显示区，是输入框(第一个值代表是哪个区域的，第二个值是代表那个输入框)
    QUERY_RESULT_BY_INPUT = (By.XPATH, '//span[text()="{}"]/../..//label[text()="{}"]/../..//input')

    # input输入框
    INPUT_BASE_GU = (By.XPATH, '//label[text()= "{}"]/../div[@class=\"x-form-element\"]//input')

    # link 数据是否对应(显示区右下角查询的数据总量)
    QUERY_RESULT_TOTAL_ROW = (By.XPATH, '//div[@id="{}"]//tr[@class="x-toolbar-right-row"]//div[@class="xtb-text"]')


if __name__ == '__main__':
    # skipMenuName = AssertResultLocators.MENU_NAME[1].format(
    #     'cdscsdc')
    # print(skipMenuName)
    a = AssertResult(None)
    link = ('链接：', '报文查询') if True else ('', '')
    compare_result = [2, '用户编号', *link, '200-普通菜单', [[1, 2, 3, 4, 5, 6], ['a', 'b', 'c', 'd', 'e', 'f']]]
    a.output_compare_list(compare_result)
