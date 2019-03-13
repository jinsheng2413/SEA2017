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

logger = Logger(logger='AssertResult').getlog()


# 校验新方法
class AssertResult():
    def __init__(self, call_from):
        self.tst_inst = call_from
        # logger.info('This test ({}) is exec new assert func.'.format(call_from.menu_no))

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
                # col_pos_info['HIDE_ROWS'] = first_row_idx
                # # 查询结果行数
                # locator = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT, case_result[0])
                # els = self.tst_inst._find_elements(locator)
                # row_cnt = len(els) if bool(els) else 0
                # if row_cnt > 0:
                match_cnt = 0
                # col_pos_info = self.calc_col_idx(case_result[0], case_result[1])
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
        try:
            # 检查查询结果是否有数据
            is_skiped = True
            # 按下面代码执行会报这个错：'FirefoxWebElement' object does not support indexing
            # el_link = el_data_rows[int(case_result[3])].find_elements_by_xpath('./td[{}]//a'.format(col_pos_info['COL_IDX']))
            if link_xpath is None:
                link_xpath = self.tst_inst.format_xpath_multi(AssertResultLocators.QUERY_RESULT_ROW_COL,
                                                              (case_result[0], int(case_result[3]) + col_pos_info['HIDE_ROWS'],
                                                               col_pos_info['COL_IDX']), True)
            el_link = self.tst_inst._find_displayed_element(link_xpath)
            self.tst_inst.scrollTo(el_link)
            el_link.click()
        except Exception as ex:
            print('跳转验证失败:' + ex.__str__())
            is_skiped = False
        return is_skiped

    # def skip_tab_page(self, case_result, case_data):
    #     """
    #     # tab页跳转到另一个页面
    #     :param case_result: tst_case_result 表配置跳转的数据
    #     :param case_data: 整个用例的数据
    #     :return:
    #     """
    #     col_pos_info = self.calc_col_idx(case_result[0], case_result[1])
    #     # 获取要截取的值
    #     map_rela_rslt = DataAccess.get_skip_data(case_data['TST_CASE_ID'], case_result[1])
    #
    #     skip_data_before = self.get_skip_data_before(case_data, case_result, map_rela_rslt)
    #     # old_page_list = []
    #     # new_page_list = []
    #     # # 获取跳转前页面所要携带的值
    #     # for map_rela in map_rela_rslt:
    #     #
    #     #     if map_rela[10] == '1':
    #     #         old_page_list.append(map_rela[9])
    #     #     # 获取查询条件输入框的值
    #     #     elif map_rela[4] == '01':
    #     #         locator_qry = self.get_xpath(DataAccess.get_xpath_tab_data(map_rela[5], case_id, caseData['TAB_NAME']))
    #     #         old_page_list.append(self.get_text(locator_qry))
    #     #     else:
    #     #         loc_col_name = case_result[0]
    #     #         col_idx = self.calc_col_idx(loc_col_name, map_rela[5])['COL_IDX']
    #     #         locator = self.get_xpath(loc_col_name, map_rela[3], col_idx, type=2)
    #     #         old_page_list.append(self.tst_inst.driver.find_element(*locator).text)
    #
    #     # 跳转到对应的页面
    #     self.skip_to_page(case_result, col_pos_info)
    #
    #     # 校验页面的名称是否正确
    #     name = self.assert_page_name(case_result[2])
    #     if name == False:
    #         print('跳转{}到页面失败'.format(case_result[2]))
    #
    #     # 判断文字是否正确
    #     skip_data_after = self.get_skip_data_after(case_result, map_rela_rslt)
    #     # for map_rela in map_rela_rslt:
    #     #     if map_rela[8] == None and map_rela[4] == '04':
    #     #         try:
    #     #             resd = self.driver.find_element(*AssertResultLocators.LINK_DATA).text
    #     #             resd_new = resd[resd.index('/') + 1:len(resd)].strip()
    #     #             new_page_list.append(resd_new)
    #     #         except:
    #     #             new_page_list.append('0')
    #     #     elif map_rela[10] == '1':
    #     #         new_page_list.append(map_rela[9])
    #     #
    #     #     else:
    #     #         try:
    #     #             text = self.get_text(self.get_xpath(DataAccess.get_xpath_tab_data(map_rela[8], case_id, case_result[2])))
    #     #             new_page_list.append(text)
    #     #         except:
    #     #             logger.error('跳转的新页面时数据没有带过去')
    #     #             return False
    #
    #     # 返回前一个tab页
    #     self.tst_inst.clickTabPage(case_data['TAB_NAME'])
    #
    #     # 跳转传值验证是否正确
    #     return self.check_skip_data(col_pos_info, map_rela_rslt, case_result[3], skip_data_before, skip_data_after)
    #     # Error_res = True
    #     # col_idx = col_pos_info['COL_IDX'] - col_pos_info['HIDE_COLS']
    #     # info = '跳转坐标（{}行,{}列）element_sn:{}跳转前:xpath:{}、值：{}-----跳转后:xpath:{}、值：{}'
    #     # for x, y, map_rela in zip(old_page_list, new_page_list, map_rela_rslt):
    #     #     info_rlt = info.format(case_result[3], col_idx, map_rela[11], map_rela[5], x, map_rela[8], y)
    #     #     if x == y:
    #     #         logger.info(info_rlt)
    #     #     elif map_rela[7] == '02':
    #     #         if x in y:
    #     #             logger.info(info_rlt)
    #     #         elif map_rela[7] == '03':
    #     #             if (x == '全部') & (y == ''):
    #     #                 logger.info(info_rlt)
    #     #             elif x == y:
    #     #                 logger.info(info_rlt)
    #     #     else:
    #     #         err_info = '跳转传值错误:' + info_rlt
    #     #         logger.error(err_info)
    #     #         print('</br>' + err_info + '</br>')
    #     #         Error_res = False
    #     # return Error_res

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
        #
        # loc = self.tst_inst.format_xpath_multi(AssertResultLocators.TABLE_HEAD, loc_col_name, True)
        # el_tr = self.tst_inst._find_displayed_element(loc, idx=idx)
        #
        # # print('表格列名清单', el_tr.text)
        #
        # col_pos_info = {'COL_IDX': 0, 'EL_COL': None, 'HIDE_COLS': 0, 'FIRST_COL_IDX': 0, 'EL_FIRST': None, 'COL_IS_HIDED': True}
        # # 查找表头所有列名元素
        # el_tds = el_tr.find_elements_by_xpath('./td')
        # if bool(el_tds):
        #     # 隐藏列个数
        #     hide_cols = 0
        #     for i, el in enumerate(el_tds):
        #         # el_label = el.text
        #         el_label = self.tst_inst.get_el_text(el)
        #         el_label = Utils.replace_chrs(el_label, ' \r\n\t')
        #         if self.tst_inst.el_is_hided(el):
        #             hide_cols += 1
        #         else:
        #             if col_pos_info['EL_FIRST'] is None and el.is_displayed():
        #                 # 第一个带标签，且显示的列
        #                 col_pos_info['EL_FIRST'] = el
        #                 col_pos_info['FIRST_COL_IDX'] = i + 1
        #             if el_label == col_name:
        #                 col_pos_info['COL_IS_HIDED'] = not el.is_displayed()
        #                 col_pos_info['EL_COL'] = el
        #                 # 表头列名位置，xpath元素下表以1开始，故+1
        #                 col_pos_info['COL_IDX'] = i + 1
        #                 break
        #     col_pos_info['HIDE_COLS'] = hide_cols
        #     logger.info('\r“{}”在表格中计算结果：第{}列（其中隐藏列{}列），且{}。\r'.format(col_name, col_pos_info['COL_IDX'], hide_cols,
        #                                                               ('不可见' if col_pos_info['COL_IS_HIDED'] else '可见')))
        #     return col_pos_info
        # else:
        #     raise AssertError('定位列{}在表格中的位置时报错！'.format(col_name))

    def skip_windows_page(self, case_result, col_pos_info):
        """
        窗口跳转
        :param case_result: 以，为分隔符，定位列名；校验列名；期望值(校验值)；定位行号;是否特殊处理
        :return:
        """

        # 【滚动到链接列名所在位置】
        # 计算链接列名列序号（包括隐藏列）  --【终端信息维护】  【终端调试信息】
        # 定位列名；校验列名；期望值；定位行号;是否特殊处理
        is_find, first_row_idx, row_cnt = self.query_records(case_result[0])
        if is_find:
            col_pos_info['HIDE_ROWS'] = first_row_idx
            self.tst_inst.scrollTo(col_pos_info['EL_COL'])
            # 跳转到目标页
            is_skiped = self.skip_to_page(case_result, col_pos_info)
            if is_skiped:
                sleep(2)
                # 关闭窗口
                close_xpath = self.tst_inst.format_xpath(AssertResultLocators.WINDOWS_CLOSE, case_result[2])
                el = self.tst_inst._direct_find_element(close_xpath)
                el.click()
            self.tst_inst.scrollTo(col_pos_info['EL_FIRST'])
        else:
            raise AssertError('没查询结果， 跳转验证失败！！')
        return is_skiped

    # def clickSkip(self, case_result, case_data):
    #     """
    #
    #     :param case_result: tst_case_result 验证数据
    #     :param case_data: 用例所有数据
    #     :param model: 老版本校验期望值
    #     :param version: 1为老版本，2为新版本
    #     :return:
    #     """
    #     try:
    #         col_pos_info = self.calc_col_idx(case_result[0], case_result[1])
    #         # 查询结果行数
    #         locator = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT, case_result[0])
    #         els = self.tst_inst._find_elements(locator)
    #         if bool(els) > 0:
    #             case_id = case_data['TST_CASE_ID']
    #             # 获取要截取的值
    #             map_rela_rslt = DataAccess.get_skip_data(case_id, case_result[1])
    #             skip_data_before = self.get_skip_data_before(case_data, case_result, map_rela_rslt)
    #             # skip_data_before = []
    #             # skip_data_after = []
    #             # for map_rela in map_rela_rslt:
    #             #     if map_rela[10] == '1':
    #             #         skip_data_before.append(map_rela[9])
    #             #     # 获取查询条件输入框的值
    #             #     elif map_rela[4] == '01':
    #             #         locator_qry = self.get_xpath(DataAccess.get_xpath_tab_data(map_rela[5], case_id, case_data['TAB_NAME']))
    #             #         skip_data_before.append(self.get_text(locator_qry))
    #             #     else:
    #             #         loc_col_name = case_result[0]
    #             #         col_idx = self.calc_col_idx(loc_col_name, map_rela[5])['COL_IDX']
    #             #         locator = self.get_xpath(loc_col_name, map_rela[3], col_idx, type=2)
    #             #         skip_data_before.append(self.tst_inst.driver.find_element(*locator).text)
    #
    #             # 跳转到对应的页面
    #             self.skip_to_page(case_result, col_pos_info)
    #             # 校验页面的名称是否正确
    #             name = self.assert_page_name(case_result[2])
    #             if name == False:
    #                 print('跳转{}到页面失败'.format(case_result[2]))
    #             # 判断文字是否正确
    #             skip_data_after = self.get_skip_data_after(case_result, map_rela_rslt)
    #             # for map_rela in map_rela_rslt:
    #             #     if map_rela[8] == None and map_rela[4] == '04':
    #             #         try:
    #             #             resd = self.tst_inst.driver.find_element(*AssertResultLocators.LINK_DATA).text
    #             #             resd_new = resd[resd.index('/') + 1:len(resd)].strip()
    #             #             skip_data_after.append(resd_new)
    #             #         except:
    #             #             skip_data_after.append('0')
    #             #     elif map_rela[10] == '1':
    #             #         skip_data_after.append(map_rela[9])
    #             #     else:
    #             #         try:
    #             #             v_xpath = self.get_xpath(DataAccess.get_xpath_menu_data(map_rela[8], case_result[2], map_rela[6]))
    #             #             self.tst_inst.sleep_time(1)
    #             #             text = self.get_text(v_xpath)
    #             #             skip_data_after.append(text)
    #             #         except:
    #             #             logger.error('获取跳转到新页面的时，获取xpath')
    #             #             return False
    #
    #             self.tst_inst.menuPage.closePage(case_result[2])
    #             # 校验跳转传值是否正确
    #             # Error_res = True
    #             # col_idx = col_pos_info['COL_IDX'] - col_pos_info['HIDE_COLS']
    #             # info = '跳转坐标（{}行,{}列）element_sn:{}跳转前:xpath:{}、值：{}-----跳转后:xpath:{}、值：{}'
    #             # for x, y, map_rela in zip(skip_data_before, skip_data_after, map_rela_rslt):
    #             #     formated_info = info.format(case_result[3], col_idx, map_rela[11], map_rela[5], x, map_rela[8], y)
    #             #     if x == y:
    #             #         logger.info(formated_info)
    #             #     elif map_rela[7] == '02':
    #             #         if x in y:
    #             #             logger.info(formated_info)
    #             #     elif map_rela[7] == '03':
    #             #         if (x == '全部') & (y == ''):
    #             #             logger.info(formated_info)
    #             #         elif x == y:
    #             #             logger.info(formated_info)
    #             #     else:
    #             #         err_info = '跳转传值错误:' + formated_info
    #             #         logger.error(err_info)
    #             #         print('</br>' + err_info + '</br>')
    #             #         Error_res = False
    #             # return False if Error_res == False else True
    #             return self.check_skip_data(col_pos_info, map_rela_rslt, case_result[3], skip_data_before, skip_data_after)
    #     except:
    #         print('21跳转验证失败')
    #         return False
    #

    def check_query_result(self, para, isDisplay=False):
        """

        :param para: 用例数据
        :param version: 1为老版本，2为新版本
        :return: 返回校验结果
        """
        esplain = {
            '11': '显示区未查询出结果',
            '12': '按条件查询出的结果与期望值不一致',
            '21': '跳转菜单页面不正确',
            '22': '跳转弹窗不正确',
            '23': '跳转tab页不正确',
            '24': '跳转弹窗的名称带的值不正确',
            '25': '跳转到新的菜单页，但不携带值错误',
            '26': '单列数据有两个跳转',
            '27': 'tab页套多个tab页',
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
            assert_type = row[0]
            case_result = row[1:]
            if assert_type not in ['11', '31']:
                col_and_link_tag = self.special_deal(case_result[4], case_result[1])
                col_pos_info = self.calc_col_idx(case_result[0], col_and_link_tag[0])
            logger.info('*******' + case_id + '*********校验类别：{}；定位列名：{}；校验列名：{}；期望值：{}；定位行号：{};是否特殊处理：{}\r'.format(*row))
            if assert_type == '11':  # 【OK】
                locator = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT, case_result[0])
                assert_rslt = self.assert_context(locator)
            elif assert_type == '12':  # 判断值是否准确,item截取字符串，在转换成列表
                assert_rslt = self.assertValue(case_result, col_pos_info)
            elif assert_type == '21':  # 【OK】 # 判断跳转的页面是否是指定页面,item截取字符串，在转换成列表
                # assert_rslt = self.clickSkip(case_result, para)
                assert_rslt = self.skip_menu_tab_page(assert_type, para, case_result, col_pos_info)
            elif assert_type == '22':  # 【OK】
                assert_rslt = self.skip_windows_page(case_result, col_pos_info)
            elif assert_type == '23':
                # assert_rslt = self.skip_tab_page(case_result, para)
                assert_rslt = self.skip_menu_tab_page(assert_type, para, case_result, col_pos_info, is_menu=False)
            elif assert_type == '24':
                assert_rslt = self.tab_skip_into_window(case_result, col_pos_info)
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
            elif assert_type == '31':
                assert_rslt = self.assertInput(case_id, case_result)

            ls_check_rslt[i] = {assert_type: assert_rslt}

        result = True
        # 处理判断结果，具体那一步出错
        ls_check_rslt_values = ls_check_rslt.values()
        for item in ls_check_rslt_values:
            for key, value in item.items():
                if value == False:
                    err_info = '错误类型:{}'.format(esplain[key])
                    logger.error(err_info)  # 出错具体原因
                    print(err_info)
                    result = value
                    return result
        return result

    # 获取文本框的内容
    def get_xpath(self, *agrs, type=1):
        """
        1.输入框
        2.显示区第几行第几列值

        """
        if type == 1:
            xpath = self.tst_inst.format_xpath(AssertResultLocators.INPUT_BASE_GU, agrs[0])
        elif type == 2:
            # xpath = self.tst_inst.format_xpath(AssertResultLocators.DISPLAY_LINE, (agrs[0], agrs[1], agrs[2]))
            xpath = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT_ROW_COL, (agrs[0], agrs[1], agrs[2]))
        return xpath


    # def clean_empty_blank(self, tag_text, tag_name='div'):
    #     """
    #     剔除标签中的空白字符及冒号：:
    #     :param tag_text: 标签中第一个连续中英文
    #     :param tag_name: 要剔除的tag
    #     """
    #     clean_obj = {'div': "//div[contains(text(),'{}')]".format(tag_text)}
    #     tn = clean_obj[tag_name]
    #     # print(tn)
    #     script = AssertResultLocators.CLEAN_BLANK % tn
    #     # print(script)
    #     self.tst_inst.exec_script(script)

    def get_text(self, locator):
        el = self.tst_inst._find_displayed_element(locator)
        return el.get_attribute('value')

    def assertInput(self, case_id, case_result):
        """
        获取单个
        :param case_result:
        :param case_id:
        :return:
        """
        xpath = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT_BY_INPUT, (case_result[0], case_result[1]))
        val = self.get_text(xpath)
        if case_result[2] == val:
            logger.info('查询详细信息的输入框的值与期望结果一样')
            return True
        else:
            logger.error('查询详细信息的输入框的值与期望结果不一致')
            return False

    def tab_skip_into_window(self, case_result, col_pos_info):
        """
        弹窗为非固定值的跳转，窗口名为所在行某一列的值
        :param case_result:
        :return:
        """
        is_find, first_row_idx, row_cnt = self.query_records(case_result[0])
        if is_find:
            col_pos_info['HIDE_ROWS'] = first_row_idx
            col_idx = self.calc_col_idx(case_result[0], case_result[2])['COL_IDX']
            xpath = self.tst_inst.format_xpath(AssertResultLocators.QUERY_RESULT_ROW_COL, (case_result[0], case_result[3], col_idx))
            dlg_title = self.tst_inst.driver.find_element(*xpath).text

            self.skip_to_page(case_result, col_pos_info)

            tab_xpath = self.tst_inst.format_xpath(AssertResultLocators.DLG_TITLE, dlg_title)
            res = self.assert_context(tab_xpath)
            self.tst_inst.sleep_time(2)

            self.tst_inst.click((By.XPATH, tab_xpath[1] + '/../div[1]'))
        else:
            raise AssertError('没查询结果， 跳转验证失败！！')
        return res

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
        skip_data_before = []
        for map_rela in map_rela_rslt:
            if map_rela[10] == '1':  # 是否转换
                skip_data_before.append(map_rela[9])  # 转换后的值
            # 获取查询条件输入框的值
            elif map_rela[4] == '01':  # 页面元素类型：【01-查询条件（XPATH)】;02-表格列对应值;03-表格列名;04-读取统计数与明细对比
                # 把查询条件的xpath转换为对应查询条件中文名
                xpath_name = DataAccess.get_xpath_tab_data(map_rela[5], case_data['TST_CASE_ID'], case_data['TAB_NAME'])
                locator_qry = self.get_xpath(xpath_name)
                skip_data_before.append(self.get_text(locator_qry))
            else:
                loc_col_name = case_result[0]
                col_idx = self.calc_col_idx(loc_col_name, map_rela[5])['COL_IDX']
                locator = self.get_xpath(loc_col_name, case_result[3], col_idx, type=2)
                skip_data_before.append(self.tst_inst.driver.find_element(*locator).text)
        print('skip_data_before:', skip_data_before)
        return skip_data_before

    def get_skip_data_after(self, case_result, map_rela_rslt):
        skip_data_after = []
        for map_rela in map_rela_rslt:
            if map_rela[8] == None and map_rela[4] == '04':
                try:
                    resd = self.tst_inst.driver.find_element(*AssertResultLocators.LINK_TOTAL_ROW_INFO).text
                    resd_new = resd[resd.index('/') + 1:len(resd)].strip()
                    skip_data_after.append(resd_new)
                except:
                    skip_data_after.append('0')
            elif map_rela[10] == '1':
                skip_data_after.append(map_rela[9])
            else:
                try:
                    v_xpath = self.get_xpath(DataAccess.get_xpath_menu_data(map_rela[8], case_result[2], map_rela[6]))
                    self.tst_inst.sleep_time(1)
                    text = self.get_text(v_xpath)
                    skip_data_after.append(text)
                except:
                    logger.error('跳转的新页面/窗口时数据没有带过去')
                    return False
        print('skip_data_after:', skip_data_after)
        return skip_data_after

    def check_skip_data(self, col_pos_info, map_rela_rslt, row_idx, skip_data_before, skip_data_after):
        is_skip_correct = True
        col_idx = col_pos_info['COL_IDX'] - col_pos_info['HIDE_COLS']
        info = '跳转坐标（{}行,{}列）element_sn:{}跳转前:xpath:{}、值：{}-----跳转后:xpath:{}、值：{}'
        for x, y, map_rela in zip(skip_data_before, skip_data_after, map_rela_rslt):
            info_rlt = info.format(row_idx, col_idx, map_rela[11], map_rela[5], x, map_rela[8], y)
            if x == y:
                logger.info(info_rlt)
            elif map_rela[7] == '02':
                if x in y:
                    logger.info(info_rlt)
            elif map_rela[7] == '03':
                if (x == '全部') & (y == ''):
                    logger.info(info_rlt)
                elif x == y:
                    logger.info(info_rlt)
            else:
                err_info = '跳转传值错误:' + info_rlt
                logger.error(err_info)
                print('</br>' + err_info + '</br>')
                is_skip_correct = False
        return is_skip_correct

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
            self.skip_to_page(case_result, col_pos_info, link_xpath)

            # 校验页面的名称是否正确
            is_skiped = self.assert_page_name(case_result[2])
            if is_skiped == False:
                print('跳转{}到页面失败'.format(case_result[2]))

            # 获取跳转目标页面相关元素值
            skip_data_after = self.get_skip_data_after(case_result, map_rela_rslt)

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
            raise AssertError('没查询结果， 跳转验证失败！！')

    # def skip_two_link(self, case_result, case_data):
    #     """
    #
    #     :param case_result: 查询结果校验列表内容：定位列名；校验列名；期望值；定位行号;是否特殊处理
    #     :param case_data:
    #     :return:
    #     """
    #     is_special = case_result[4]
    #     if is_special == 'Y':
    #         col_and_link_tag = case_result[1].split('-')
    #         col_name = col_and_link_tag[0]
    #         link_tab = col_and_link_tag[1]
    #     else:
    #         col_name = case_result[1]
    #         link_tab = ''
    #
    #     col_pos_info = self.calc_col_idx(case_result[0], col_name)
    #
    #     case_id = case_data['TST_CASE_ID']
    #     # 获取跳转映射对应关系
    #     map_rela_rslt = DataAccess.get_skip_data(case_id, case_result[1])
    #     """
    #     /*带*字段来自tst_case_result， 其余来自tst_col_link_rela
    #     xpath_type:页面元素类型：01-查询条件（XPATH);02-表格列对应值;03-表格列名;04-读取统计数与明细对比
    #     0源:列定位字段     1Tab页名称  2源:跳转字段名  3取值行号 4页面元素类型  5页面元素  6目标页面Tab页名称     7转换类型   8目标页面元素      9转换后的值  10是否转换  11源xpath序号
    #     TAB_COLUMN_NAME*  TAB_NAME   COLUMN_NAME*    ROW_NUM*  XPATH_TYPE     XPATH      TARGET_TAB_NAME     TRANS_TYPE  TARGET_XPATH      TRANS_VALUE  IS_TRANS    ELEMENT_SN
    #                                  同col_name
    #     用户编号          终端调试    备注-报文查询    1         02             用户编号    01                  01          CONS_NO                        0           1
    #     用户编号          终端调试    备注-报文查询    1         02             用户名称    01                  01          CONS_NAME                      0           2
    #     用户编号          终端调试    备注-报文查询    1         02             终端地址    01                  01          TMNL_ADDR                      0           3
    #     """
    #     skip_data_before = self.get_skip_data_before(case_data, case_result, map_rela_rslt)
    #     # for map_rela in map_rela_rslt:
    #     #     if map_rela[10] == '1': # 是否转换
    #     #         old_page_list.append(map_rela[9])   # 转换后的值
    #     #     # 获取查询条件输入框的值
    #     #     elif map_rela[4] == '01': # 页面元素类型：【01-查询条件（XPATH)】;02-表格列对应值;03-表格列名;04-读取统计数与明细对比
    #     #         # 把查询条件的xpath转换为对应查询条件中文名
    #     #         xpath_name = DataAccess.get_xpath_tab_data(map_rela[5], case_id, case_data['TAB_NAME'])
    #     #         locator_qry = self.get_xpath(xpath_name)
    #     #         old_page_list.append(self.get_text(locator_qry))
    #     #     else:
    #     #         loc_col_name = case_result[0]
    #     #         col_idx = self.calc_col_idx(loc_col_name, map_rela[5])['COL_IDX']
    #     #         locator = self.get_xpath(loc_col_name, case_result[3], col_idx, type=2)
    #     #         old_page_list.append(self.tst_inst.driver.find_element(*locator).text)
    #     # 定位列名；校验列名；期望值(校验值)；定位行号;是否特殊处理
    #     link_xpath = self.tst_inst.format_xpath_multi(AssertResultLocators.QUERY_RESULT_ROW_COL_LINKS,
    #                                                   (case_result[0], case_result[3], col_pos_info['COL_IDX'], link_tab), True)
    #     self.skip_to_page(case_result, col_pos_info, link_xpath)
    #     # self.tst_inst.scrollTo(link_xpath)
    #     # self.tst_inst.click(link_xpath)
    #
    #     # 校验页面的名称是否正确
    #     is_skiped = self.assert_page_name(case_result[2])
    #     if is_skiped == False:
    #         print('跳转{}到页面失败'.format(case_result[2]))
    #
    #     # 获取跳转目标页面相关元素值
    #     skip_data_after = self.get_skip_data_after(case_result, map_rela_rslt)
    #     # for map_rela in map_rela_rslt:
    #     #     if map_rela[8] == None and map_rela[4] == '04':
    #     #         try:
    #     #             resd = self.tst_inst.driver.find_element(*AssertResultLocators.LINK_DATA).text
    #     #             resd_new = resd[resd.index('/') + 1:len(resd)].strip()
    #     #             new_page_list.append(resd_new)
    #     #         except:
    #     #             new_page_list.append('0')
    #     #     elif map_rela[10] == '1':
    #     #         new_page_list.append(map_rela[9])
    #     #     else:
    #     #         try:
    #     #             v_xpath = self.get_xpath(DataAccess.get_xpath_menu_data(map_rela[8], case_result[2], map_rela[6]))
    #     #             self.tst_inst.sleep_time(1)
    #     #             text = self.get_text(v_xpath)
    #     #             new_page_list.append(text)
    #     #         except:
    #     #             logger.error('跳转的新页面时数据没有带过去')
    #     #             return False
    #     # print('old:', new_page_list)
    #
    #     # 关闭菜单页
    #     self.tst_inst.menuPage.closePage(case_result[2])
    #     first_col_idx = self.tst_inst.format_xpath_multi(AssertResultLocators.QUERY_RESULT_ROW_COL,
    #                                                   (case_result[0], case_result[3], col_pos_info['FIRST_COL_IDX']), True)
    #     self.tst_inst.scrollTo(first_col_idx)
    #
    #     # 校验跳转传值是否正确
    #     return self.check_skip_data(col_pos_info, map_rela_rslt, case_result[3], skip_data_before, skip_data_after)

    # def skip_more_tab_link(self, case_result, case_data):
    #     """
    #     # tab页跳转sxs
    #     :param case_result: tst_case_result 校验数据
    #     :param case_data: 整个用例的数据
    #     :return:
    #     """
    #     is_special = case_result[4]
    #     if is_special == 'Y':
    #         col_and_link_tag = case_result[1].split('-')
    #         col_name = col_and_link_tag[0]
    #         tab_page_name = col_and_link_tag[1]
    #     else:
    #         col_name = case_result[1]
    #         tab_page_name = ''
    #
    #     col_pos_info = self.calc_col_idx(case_result[0], col_name)
    #
    #     case_id = case_data['TST_CASE_ID']
    #     # 获取要截取的值
    #     map_rela_rslt = DataAccess.get_skip_data(case_id, case_result[1])
    #     skip_data_before = self.get_skip_data_before(case_data, case_result, map_rela_rslt)
    #     # skip_data_after = []
    #     # for map_rela in map_rela_rslt:
    #     #     if map_rela[10] == '1':
    #     #         skip_data_before.append(map_rela[9])
    #     #     # 获取查询条件输入框的值
    #     #     elif map_rela[4] == '01':
    #     #         locator_qry = self.get_xpath(DataAccess.get_xpath_tab_data(map_rela[5], case_id, case_data['TAB_NAME']))
    #     #         skip_data_before.append(self.get_text(locator_qry))
    #     #     else:
    #     #         loc_col_name = case_result[0]
    #     #         col_idx = self.calc_col_idx(loc_col_name, map_rela[5])['COL_IDX']
    #     #         locator = self.get_xpath(loc_col_name, map_rela[3], col_idx, type=2)
    #     #         skip_data_before.append(self.tst_inst.driver.find_element(*locator).text)
    #
    #     pageRes = ''
    #     # 跳转到对应的页面
    #     self.skip_to_page(case_result, col_pos_info)
    #     # 校验页面的名称是否正确
    #     name = self.assert_page_name(case_result[2])
    #     if name == False:
    #         print('跳转{}到页面失败'.format(case_result[2]))
    #     # 判断文字是否正确
    #     skip_data_after = self.get_skip_data_after(case_result, map_rela_rslt)
    #
    #     # for map_rela in map_rela_rslt:
    #     #     if map_rela[8] == None and map_rela[4] == '04':
    #     #         try:
    #     #             resd = self.driver.find_element(*AssertResultLocators.LINK_DATA).text
    #     #             resd_new = resd[resd.index('/') + 1:len(resd)].strip()
    #     #             skip_data_after.append(resd_new)
    #     #         except:
    #     #             skip_data_after.append('0')
    #     #     elif map_rela[10] == '1':
    #     #         skip_data_after.append(map_rela[9])
    #     #
    #     #     else:
    #     #         try:
    #     #             v_xpath = self.get_xpath(DataAccess.get_xpath_menu_data(map_rela[8], case_result[2], map_rela[6]))
    #     #             self.tst_inst.sleep_time(1)
    #     #             text = self.get_text(v_xpath, second=1)
    #     #             skip_data_after.append(text)
    #     #         except:
    #     #             logger.error('获取新页面的值失败')
    #     #             return False
    #
    #     # 返回前一个tab页
    #     self.tst_inst.menuPage.closePage(case_result[2])
    #     # 跳转传值验证是否正确
    #     # Error_res = True
    #     # col_idx = col_pos_info['COL_IDX'] - col_pos_info['HIDE_COLS']
    #     # info = '跳转坐标（{}行,{}列）element_sn:{}跳转前:xpath:{}、值：{}-----跳转后:xpath:{}、值：{}'
    #     # for x, y, map_rela in zip(skip_data_before, skip_data_after, map_rela_rslt):
    #     #     info_rlt = info.format(case_result[3], col_idx, map_rela[11], map_rela[5], x, map_rela[8], y)
    #     #     if x == y:
    #     #         logger.info(info_rlt)
    #     #     elif map_rela[7] == '02':
    #     #         if x in y:
    #     #             logger.info(info_rlt)
    #     #         elif map_rela[7] == '03':
    #     #             if (x == '全部') & (y == ''):
    #     #                 logger.info(info_rlt)
    #     #             elif x == y:
    #     #                 logger.info(info_rlt)
    #     #     else:
    #     #         err_info = '跳转传值错误:' + info_rlt
    #     #         logger.error(err_info)
    #     #         print('</br>' + err_info + '</br>')
    #     #         Error_res = False
    #     # return Error_res
    #     return self.check_skip_data(col_pos_info, map_rela_rslt, case_result[3], skip_data_before, skip_data_after)

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
    QUERY_RESULT_ROW_COL = (
        By.XPATH,
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
    LINK_TOTAL_ROW_INFO = (By.XPATH, '(//*[@id="UserDistStat_DetailGrid"]//tr[@class="x-toolbar-right-row"]//div[@class="xtb-text"])[1]')
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
