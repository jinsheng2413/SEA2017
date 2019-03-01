# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: assert_result.py
@time: 2019/1/15 0015 9:32
@desc:
"""
from selenium.webdriver.common.by import By

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.logger import Logger
from com.nrtest.common.utils import Utils

logger = Logger(logger='AssertResult').getlog()

#校验新方法
class AssertResult():
    def __init__(self, call_from):
        self.tst_inst = call_from

    def save_img(self, img_path, img_name):
        self.tst_inst.save_img(img_path, img_name)

    def popup(self, img_path, img_name, *args):
        return self.tst_inst.popup(img_path, img_name, *args)

    def click_link(self, column_name, line, colum_only_one='', only=1):
        """
        点击链接
        :param column_name:
        :param line:
        :param colum_only_one:
        :param only:
        """
        column = self.tst_inst.calc_col_idx(column_name)
        num = self.tst_inst.element_cnt(column_name)
        if num > 0:
            if only == 1:
                col_name = column_name
            else:  # 2
                col_name = colum_only_one
            xpath = self.tst_inst.format_xpath(AssertResultLocators.DISPLAY_LINE, (col_name, column, line))
            self.tst_inst.click(xpath)

            # if only == 1 and num > 0:
            #     self.tst_inst.click(self.tst_inst.combination_xpath(column_name, column, line))
            # elif only == 2 and num > 0:
            #     self.tst_inst.click(self.tst_inst.combination_xpath(colum_only_one, column, line))

    def assert_page_name(self, page_name):
        """
        判断跳转的页面的名称是否正确
        :param page_name:
        :return:
        """
        xpath = self.tst_inst.format_xpath(AssertResultLocators.MENU_NAME, page_name)
        return self.tst_inst.assert_context(xpath)
        # skipMenuName = AssertResultLocators.MENU_NAME[1].format(page_name)
        # result = self.tst_inst.assert_context((By.XPATH, skipMenuName))
        # return result

    @BeautifulReport.add_popup_img(6)
    def skip_to_page(self, skipValue, iSchange=False):
        """
        链接跳转:跳转到另一个页面
        :param skipValue:
        :return:
        """
        try:
            displayElement = '// *[text() ="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]'.format(
                skipValue[0])
            self.tst_inst.commonWait((By.XPATH, displayElement))
            el_cnts = len(self.tst_inst._find_elements((By.XPATH, displayElement)))
            if el_cnts > 0:
                if 1:
                    if iSchange:
                        line_name = skipValue[1].split('-')[1]
                    else:
                        line_name = skipValue[1]

                    lineName = self.tst_inst.calc_col_idx(line_name)  # 判断是那一列
                    displayLine = '(//*[text()="{0}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)[{1}]/td[{2}]//a'.format(
                        skipValue[0], skipValue[3], lineName)
                    try:
                        # 点击要跳转的链接
                        self.tst_inst.click((By.XPATH, displayLine))
                    except:
                        print('跳转验证失败')
        except:
            print('验证失败')
        return ()

    def page_back(self, menuPage='请输入菜单页名称', tab='请输入tab页名称', popUpWindow='请输入弹窗页名称'):
        """
        #页面的返回（包含弹窗、tab的页、菜单页）

        :param menuPage: 菜单页
        :param tab: tab页
        :param popUpWindow: 弹窗
        :return:
        """
        dic = {1: menuPage, 2: tab, 3: popUpWindow}
        # 判断跳转是什么类型的页面
        page = None
        for key, value in dic.items():
            if '请输入' not in value:
                page = key
                break
        if page == 1:
            # 关闭菜单页
            # self.tst_inst.closePages(page_name=menuPage, isCurPage=False)
            self.tst_inst.closePages(menuPage)
        elif page == 2:
            # 切换到另一个tab页
            self.tst_inst.clickTabPage(tab)
        elif page == 3:
            self.tst_inst.click(AssertResultLocators.WINDOWS_CLOSE)

    def skip_tab_page(self, case_result, caseData):
        """
        # tab页跳转到另一个页面
        :param case_result: tst_case_result 表配置跳转的数据
        :param caseData: 整个用例的数据
        :return:
        """
        case_id = caseData['TST_CASE_ID']
        # 获取要截取的值
        old_data = DataAccess.get_skip_data(case_id, case_result[1])
        old_page_list = []
        new_page_list = []
        # 获取跳转前页面所要携带的值
        for item in old_data:

            if item[10] == '1':
                old_page_list.append(item[9])
            # 获取查询条件输入框的值
            elif item[4] == '01':
                locator_qry = self.get_xpath(
                    DataAccess.get_xpath_tab_data(item[5], case_id, caseData['TAB_NAME'])[0][0])
                old_page_list.append(self.get_text(locator_qry))
            else:
                line = self.tst_inst.calc_col_idx(item[5])
                locator = self.get_xpath(item[0], item[3], line, type=2)
                old_page_list.append(self.tst_inst.driver.find_element(*locator).text)
        pageRes = ''
        # 跳转到对应的页面
        self.skip_to_page(case_result)
        # 校验页面的名称是否正确
        name = self.assert_page_name(case_result[2])
        if name == False:
            print('跳转{}到页面失败'.format(case_result[2]))
        # 判断文字是否正确
        for item in old_data:
            if item[8] == None and item[4] == '04':
                try:
                    resd = self.driver.find_element(*AssertResultLocators.LINK_DATA).text
                    resd_new = resd[resd.index('/') + 1:len(resd)].strip()
                    new_page_list.append(resd_new)
                except:
                    new_page_list.append('0')
            elif item[10] == '1':
                new_page_list.append(item[9])

            else:
                try:
                    ta = DataAccess.get_xpath_tab_data(item[8], case_id, case_result[2])
                    text = self.get_text(self.get_xpath(ta[0][0]), second=1)
                    new_page_list.append(text)
                except:
                    logger.error('跳转的新页面时数据没有带过去')
                    return False

        # 返回前一个tab页
        self.tst_inst.clickTabPage(caseData['TAB_NAME'])
        # 跳转传值验证是否正确
        Error_res = True
        line = self.tst_inst.calc_col_idx(case_result[1])
        info = '跳转坐标（{}行,{}列）element_sn:{}跳转前:xpath:{}、值：{}-----跳转后:xpath:{}、值：{}'
        for x, y, item in zip(old_page_list, new_page_list, old_data):
            info_rlt = info.format(case_result[3], line, item[11], item[5], x, item[8], y)
            if x == y:
                logger.info(info_rlt)
            elif item[7] == '02':
                if x in y:
                    logger.info(info_rlt)
            else:
                err_info = '跳转传值错误:' + info_rlt
                logger.error(err_info)
                print('</br>' + err_info + '</br>')
                Error_res = False
        return False if Error_res == False else True

    def assert_expect_value(self, locator, value):
        """
        校验期望值是否正确
        :param locator:
        :param value:
        :return:
        """
        res = self.tst_inst.driver.find_element(*locator).text
        res2 = Utils.replace_chrs(res)
        return value in res2

    def skip_windows_page(self, case_result):
        """
        窗口跳转
        :param case_result: 以，为分隔符，第一位是显示区唯一列明，第二位是要校验值的列明，第三位是校验值
        :return:
        """
        try:
            l = self.tst_inst.calc_col_idx(case_result[1], is_num=False)

            xpath = AssertResultLocators.DISPLAY_NUM[1].format(case_result[0], l)
            self.tst_inst.scrollTo((By.XPATH, xpath))
            self.skip_to_page(case_result)
            xpath = AssertResultLocators.WINDOWS_NAME[1].format(case_result[2])
            self.tst_inst.commonWait((By.XPATH, xpath))
            is_skiped = True
        except:
            is_skiped = False
        finally:
            close_xpath = AssertResultLocators.WINDOWS_CLOSE[1].format(case_result[2])

            self.tst_inst.click((By.XPATH, close_xpath))
            back_xpath = AssertResultLocators.DISPLAY_NUM[1].format(case_result[0], 2)
            self.tst_inst.sleep_time(1)
            self.tst_inst.scrollTo((By.XPATH, back_xpath))

        return is_skiped

    def assertValue(self, case_result):
        """
        case_result ='手机,外包队伍名称,test'
        :param assert_values:以，为分隔符，第一位是显示区唯一列明，第二位是要校验值的列明，第三位是校验值
        :return:
        """
        print('-------------------')
        try:
            # 显示区是否有值
            xpath_table = '// *[text() ="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]'.format(
                case_result[0])
            self.tst_inst.commonWait((By.XPATH, xpath_table))
            # 显示区查询出多少结果数量
            displayNum = len(self.tst_inst._find_elements((By.XPATH, xpath_table)))

            diplayName = self.tst_inst.calc_col_idx(case_result[1])  # 判断具体是哪一行
            ringhtNum = 0
            displayLineElement = '(//*[text()="{0}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)[{1}]/td[{2}]//*[contains(text(),"{3}")]'
            if displayNum > 0:

                for i in range(1, displayNum + 1):
                    # 显示区结果的每一行对应列的数据的xpath
                    displayLineElement_index = displayLineElement.format(case_result[0], i, diplayName,
                                                                         case_result[2])
                    try:
                        assert_rslt = self.tst_inst.assert_context((By.XPATH, displayLineElement_index))
                        if assert_rslt:
                            ringhtNum += 1
                        else:
                            print('第{0}行，{1}列显示的值与{2}不一致'.format(i, case_result[1], case_result[2]))
                            break
                    except:
                        print('校验失败')
                return ringhtNum == displayNum

        except:
            print('显示区结果值校验失败')
            return False

    def clickSkip(self, case_result, caseData):

        """

        :param case_result: tst_case_result 验证数据
        :param caseData: 用例所有数据
        :param model: 老版本校验期望值
        :param version: 1为老版本，2为新版本
        :return:
        """
        try:
            case_id = caseData['TST_CASE_ID']
            displayElement = '// *[text() ="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]'.format(
                case_result[0])
            self.tst_inst.commonWait((By.XPATH, displayElement))
            display_num = len(self.tst_inst._find_elements((By.XPATH, displayElement)))
            if display_num > 0:

                # 获取要截取的值
                old_data = DataAccess.get_skip_data(case_id, case_result[1])
                old_page_list = []
                new_page_list = []
                for item in old_data:

                    if item[10] == '1':
                        old_page_list.append(item[9])
                    # 获取查询条件输入框的值
                    elif item[4] == '01':
                        locator_qry = self.get_xpath(
                            DataAccess.get_xpath_tab_data(item[5], case_id, caseData['TAB_NAME'])[0][0])
                        old_page_list.append(self.tst_inst.get_text(locator_qry))
                    else:
                        line = self.tst_inst.calc_col_idx(item[5])
                        locator = self.get_xpath(item[0], item[3], line, type=2)
                        old_page_list.append(self.tst_inst.driver.find_element(*locator).text)
                pageRes = ''
                # 跳转到对应的页面
                self.skip_to_page(case_result)
                # 校验页面的名称是否正确
                name = self.assert_page_name(case_result[2])
                if name == False:
                    print('跳转{}到页面失败'.format(case_result[2]))
                # 判断文字是否正确
                for item in old_data:
                    if item[8] == None and item[4] == '04':
                        try:
                            resd = self.tst_inst.driver.find_element(
                                *AssertResultLocators.LINK_DATA).text
                            resd_new = resd[resd.index('/') + 1:len(resd)].strip()
                            new_page_list.append(resd_new)
                        except:
                            new_page_list.append('0')
                    elif item[10] == '1':
                        new_page_list.append(item[9])
                    else:
                        try:

                            ta = DataAccess.get_xpath_menu_data(item[8], case_result[2], item[6])
                            v_xpath = self.get_xpath(ta[0][0])
                            self.tst_inst.sleep_time(1)
                            text = self.get_text(v_xpath, second=1)
                            new_page_list.append(text)
                        except:
                            logger.error('获取跳转到新页面的时，获取xpath')
                            return False

                self.tst_inst.menuPage.closePage(case_result[2])
                # 校验跳转传值是否正确
                Error_res = True
                line = self.tst_inst.calc_col_idx(case_result[1])
                info = '跳转坐标（{}行,{}列）element_sn:{}跳转前:xpath:{}、值：{}-----跳转后:xpath:{}、值：{}'
                for x, y, item in zip(old_page_list, new_page_list, old_data):
                    info_rlt = info.format(case_result[3], line, item[11], item[5], x, item[8], y)
                    if x == y:
                        logger.info(info_rlt)
                    elif item[7] == '02':
                        if x in y:
                            logger.info(info_rlt)
                    else:
                        err_info = '跳转传值错误:' + info_rlt
                        logger.error(err_info)
                        print('</br>' + err_info + '</br>')
                        Error_res = False
                return False if Error_res == False else True

        except:
            print('21跳转验证失败')
            return False

    def check_query_result(self, para,isDisplay=False):
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
        case_id = para['TST_CASE_ID']
        case_results = DataAccess.get_case_result(case_id)
        display_tab = '// *[text() ="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]'  # 根据XPATH判断显示区是否有值
        ls_check_rslt = {}
        for i,case_result in enumerate(case_results):  # 根据rslt有几个值来判断要做几次校验
            assert_type = case_result[0]
            if assert_type == '11':
                assert_rslt = self.tst_inst.assert_context((By.XPATH, display_tab.format(case_result[1])),
                                                           isDisplay=isDisplay)  # 判断是否有值
            elif assert_type == '12':  # 判断值是否准确,item截取字符串，在转换成列表
                assert_rslt = self.assertValue(case_result[1:])
            elif assert_type == '21':  # 判断跳转的页面是否是指定页面,item截取字符串，在转换成列表
                assert_rslt = self.clickSkip(case_result[1:], para)
            elif assert_type == '22':
                assert_rslt = self.skip_windows_page(case_result[1:])
            elif assert_type == '23':
                assert_rslt = self.skip_tab_page(case_result[1:], para)
            elif assert_type == '24':
                assert_rslt = self.tab_skip_into_window(case_result[1:])
            elif assert_type == '25':  # 跳转到新的菜单页，但不携带值
                assert_rslt = self.skip_new_menu(case_result[1:])
            elif assert_type == '26':  # 单列数据有两个跳转
                assert_rslt = self.skip_two_link(case_result[1:], para)
            elif assert_type == '27':
                assert_rslt = self.skip_more_tab_link(case_result[1:], para)
            elif assert_type == '31':
                assert_rslt = self.assertInput(case_result[1:], case_id)
            dic ={assert_type: assert_rslt}

            ls_check_rslt[i] = dic

        result = True
        # 处理判断结果，具体那一步出错
        ls_check_rslt_values = ls_check_rslt.values()
        for item in ls_check_rslt_values:
            for key,value in item.items():
             if value == False:
                err_info = '用例编号:{},错误类型:{}'.format(case_id, esplain[key])
                logger.error(err_info)  # 出错具体原因
                print(err_info)
                result = value
                return result
        return result

    # 组合替换xpath
    # def combination_xpath(self, column_name, cloumn, line):
    #     # 定位目标xpath
    #     xpath = AssertResultLocators.DISPLAY_LINE.format(column_name, cloumn, line)
    #     return xpath

    def element_cnt(self, column_name):
        """
        判定显示区有多少数据
        :param column_name:
        :return:
        """
        xpath = self.tst_inst.format_xpath(AssertResultLocators.DISPLAY_ELEMENT, column_name)
        num = self.tst_inst._find_elements(xpath)
        return num

    # 获取文本框的内容
    def get_xpath(self, *agrs, type=1):

        """
        1.输入框
        2.显示区第几行第几列值

        """
        if type == 1:
            xpath = AssertResultLocators.INPUT_BASE_GU[1].format(agrs[0])
            return (By.XPATH, xpath)
        elif type == 2:
            xpath = AssertResultLocators.DISPLAY_LINE[1].format(agrs[0], agrs[1], agrs[2])
            return (By.XPATH, xpath)

    def clean_empty_blank(self, tag_text, tag_name='div'):
        """
        剔除标签中的空白字符及冒号：:
        :param tag_text: 标签中第一个连续中英文
        :param tag_name: 要剔除的tag
        """
        clean_obj = {'div': "//div[contains(text(),'{}')]".format(tag_text)}
        tn = clean_obj[tag_name]
        print(tn)
        script = AssertResultLocators.CLEAN_BLANK % tn
        print(script)
        self.tst_inst.exec_script(script)

    def compare_str(self, one_str, two_str):
        res = []
        for x, y in zip(one_str, two_str):
            if x == y:
                res.append(1)
            else:
                res.append(0)
        return False if 0 in res else True

    def get_text(self, locator, second=0):
        el = self.tst_inst._find_displayed_element(locator)
        return el.get_attribute('value')

    def assertInput(self, case_result, case_id):
        """
        获取单个
        :param case_result:
        :param case_id:
        :return:
        """
        xpath = AssertResultLocators.DISPLAY_RESULT[1].format(case_result[0], case_result[1])
        val = self.get_text((By.XPATH, xpath))
        if case_result[2] == val:
            logger.info('查询详细信息的输入框的值与期望结果一样')
            return True
        else:
            logger.error('查询详细信息的输入框的值与期望结果不一致')
            return False

    def tab_skip_into_window(self, para):
        """
        弹窗为非固定值,跳转
        :param para:
        :return:
        """

        line = self.checkBoxAssertLine_up(para[2])
        xpath = AssertResultLocators.DISPLAY_LINE[1].format(para[0], para[3], line)
        content = self.tst_inst.driver.find_element(*(By.XPATH, xpath)).text
        self.skip_to_page(para)
        tab_xpath = AssertResultLocators.WINDOWS_NAME_24[1].format(content)
        res = self.tst_inst.assert_context((By.XPATH, tab_xpath))
        self.tst_inst.sleep_time(2)
        con_xpath = tab_xpath + '/../div[1]'
        el = self.tst_inst.click((By.XPATH, con_xpath))

        return res

    def checkBoxAssertLine_up(self, value):
        l = self.tst_inst.calc_col_idx(value)
        try:
            res = self.tst_inst.assert_context((By.XPATH, AssertResultLocators.DISPLAY_BLANK[1]))
            if res == False:
                return l + 1
            else:
                return l
        except:
            pass

    def skip_new_menu(self, para):
        """
        跳转到新的菜单，但不需要校验值
        :param para:
        :return:
        """
        self.skip_to_page(para)
        xpath = AssertResultLocators.MENU_NAME[1].format(para[2])
        res = self.tst_inst.assert_context((By.XPATH, xpath))
        self.tst_inst.menuPage.closePage(page_name=para[2])
        return res

    def skip_two_link(self, para, caseData):
        """

        :param para:
        :return:
        """
        if para[4] == 'Y':
            change_value = para[1].split('-')
            case_id = caseData['TST_CASE_ID']
            # 获取要截取的值
            old_data = DataAccess.get_skip_data(case_id, para[1])
            old_page_list = []
            new_page_list = []
            for item in old_data:


                if item[10] == '1':
                    old_page_list.append(item[9])
                # 获取查询条件输入框的值
                elif item[4] == '01':
                    locator_qry = self.get_xpath(
                        DataAccess.get_xpath_tab_data(item[5], case_id, caseData['TAB_NAME'])[0][0])
                    old_page_list.append(self.tst_inst.get_text(locator_qry))
                else:
                    line = self.calc_col_idx(item[5])

                    locator = self.get_xpath(item[0], item[3], line, type=2)
                    old_page_list.append(self.tst_inst.driver.find_element(*locator).text)
            l = self.tst_inst.calc_col_idx(change_value[0], is_num=False)

            xpath = AssertResultLocators.DISPLAY_NUM[1].format(para[0], l)
            self.tst_inst.scrollTo((By.XPATH, xpath))
            print('------')
            line = self.checkBoxAssertLine_up(change_value[0]) + 1
            link_xpath = AssertResultLocators.DISPLAY_LINE[1].format(change_value[0], para[3], line)
            link_xpath_new = link_xpath + '//*[contains(text(),"{}")]'.format(change_value[1])
            self.tst_inst.click((By.XPATH, link_xpath_new))
            # 校验页面的名称是否正确
            name = self.assert_page_name(para[2])
            if name == False:
                print('跳转{}到页面失败'.format(para[2]))
            # 判断文字是否正确
            for item in old_data:
                if item[8] == None and item[4] == '04':
                    try:
                        resd = self.tst_inst.driver.find_element(
                            *AssertResultLocators.LINK_DATA).text
                        resd_new = resd[resd.index('/') + 1:len(resd)].strip()
                        new_page_list.append(resd_new)
                    except:
                        new_page_list.append('0')
                elif item[10] == '1':
                    new_page_list.append(item[9])
                else:
                    try:

                        ta = DataAccess.get_xpath_menu_data(item[8], para[2], item[6])
                        v_xpath = self.get_xpath(ta[0][0])
                        # self.tst_inst.commonWait(v_xpath)
                        self.tst_inst.sleep_time(1)
                        text = self.get_text(v_xpath, second=1)
                        new_page_list.append(text)
                    except:
                        logger.error('跳转的新页面时数据没有带过去')
                        return False
            print('old:', new_page_list)
            xpath = AssertResultLocators.DISPLAY_NUM[1].format(para[0], 1)
            self.tst_inst.scrollTo((By.XPATH, xpath))

            # 关闭其他菜单页
            self.tst_inst.menuPage.closePage(para[2])

            # 校验跳转传值是否正确
            Error_res = True
            line = self.tst_inst.calc_col_idx(para[1])
            info = '跳转坐标（{}行,{}列）element_sn:{}跳转前:xpath:{}、值：{}-----跳转后:xpath:{}、值：{}'
            for x, y, item in zip(old_page_list, new_page_list, old_data):
                info_rlt = info.format(para[3], line, item[11], item[5], x, item[8], y)
                if x == y:
                    logger.info(info_rlt)
                elif item[7] == '02':
                    if x in y:
                        logger.info(info_rlt)
                else:
                    err_info = '跳转传值错误:' + info_rlt
                    logger.error(err_info)
                    print('</br>' + err_info + '</br>')
                    Error_res = False
            return False if Error_res == False else True

    def skip_more_tab_link(self, case_result, caseData):
        """
                # tab页跳转sxs
                :param case_result: tst_case_result 校验数据
                :param caseData: 整个用例的数据
                :return:
                """
        case_id = caseData['TST_CASE_ID']
        change_value = case_result[1].split('-')
        # 获取要截取的值
        old_data = DataAccess.get_skip_data(case_id, case_result[1])
        old_page_list = []
        new_page_list = []
        for item in old_data:

            if item[10] == '1':
                old_page_list.append(item[9])
            # 获取查询条件输入框的值
            elif item[4] == '01':
                locator_qry = self.get_xpath(
                    DataAccess.get_xpath_tab_data(item[5], case_id, caseData['TAB_NAME'])[0][0])
                old_page_list.append(self.get_text(locator_qry))
            else:
                line = self.tst_inst.calc_col_idx(item[5])
                locator = self.get_xpath(item[0], item[3], line, type=2)
                old_page_list.append(self.tst_inst.driver.find_element(*locator).text)
        pageRes = ''
        # 跳转到对应的页面
        self.skip_to_page(case_result, iSchange=True)
        # 校验页面的名称是否正确
        name = self.assert_page_name(case_result[2])
        if name == False:
            print('跳转{}到页面失败'.format(case_result[2]))
        # 判断文字是否正确
        for item in old_data:
            if item[8] == None and item[4] == '04':
                try:
                    resd = self.driver.find_element(*AssertResultLocators.LINK_DATA).text
                    resd_new = resd[resd.index('/') + 1:len(resd)].strip()
                    new_page_list.append(resd_new)
                except:
                    new_page_list.append('0')
            elif item[10] == '1':
                new_page_list.append(item[9])

            else:
                try:
                    ta = DataAccess.get_xpath_menu_data(item[8], case_result[2], item[6])
                    v_xpath = self.get_xpath(ta[0][0])
                    self.tst_inst.sleep_time(1)
                    text = self.get_text(v_xpath, second=1)
                    new_page_list.append(text)
                except:
                    logger.error('获取新页面的值失败')
                    return False

                # 返回前一个tab页
                self.tst_inst.menuPage.closePage(case_result[2])
        # 跳转传值验证是否正确
        Error_res = True
        line = self.tst_inst.calc_col_idx(change_value[1])
        info = '跳转坐标（{}行,{}列）element_sn:{}跳转前:xpath:{}、值：{}-----跳转后:xpath:{}、值：{}'
        for x, y, item in zip(old_page_list, new_page_list, old_data):
            info_rlt = info.format(case_result[3], line, item[11], item[5], x, item[8], y)
            if x == y:
                logger.info(info_rlt)
            elif item[7] == '02':
                if x in y:
                    logger.info(info_rlt)
            else:
                err_info = '跳转传值错误:' + info_rlt
                logger.error(err_info)
                print('</br>' + err_info + '</br>')
                Error_res = False
        return False if Error_res == False else True


class AssertResultLocators:
    # 弹窗的关闭xpath
    WINDOWS_CLOSE = (By.XPATH,
                     '//*[text()="{}"]/../div[1]')
    WINDOWS_CLOSE_NEW = (
        By.XPATH, '//div[@class=" x-window x-resizable-pinned"]//span[@class="x-window-header-text" and text()="{}"]')

    # 弹窗页面的
    WINDOWS_PAGE = (By.XPATH, '//*[@class=\" x-window x-window-plain x-resizable-pinned\"]')

    # 弹窗标题
    WINDOWS_NAME = (By.XPATH,
                    '//span[text()="{}"]')
    WINDOWS_NAME_24 = (
        By.XPATH, '//div[@class=" x-window x-resizable-pinned"]//span[@class="x-window-header-text" and text()="{}"]')

    # 菜单页的名称
    MENU_NAME = (By.XPATH, "//span[@class=\"x-tab-strip-inner\"]/span[contains(text(),'{}')]")

    DISPLAY_ELEMENT = (
        By.XPATH, '// *[text() ="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]')
    DISPLAY_NUM = (By.XPATH,
                   '(//*[text()="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)[1]/td[{}]')

    # 显示区
    DISPLAY_LINE = (By.XPATH,
                    '(//*[text()="{0}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)[{1}]/td[{2}]')
    DISPLAY_LINE_NEW = (By.XPATH,
                        '// *[text() ="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]/ancestor::div[@class="x-grid3-viewport"]//*[@class="x-grid3-header"]//td//*[text()="{}"]')
    #显示区显示表头
    TABLE_HEAD = (By.XPATH, '//div[text()="{}"]/ancestor::div[@class="x-grid3-viewport"]//tr[@class="x-grid3-hd-row"]')
    # 空格
    DISPLAY_BLANK = (By.XPATH, '//div[@class="x-grid3-row-checker"]')

    # input输入框
    INPUT_BASE_GU = (By.XPATH, '//label[text()= "{}"]/../div[@class=\"x-form-element\"]//input')
    # 查询结果非显示区，是输入框(第一个值代表是哪个区域的，第二个值是代表那个输入框)
    DISPLAY_RESULT = (By.XPATH, '//span[text()="{}"]/../..//label[text()="{}"]/../..//input')

    # link 数据是否对应(显示区右下角查询的数据总量)
    LINK_DATA = (
        By.XPATH, '(//*[@id="UserDistStat_DetailGrid"]//tr[@class="x-toolbar-right-row"]//div[@class="xtb-text"])[1]')
    # 删除空格
    CLEAN_BLANK = r'''var elements,el,txt;
                        elements= document.evaluate("%s", document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
                        for (var i = 0; i < elements.snapshotLength; i++) {
                            el= elements.snapshotItem(i);
                            txt = el.innerText.replace(new RegExp(/[\s:：\-\(\)（）]/,'g'), '');
                            if (txt != el.innerText)
                                el.innerText = txt
                        }'''


if __name__ == '__main__':
    # skipMenuName = AssertResultLocators.MENU_NAME[1].format(
    #     'cdscsdc')
    # print(skipMenuName)
    pass
