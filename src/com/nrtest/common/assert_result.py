# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: assert_result.py
@time: 2019/1/15 0015 9:32
@desc:江西期间整改调试，并优化
"""
from time import sleep

from selenium.webdriver.common.by import By

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.logger import Logger
from com.nrtest.common.user_except import AssertError
from com.nrtest.common.utils import Utils

logger = Logger(logger='AssertResult').getlog()


# 校验新方法
class AssertResult():
    def __init__(self, call_from):
        self.tst_inst = call_from

    def save_img(self, img_path, img_name):
        self.tst_inst.save_img(img_path, img_name)

    def popup(self, img_path, img_name, *args):
        return self.tst_inst.popup(img_path, img_name, *args)

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
        try:
            is_find, first_row_idx, row_cnt = self.query_records(case_result[0])
            if is_find:
                match_cnt = 0
                displayLineElement = (By.XPATH,
                                      '(//*[text()="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)[{}]/td[{}]//*[contains(text(),"{}")]')
                for i in range(1, row_cnt + 1):
                    try:
                        # 显示区结果的每一行对应列的数据的xpath
                        locator = self.tst_inst.format_xpath(displayLineElement,
                                                             (case_result[0], i + first_row_idx, col_pos_info['COL_IDX'], case_result[2]))
                        assert_rslt = self.assert_context(locator)
                        if assert_rslt:
                            match_cnt += 1
                        else:
                            print('第{}行，{}列显示的值与{}不一致\r'.format(i, case_result[1], case_result[2]))
                            break
                    except:
                        print('校验失败')
                return match_cnt == row_cnt
            else:
                raise AssertError('查询没记录，校验失败！')
        except:
            print('显示区结果值校验失败')
            return False

    def assert_page_name(self, page_name):
        """
        判断跳转的页面的菜单名是否正确
        :param page_name:
        :return:
        """
        xpath = self.tst_inst.format_xpath(AssertResultLocators.MENU_NAME, page_name)
        return self.assert_context(xpath)

    @BeautifulReport.add_popup_img(6)
    def skip_to_page(self, case_result, col_pos_info, link_xpath=None):
        """
        链接跳转:跳转到另一个页面
        :param case_result: 查询结果校验列表内容：定位列名；校验列名；期望值；定位行号;是否特殊处理
        :param col_pos_info:  数据内容{'COL_IDX':0, 'EL_COL':None, 'EL_FIRST':None, 'COL_IS_HIDED':True}
        :return:
        """
        #  IS_SKIPED：能点击，但不一定会跳转（没link时）；CLICKABLE：可点击，且不会报错
        skip_info = {'IS_SKIPED': True, 'LINK_TEXT': None, 'EL_A': None, 'CLICKABLE': False, 'EL_AFTER_A': None, 'AFTER_TEXT': ''}
        try:
            # 按下面代码执行会报这个错：'FirefoxWebElement' object does not support indexing
            # el_link = el_data_rows[int(case_result[3])].find_elements_by_xpath('./td[{}]//a'.format(col_pos_info['COL_IDX']))
            if link_xpath is None:
                link_xpath = self.tst_inst.format_xpath_multi(AssertResultLocators.QUERY_RESULT_ROW_COL,
                                                              (case_result[0], int(case_result[3]) + col_pos_info['HIDE_ROWS'],
                                                               col_pos_info['COL_IDX']), True)
            el_link = self.tst_inst._find_displayed_element(link_xpath)
            skip_info['EL_A'] = el_link.find_elements_by_xpath('.//a')
            skip_info['LINK_TEXT'] = el_link.text
            skip_info['CLICKABLE'] = bool(skip_info['EL_A'])
            self.tst_inst.scrollTo(el_link)
            el_link.click()

            el_after_click = self.tst_inst._find_displayed_element(link_xpath)
            if bool(el_after_click):
                skip_info['EL_AFTER_A'] = el_after_click.find_elements_by_xpath('.//a')
                skip_info['AFTER_TEXT'] = el_after_click.text if bool(el_after_click) else ''

            # 休眠N秒，等待跳转页面加载:WAIT_FOR_TARGET
            seconds = case_result[5]
            if seconds > 0:  # 按loading元素等待，超时不抛异常
                try:
                    self.tst_inst.query_timeout(timeout_seconds=seconds)
                except:
                    pass
            else:
                sleep(abs(seconds))
        except Exception as ex:
            print('跳转验证失败:' + ex.__str__())
            skip_info['IS_SKIPED'] = False

        return skip_info

    def calc_col_idx(self, loc_col_name, col_name, idx=1):
        """
        计算所给列名（col_name）在表格中的所处位置【该函数已移至base_page】
        --------------------loc_col_name[0]-----------------|-col_name[1]-|----[2]-------|--要定位的行号[3]--|-----[4]-----
        nvl(tab_column_name, column_name) AS tab_column_name, column_name, expected_value, row_num,          is_special
        :param loc_col_name: 能唯一定位表头的关键列名
        :param col_name: 计算列位置的列名
        :param idx: 第idx个可见对象
        :return: 返回：列位置，列是否可见以及第一列带标签的列
        """
        return self.tst_inst.calc_col_idx(loc_col_name, col_name, idx)

    def check_query_result(self, para):
        """
        查询结果校验处理
        :param para: 用例数据
        :return: 返回校验结果
        """
        esplain = {
            '11': '显示区未查询出结果',
            '12': '按条件查询出的结果与期望值不一致',
            '21': '跳转菜单页面不正确',
            '22': '跳转弹窗不正确',
            '23': '跳转tab页不正确',
            '24': '跳转弹窗的名称带的值不正确',
            '25': '跳转到新的菜单页，但不携带值错误',  # 这里的菜单是指没有menu_no的菜单 ？？？？  tst_case_id = 9993110012
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
            is_calc_col_idx = assert_type not in ['11', '31']
            if is_calc_col_idx:
                col_and_link_tag = self.special_deal(case_result[4], case_result[1])
                col_pos_info = self.calc_col_idx(case_result[0], col_and_link_tag[0])
            logger.info('*******' + case_id + '*********校验类别：{}；定位列名：{}；校验列名：{}；期望值：{}；定位行号：{};是否特殊处理：{}\r'.format(*row))
            if assert_type == '11':  # 【OK】
                locator = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT, case_result[0])
                assert_rslt = self.assert_context(locator)
            elif assert_type == '12':  # 判断值是否准确,item截取字符串，在转换成列表
                assert_rslt = self.assertValue(case_result, col_pos_info)
            elif assert_type == '21':  # 跳转菜单
                # assert_rslt = self.clickSkip(case_result, para)
                assert_rslt = self.skip_menu_tab_page(assert_type, para, case_result, col_pos_info)
            elif assert_type == '22':  # 跳转弹窗
                assert_rslt = self.skip_windows_page(case_result, col_pos_info)
            elif assert_type == '23':  # 跳转tab页
                # assert_rslt = self.skip_tab_page(case_result, para)
                assert_rslt = self.skip_menu_tab_page(assert_type, para, case_result, col_pos_info, is_menu=False)
            elif assert_type == '24':
                # assert_rslt = self.tab_skip_into_window(case_result, col_pos_info)
                assert_rslt = self.skip_windows_page(case_result, col_pos_info, True)
            elif assert_type == '25':  # 【OK】 # 跳转到新的菜单页，但不携带值
                assert_rslt = self.skip_new_menu(case_result, col_pos_info)
            elif assert_type == '26':  # 【OK】 # 单列数据有两个跳转
                # assert_rslt = self.skip_two_link(case_result, para)
                link_xpath = self.tst_inst.format_xpath_multi(AssertResultLocators.QUERY_RESULT_ROW_COL_LINKS,
                                                              (case_result[0], case_result[3], col_pos_info['COL_IDX'], col_and_link_tag[1]), True)
                assert_rslt = self.skip_menu_tab_page(assert_type, para, case_result, col_pos_info, True, link_xpath=link_xpath)
            elif assert_type == '27':  # 【OK】
                # assert_rslt = self.skip_more_tab_link(case_result, para)
                assert_rslt = self.skip_menu_tab_page(assert_type, para, case_result, col_pos_info)
            elif assert_type == '28':  # 供电单位层层下钻
                assert_rslt = self.skip_into_child_org(assert_type, case_result, col_pos_info)
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

    def assertInput(self, case_id, case_result):
        """
        获取单个
        :param case_result:
        :param case_id:
        :return:
        """
        xpath = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT_BY_INPUT, (case_result[0], case_result[1]))
        # val = self.get_text(xpath)
        el = self.tst_inst._find_displayed_element(xpath)
        val = el.get_attribute('value')
        if case_result[2] == val:
            logger.info('查询详细信息的输入框的值与期望结果一样')
            return True
        else:
            logger.error('查询详细信息的输入框的值与期望结果不一致')
            return False

    def skip_windows_page(self, case_result, col_pos_info, is_dynamic=False):
        """
        窗口跳转
        :param case_result: 以，为分隔符，定位列名；校验列名；期望值(校验值)；定位行号;是否特殊处理；等待目标跳转对象时间
        :param col_pos_info:
        :param is_dynamic:
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
            if is_dynamic:
                # 获取弹窗的动态窗口标题名
                col_idx = self.calc_col_idx(case_result[0], case_result[2])['COL_IDX']
                xpath = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT_ROW_COL, (case_result[0], case_result[3], col_idx))
                dlg_title = self.tst_inst.driver.find_element(*xpath).text
            else:  # 固定窗口标题名
                dlg_title = case_result[2]

            # 跳转到目标页
            skip_info = self.skip_to_page(case_result, col_pos_info)
            if skip_info['CLICKABLE']:
                sleep(2)
                # 关闭窗口 已在base_page模块下的popup方法中统一处理弹窗关闭处理
                # close_xpath = self.tst_inst.format_xpath(AssertResultLocators.WINDOWS_CLOSE, case_result[2])
                # el = self.tst_inst._direct_find_element(close_xpath)
                # el.click()
                # 弹窗信息
                self.dlg_info = self.tst_inst.get_skip_except_info('01')
                is_skiped = dlg_title in self.dlg_info if bool(self.dlg_info) else False
            else:
                is_skiped = False
            self.tst_inst.scrollTo(col_pos_info['EL_FIRST'])
        else:
            raise AssertError('没查询结果， 跳转验证失败！！')
        return is_skiped


    def skip_new_menu(self, case_result, col_pos_info):
        """
        跳转到新的菜单，但不需要校验值
        :param case_result:
        :return:
        """
        is_find, first_row_idx, row_cnt = self.query_records(case_result[0])
        if is_find:
            col_pos_info['HIDE_ROWS'] = first_row_idx
            self.skip_to_page(case_result, col_pos_info)
            # xpath = self.tst_inst.format_xpath(AssertResultLocators.MENU_NAME, case_result[2])
            # res = self.assert_context(xpath)
            res = self.assert_page_name(case_result[2])
            self.tst_inst.menuPage.closePage(page_name=case_result[2])
        else:
            raise AssertError('没查询结果， 跳转验证失败！！')

        return res

    def get_skip_data_before(self, case_data, case_result, map_rela_rslt):
        """
        -------0--------|----1----|----2-------|----3---|----4-----|--5---|--------6-------|----7-----|------8-----|-----9-----|---10---|----11-----|-----12-----
        *TAB_COLUMN_NAME TAB_NAME  *COLUMN_NAME *ROW_NUM XPATH_TYPE XPATH   TARGET_TAB_NAME TRANS_TYPE TARGET_XPATH TRANS_VALUE IS_TRANS ELEMENT_SN  TARGET_MENU_NO
           是否在线   终端版本召测	查看报文	  1	       02	   终端地址	     01	            00	   TMNL_ADDR		           0	    3         99934410

        :param case_data:
        :param case_result:
        :param map_rela_rslt:
        :return:
        """
        skip_data_before = []
        for map_rela in map_rela_rslt:
            # 获取查询条件输入框的值
            xpath_type = map_rela[4]
            if xpath_type == '01':  # 页面元素类型：XPATH_TYPE 【01-查询条件（XPATH)】;02-表格列对应值;03-表格列名;04-读取统计数与明细对比
                # 把查询条件的xpath转换为对应查询条件中文名
                # menu_xpath_data = DataAccess.get_xpath_tab_data(map_rela[5], case_data['TST_CASE_ID'], case_data['TAB_NAME'])  # XPATH
                menu_xpath_data = DataAccess.get_menu_xpath_data(case_data['MENU_NO'], case_data['TAB_NAME'], map_rela[5])
                if menu_xpath_data[1] in ('04', '05', '07'):
                    val = self.tst_inst.get_para_value(case_data[map_rela[5]])
                else:
                    val = self.tst_inst.get_input_val(menu_xpath_data[0], menu_xpath_data[1], menu_xpath_data[2])
                skip_data_before.append(val)
                # locator_qry = self.get_xpath(menu_xpath_list[0])
                # skip_data_before.append(self.get_text(locator_qry))
            elif xpath_type in ['02', '04']:
                loc_col_name = case_result[0]
                col_idx = self.calc_col_idx(loc_col_name, map_rela[5])['COL_IDX']  # XPATH
                # locator = self.get_xpath(loc_col_name, case_result[3], col_idx, type=2)
                locator = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT_ROW_COL, (loc_col_name, case_result[3], col_idx))
                val = self.tst_inst.driver.find_element(*locator).text
                skip_data_before.append(val)
            elif xpath_type == '03':
                skip_data_before.append(case_result[1])
        return skip_data_before

    def get_skip_data_after(self, case_result, map_rela_rslt, is_menu, skip_data_before):
        """
        -------0--------|----1----|----2-------|----3---|----4-----|--5---|--------6-------|----7-----|------8-----|-----9-----|---10---|----11-----|-----12--------|------13-------|
        *TAB_COLUMN_NAME TAB_NAME  *COLUMN_NAME *ROW_NUM XPATH_TYPE XPATH   TARGET_TAB_NAME TRANS_TYPE TARGET_XPATH TRANS_VALUE IS_TRANS ELEMENT_SN  TARGET_MENU_NO  TARGET_MENU_NAME
           是否在线   终端版本召测	查看报文	  1	       02	   终端地址	     01	            00	   TMNL_ADDR		           0	    3         99934410
        :param case_result:
        :param map_rela_rslt:
        :param menu_name: True-跳转目标为菜单；False-跳转目标为Tab页
        :return:
        """
        # 休眠2秒，等待跳转页面加载:WAIT_FOR_TARGET
        # seconds = case_result[5]
        # if seconds > 0:  # 按loading元素等待，超时不抛异常
        #     try:
        #         self.tst_inst.query_timeout(timeout_seconds=seconds)
        #     except:
        #         pass
        # else:
        #     sleep(abs(seconds))

        # print('STEP-0')
        skip_data_after = []
        for i, map_rela in enumerate(map_rela_rslt):
            # print('STEP-1', map_rela)
            xpath_type = map_rela[4]  # XPATH_TYPE
            if xpath_type == '04' and map_rela[8] is None:  # 读取跳转页的查询结果总数  TARGET_XPATH
                try:
                    # print('STEP-2')
                    # ********************************************@TODO 弹窗窗口的记录总数需验证测试******
                    loc = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT_TOTAL_ROW,
                                                     (case_result[2] if is_menu else self.tst_inst.menu_name))
                    total_text = Utils.replace_chrs(self.tst_inst._find_displayed_element(loc).text, ' \r\n\t')
                    val = total_text.split('/')[-1]
                    skip_data_after.append(val)
                    # print('STEP-3')
                except:
                    skip_data_after.append('0')
                    # print('STEP-4')
            else:
                try:
                    # print('SETUP-5 MENU_NO:{}'.format(map_rela[12]))
                    # print('SETUP-5 TAB_NAME:{}'.format(map_rela[6]))
                    # print('SETUP-5 XPATH:{}'.format(map_rela[8]))
                    menu_xpath_data = DataAccess.get_menu_xpath_data(map_rela[12], map_rela[6],
                                                                     map_rela[8])  # TARGET_MENU_NO / TARGET_TAB_NAME/  TARGET_XPATH
                    # print('SETUP-6 xpath_name:{}'.format(menu_xpath_list[0]))
                    # print('SETUP-6 use_share_xpath:{}'.format(menu_xpath_list[1]))
                    # print('SETUP-6 option_name:{}'.format(menu_xpath_list[2]))
                    # print('SETUP-6  menu_name{}'.format(map_rela[13]))
                    if menu_xpath_data[1] in ('04', '05', '07'):  # 单选框/复选框处理
                        val = self.tst_inst.get_input_val(skip_data_before[i], menu_xpath_data[1], menu_xpath_data[2], map_rela[13])
                    else:
                        val = self.tst_inst.get_input_val(menu_xpath_data[0], menu_xpath_data[1], menu_xpath_data[2], map_rela[13])
                    # print('STEP_7')
                    skip_data_after.append(val)
                    # print('STEP_8')
                    # v_xpath = self.get_xpath(menu_xpath_list[0])
                    # self.tst_inst.sleep_time(1)
                    # text = self.get_text(v_xpath)
                    # skip_data_after.append(text)
                except:
                    # print('STEP-9')
                    logger.error('跳转的新页面/窗口需配置等待加载时间或TST_COL_LINK_RELA.TARGET_XPATH={}配置错误！'.format(map_rela[8]))
                    # print('STEP-10')
                    return None
        # print('skip_data_after:', skip_data_after)
        return skip_data_after

    def check_skip_data(self, col_pos_info, map_rela_rslt, row_idx, skip_data_before, skip_data_after):

        col_idx = col_pos_info['COL_IDX'] - col_pos_info['HIDE_COLS']
        info = '跳转坐标（{}行,{}列）element_sn:{}跳转前:xpath:{}、值：{}-----跳转后:xpath:{}、值：{}'
        try:
            all_val = '全部'
            is_pass = True
            for data_before, data_after, map_rela in zip(skip_data_before, skip_data_after, map_rela_rslt):
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
            print('\r跳转数据比对：跳转前--', skip_data_before, '--\r跳转后--', skip_data_after, '--\r跳转关系', map_rela_rslt)
            raise ex
        return is_pass

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
            col_and_link_tag = []
            col_and_link_tag.append(col_name)
            col_and_link_tag.append('')
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

    def skip_menu_tab_page(self, assert_type, case_data, case_result, col_pos_info, is_menu=True, link_xpath=None):
        """
        :param case_result: 查询结果校验列表内容：定位列名；校验列名；期望值；定位行号;是否特殊处理
        :param case_data:
        :return:
        """
        # 查询结果行数
        is_find, first_row_idx, row_cnt = self.query_records(case_result[0])
        if is_find:
            col_pos_info['HIDE_ROWS'] = first_row_idx
            # 获取跳转映射对应关系
            map_rela_rslt = DataAccess.get_skip_data(case_data['TST_CASE_ID'], case_result[1])
            """
            /*带*字段来自tst_case_result， 其余来自tst_col_link_rela
            xpath_type:页面元素类型：01-查询条件（XPATH);02-表格列对应值;03-表格列名;04-读取统计数与明细对比
            0源:列定位字段     1Tab页名称  2源:跳转字段名  3取值行号 4页面元素类型  5页面元素  6目标页面Tab页名称     7转换类型   8目标页面元素      9转换后的值  10是否转换  11源xpath序号
            TAB_COLUMN_NAME*  TAB_NAME   COLUMN_NAME*    ROW_NUM*  XPATH_TYPE     XPATH      TARGET_TAB_NAME     TRANS_TYPE  TARGET_XPATH      TRANS_VALUE  IS_TRANS    ELEMENT_SN
                                         同col_name
            用户编号          终端调试    备注-报文查询    1         02             用户编号    01                  01          CONS_NO                        0           1
            用户编号          终端调试    备注-报文查询    1         02             用户名称    01                  01          CONS_NAME                      0           2
            用户编号          终端调试    备注-报文查询    1         02             终端地址    01                  01          TMNL_ADDR                      0           3
            """
            skip_data_before = self.get_skip_data_before(case_data, case_result, map_rela_rslt)
            # 定位列名；校验列名；期望值(校验值)；定位行号;是否特殊处理
            skip_info = self.skip_to_page(case_result, col_pos_info, link_xpath)

            # 校验页面的名称是否正确
            is_skiped = skip_info['CLICKABLE'] and self.assert_page_name(case_result[2])
            if is_skiped:
                # 获取跳转目标页面相关元素值
                skip_data_after = self.get_skip_data_after(case_result, map_rela_rslt, is_menu, skip_data_before)

                if is_menu:  # 关闭菜单页
                    self.tst_inst.menuPage.closePage(case_result[2])
                else:  # 返回前一个tab页
                    self.tst_inst.clickTabPage(case_data['TAB_NAME'])

                first_col_idx = self.tst_inst.format_xpath_multi(AssertResultLocators.QUERY_RESULT_ROW_COL,
                                                                 (case_result[0], case_result[3], col_pos_info['FIRST_COL_IDX']), True)
                self.tst_inst.scrollTo(first_col_idx)

                # 校验跳转传值是否正确
                return self.check_skip_data(col_pos_info, map_rela_rslt, case_result[3], skip_data_before, skip_data_after)
            else:
                logger.error('跳转“{}”到页面失败'.format(case_result[2]))
                return False
        else:
            raise AssertError('没查询结果， 跳转验证失败！！')

    def skip_into_child_org(self, assert_type, case_result, col_pos_info):
        # 查询结果行数
        is_find, first_row_idx, row_cnt = self.query_records(case_result[0])
        if is_find:
            col_pos_info['HIDE_ROWS'] = first_row_idx

            # 下钻前的供电单位名称
            original_org_name = self.tst_inst.get_input_val(case_result[2])
            is_skiped = True
            while True:
                # 定位列名；校验列名；期望值(校验值)；定位行号;是否特殊处理
                skip_info = self.skip_to_page(case_result, col_pos_info)
                link_text = skip_info['LINK_TEXT']
                org_name = self.tst_inst.get_input_val(case_result[2])
                if skip_info['CLICKABLE']:
                    if skip_info['IS_SKIPED']:
                        if org_name == original_org_name or link_text != org_name:  # 校验下钻传值是否正确
                            raise AssertError('当前供电单位“{}”下钻失败， “{}”不是期望的供电单位！'.format(link_text, org_name))

                        # 跳转后的相关判断处理
                        after_text = skip_info['AFTER_TEXT']
                        if after_text.endswith('所'):  # 跳转后没值或到供电所时，停止跳转
                            break
                        elif not bool(skip_info['EL_AFTER_A']):  # 校验列没有链接；
                            raise AssertError('“{}”没查询结果，无法继续下钻，请检查是否合理！'.format(link_text))
                    else:
                        is_skiped = False
                        break
                else:
                    DataAccess.el_operate_log(self.tst_inst.menu_no, self.tst_inst.tst_case_id, None, self.tst_inst.class_name, '跳转失败' + assert_type,
                                              '“{}”没查询结果，故对下属单位下钻失败！'.format(org_name))
                    is_skiped = False
                    break

            # while True:
            #     # 定位列名；校验列名；期望值(校验值)；定位行号;是否特殊处理
            #     skip_info = self.skip_to_page(case_result, col_pos_info)
            #     link_text = skip_info['LINK_TEXT']
            #     org_name = self.tst_inst.get_input_val(case_result[2])
            #     if skip_info['IS_SKIPED']:
            #         # 跳转后的链接值
            #         after_text = skip_info['AFTER_TEXT']
            #         if not bool(skip_info['EL_A']) or after_text is None or after_text.endswith('所'):  # 校验列没有链接；跳转后没值或到供电所时，停止跳转
            #             break
            #         if org_name == original_org_name or link_text != org_name:  # 校验下钻传值是否正确
            #             raise AssertError('当前供电单位“{}”下钻失败， “{}”不是期望的供电单位！'.format(link_text, org_name))
            #     elif not bool(skip_info['EL_A']):
            #         DataAccess.el_operate_log(self.tst_inst.menu_no, self.tst_inst.tst_case_id, None, self.tst_inst.class_name, '跳转失败' + assert_type,
            #                                   '“{}”没查询结果，故对下属单位下钻失败！'.format(org_name))
            #         is_skiped = False
            #         break
            #     else:
            #         is_skiped = False
            #         break

            org_node = DataAccess.get_org_node_by_name(original_org_name)
            self.tst_inst.openLeftTree(org_node)
            self.tst_inst.btn_qry()

            return is_skiped
        else:
            raise AssertError('没查询结果， 下钻跳转验证失败！！')

class AssertResultLocators:
    # 弹窗的关闭xpath
    WINDOWS_CLOSE = (By.XPATH, '//*[text()="{}"]/../div[1]')
    # WINDOWS_CLOSE_NEW = (By.XPATH, '//div[@class=" x-window x-resizable-pinned"]//span[@class="x-window-header-text" and text()="{}"]')

    # 弹窗页面的
    # WINDOWS_PAGE = (By.XPATH, '//*[@class=" x-window x-window-plain x-resizable-pinned"]')

    # 弹窗标题
    # WINDOWS_NAME = (By.XPATH,  '//span[text()="{}"]')
    DLG_TITLE = (By.XPATH, '//div[@class=" x-window x-resizable-pinned"]//span[@class="x-window-header-text" and text()="{}"]')

    # 菜单页的名称
    MENU_NAME = (By.XPATH, '//span[@class="x-tab-strip-inner"]/span[contains(text(),"{}")]')

    # DISPLAY_ELEMENT = (
    #     By.XPATH, '// *[text() ="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]')

    # 要滚动到的目标位置
    # DISPLAY_NUM = (By.XPATH, '(//*[text()="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)[1]/td[{}]')

    # 【显示区】
    # 显示区显示表头，
    # TABLE_HEAD = (By.XPATH, '//div[text()="{}"]/ancestor::div[contains(@class,"x-grid-with-col-lines") and not(contains(@class, "x-hide-display"))]//div[@class="x-grid3-viewport"]//tr[@class="x-grid3-hd-row"]')

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

    # DISPLAY_LINE = (By.XPATH,
    #                 '(//*[text()="{0}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)[{1}]/td[{2}]')
    # DISPLAY_LINE_NEW = (By.XPATH,
    #                     '// *[text() ="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]/ancestor::div[@class="x-grid3-viewport"]//*[@class="x-grid3-header"]//td//*[text()="{}"]')

    # 空格
    # DISPLAY_BLANK = (By.XPATH, '//div[@class="x-grid3-row-checker"]')

    # input输入框
    INPUT_BASE_GU = (By.XPATH, '//label[text()= "{}"]/../div[@class=\"x-form-element\"]//input')

    # link 数据是否对应(显示区右下角查询的数据总量)
    # LINK_TOTAL_ROW_INFO = (By.XPATH, '(//*[@id="UserDistStat_DetailGrid"]//tr[@class="x-toolbar-right-row"]//div[@class="xtb-text"])[1]')
    QUERY_RESULT_TOTAL_ROW = (By.XPATH, '//div[@id="{}"]//tr[@class="x-toolbar-right-row"]//div[@class="xtb-text"]')
    # 删除空格
    # CLEAN_BLANK = r'''var elements,el,txt;
    #                     elements= document.evaluate("%s", document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
    #                     for (var i = 0; i < elements.snapshotLength; i++) {
    #                         el= elements.snapshotItem(i);
    #                         txt = el.innerText.replace(new RegExp(/[\s:：\-\(\)（）]/,'g'), '');
    #                         if (txt != el.innerText)
    #                             el.innerText = txt
    #                     }'''


if __name__ == '__main__':
    # skipMenuName = AssertResultLocators.MENU_NAME[1].format(
    #     'cdscsdc')
    # print(skipMenuName)
    pass
