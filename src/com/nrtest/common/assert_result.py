# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: assert_result.py
@time: 2019/1/15 0015 9:32
@desc:
"""
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.base_page import Page
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.global_drv import *
from com.nrtest.common.logger import Logger
from com.nrtest.common.utils import Utils

logger = Logger(logger='AssertResult').getlog()
from com.nrtest.sea.locators.other.menu_locators import MenuLocators
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class AssertResult(Page):
    def __init__(self, call_from):
        super().__init__(get_driver())
        self.case_para = call_from.case_para

    def click_link(self, column_name, line, colum_only_one='', only=1):
        """
        点击链接
        :param column_name:
        :param line:
        :param colum_only_one:
        :param only:
        """
        column = self.checkBoxAssertLine(column_name)
        num = self.element_cnt(column_name)
        if num > 0:
            if only == 1:
                col_name = column_name
            else:  # 2
                col_name = colum_only_one
            xpath = self.format_xpath(AssertResultLocators.DISPLAY_LINE, (col_name, column, line))
            self.click(xpath)

            # if only == 1 and num > 0:
            #     self.click(self.combination_xpath(column_name, column, line))
            # elif only == 2 and num > 0:
            #     self.click(self.combination_xpath(colum_only_one, column, line))

    def assert_page_name(self, page_name):
        """
        判断跳转的页面的名称是否正确
        :param page_name:
        :return:
        """
        xpath = self.format_xpath(AssertResultLocators.MENU_NAME, page_name)
        return self.assert_context(xpath)
        # skipMenuName = AssertResultLocators.MENU_NAME[1].format(page_name)
        # result = self.assert_context((By.XPATH, skipMenuName))
        # return result

    @BeautifulReport.add_popup_img(6)
    def skip_to_page(self, skipValue):
        """
        链接跳转:跳转到另一个页面
        :param skipValue:
        :return:
        """
        try:
            displayElement = '// *[text() ="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]'.format(
                skipValue[0])
            self.commonWait((By.XPATH, displayElement))
            display_num = len(self._find_elements((By.XPATH, displayElement)))
            if display_num > 0:
                if 1:
                    lineName = self.checkBoxAssertLine(skipValue[1])  # 判断是那一列
                    displayLine = '(//*[text()="{0}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)[{1}]/td[{2}]//a'.format(
                        skipValue[0], skipValue[3], lineName + 1)
                    try:
                        # 点击要跳转的链接
                        self.click((By.XPATH, displayLine))
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
            self.closePages(page_name=menuPage, isCurPage=False)
        elif page == 2:
            # 切换到另一个tab页
            self.clickTabPage(tab)
        elif page == 3:
            self.click(AssertResultLocators.WINDOWS_CLOSE)

    def skip_tab_page(self, para, caseId='', caseData=''):
        """
        # tab页跳转sxs
        :param para: tst_case_result 校验数据
        :param caseId:  用例编号
        :param caseData: 整个用例的数据
        :return:
        """
        if para[len(para) - 1] == 'Y':
            self.clean_empty_blank(para[1])
        # 获取要截取的值
        old_data = DataAccess.get_skip_data(caseId, para[1])
        old_page_list = []
        new_page_list = []
        for item in old_data:
            line = self.checkBoxAssertLine(item[5]) + 1
            locator = self.get_xpath(item[0], item[3], line, type=2)
            if item[10] == '1':
                old_page_list.append(item[9])
            # 获取查询条件输入框的值
            elif item[4] == '01':
                locator_qry = self.get_xpath(DataAccess.get_xpath_tab_data(item[5], caseId, caseData['TAB_NAME'])[0][0])
                old_page_list.append(self.get_text(locator_qry))
            else:
                old_page_list.append(self.driver.find_element(*locator).text)
        pageRes = ''
        # 跳转到对应的页面
        self.skip_to_page(para)
        # 校验页面的名称是否正确
        name = self.assert_page_name(para[2])
        if name == False:
            print('跳转{}到页面失败'.format(para[2]))
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
                    ta = DataAccess.get_xpath_tab_data(item[8], caseId, para[2])
                    text = self.get_text(self.get_xpath(ta[0][0]), second=1)
                    new_page_list.append(text)
                except:
                    logger.error('跳转的新页面时数据没有带过去')
                    return False

        # 返回前一个tab页
        self.clickTabPage(caseData['TAB_NAME'])
        # 跳转传值验证是否正确
        res = False
        l = 0
        line = self.checkBoxAssertLine(para[1])
        for x, y, item in zip(old_page_list, new_page_list, old_data):
            if x == y:
                logger.info(
                    '跳转坐标（{row}行,{col}列）element_sn:{sn}跳转前:xpath:{xpath_old}、值：{xpath_old_value}-----跳转后:xpath:{xpath_new}、值：{xpath_new_value}'.format(
                        row=para[3], col=line + 1, sn=item[11], xpath_old=item[5],
                        xpath_old_value=x, xpath_new=item[8], xpath_new_value=y))
                res = True
            else:
                logger.error(
                    '跳转坐标（{row}行，{col}列）,跳转传值错误error:element_sn:{sn}跳转前:xpath:{xpath_old}、值：{xpath_old_value}-----跳转后:xpath:{xpath_new}、值：{xpath_new_value}'.format(
                        row=para[3], col=line + 1, sn=item[11], xpath_old=item[5],
                        xpath_old_value=x, xpath_new=item[8], xpath_new_value=y))
                l += 1
        # if l > 0:
        #     res = False
        # return res
        return not bool(l)

    def assert_expect_value(self, locator, value):
        """
        校验期望值是否正确
        :param locator:
        :param value:
        :return:
        """
        res = self.driver.find_element(*locator).text
        res2 = Utils.replace_chrs(res)
        return value in res2

    def skip_windows_page(self, para):
        """
        窗口跳转
        :param para: 以，为分隔符，第一位是显示区唯一列明，第二位是要校验值的列明，第三位是校验值
        :return:
        """
        try:
            self.skip_to_page(para)
            xpath = AssertResultLocators.WINDOWS_NAME[1].format(para[2])
            self.commonWait((By.XPATH, xpath))
            is_skiped = True
        except:
            is_skiped = False
        finally:
            self.click(AssertResultLocators.WINDOWS_CLOSE)

        return is_skiped

    def assertValue(self, assertValues):
        """
        assertValues ='手机,外包队伍名称,test'
        :param assert_values:以，为分隔符，第一位是显示区唯一列明，第二位是要校验值的列明，第三位是校验值
        :return:
        """
        print('-------------------')
        try:
            # 显示区是否有值
            xpath_table = '// *[text() ="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]'.format(
                assertValues[0])
            self.commonWait((By.XPATH, xpath_table))
            # 显示区查询出多少结果数量
            displayNum = len(self._find_elements((By.XPATH, xpath_table)))
            try:
                xpath_checker = '//*[@class="x-grid3-row-checker"]'
                displayCheck = self.assert_context((By.XPATH, xpath_checker))
            except:
                print('没有弹出确定按钮')
            diplayName = self.checkBoxAssertLine(assertValues[1])  # 判断具体是哪一行
            ringhtNum = 0
            displayLineElement = '(//*[text()="{0}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)[{1}]/td[{2}]//*[contains(text(),"{3}")]'
            if displayNum > 0:
                if displayCheck:
                    for i in range(1, displayNum + 1):
                        # 显示区结果的每一行对应列的数据的xpath
                        displayLineElement_index = displayLineElement.format(assertValues[0], i, diplayName + 1,
                                                                             assertValues[2])
                        try:
                            assert_rslt = self.assert_context((By.XPATH, displayLineElement_index))
                            if assert_rslt:
                                ringhtNum += 1
                            else:
                                print('第{0}行，{1}列显示的值与{2}不一致'.format(i, assertValues[1], assertValues[2]))
                                break
                        except:
                            print('校验失败')
                    return ringhtNum == displayNum

                # elif not displayCheck:  # 非带有复选框显示区
                else:
                    for i in range(1, displayNum + 1):
                        # 显示区结果的每一行对应列的数据的xpath
                        displayLineElement_index = displayLineElement.format(assertValues[0], i, diplayName + 1,
                                                                             assertValues[2])
                        try:
                            assert_rslt = self.assert_context((By.XPATH, displayLineElement_index))
                            if assert_rslt:
                                ringhtNum += 1
                            else:
                                print('第{0}行，{1}列显示的值与{2}不一致'.format(i, assertValues[1], assertValues[2]))
                                break
                        except:
                            print('校验失败')

                    return ringhtNum == displayNum
        except:
            print('显示区结果值校验失败')

    def clickSkip(self, assertValues, caseId='', caseData='', model=1, version=1):

        """

        :param assertValues: tst_case_result 验证数据
        :param caseId: 用例id
        :param caseData: 用例所有数据
        :param model: 老版本校验期望值
        :param version: 1为老版本，2为新版本
        :return:
        """
        try:
            displayElement = '// *[text() ="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]'.format(
                assertValues[0])
            self.commonWait((By.XPATH, displayElement))
            display_num = len(self._find_elements((By.XPATH, displayElement)))
            if display_num > 0:
                # try:
                #     sel = '//*[@class="x-grid3-row-checker"]'
                #
                #     displayCheckbox = self.assert_context((By.XPATH, sel))  # 判断显示区是有复选框的还是没有复选框的
                #     print('显示区有复选框')
                # except:
                #     print('显示区没有复选框')
                if 1:
                    lineName = self.checkBoxAssertLine(assertValues[1])  # 判断是那一列
                    displayLine = '(//*[text()="{0}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)[{1}]/td[{2}]'.format(
                        assertValues[0], 1, lineName + 1)
                    try:

                        try:
                            if version == 1:
                                self.click((By.XPATH, displayLine))
                                # 把弹出的确定框点掉

                                self.btn_confirm()
                                skipMenuName = "//span[@class=\"x-tab-strip-inner\"]/span[contains(text(),'{}')]".format(
                                    assertValues[2])
                                result = self.assert_context((By.XPATH, skipMenuName))  # 判断跳转菜单页是否存在
                                if model == 2:
                                    # 校验期望值是否正确
                                    value = self.assert_expect_value(AssertResultLocators.TAB_PAGE_TEXT,
                                                                     assertValues[3])

                                self.menuPage.closePages(page_name=assertValues[2], isCurPage=False)  # 关闭跳转菜单页
                                if model == 1:
                                    return result
                                elif model == 2:
                                    return True if result and value else False
                            elif version == 2:
                                # 获取要截取的值
                                old_data = DataAccess.get_skip_data(caseId, assertValues[1])
                                old_page_list = []
                                new_page_list = []
                                for item in old_data:
                                    line = self.checkBoxAssertLine(item[5]) + 1
                                    locator = self.get_xpath(item[0], item[3], line, type=2)
                                    if item[10] == '1':
                                        old_page_list.append(item[9])
                                    # 获取查询条件输入框的值
                                    elif item[4] == '01':
                                        locator_qry = self.get_xpath(
                                            DataAccess.get_xpath_tab_data(item[5], caseId, caseData['TAB_NAME'])[0][0])
                                        old_page_list.append(self.get_text(locator_qry))
                                    else:
                                        old_page_list.append(self.driver.find_element(*locator).text)
                                pageRes = ''
                                # 跳转到对应的页面
                                self.skip_to_page(assertValues)
                                # 校验页面的名称是否正确
                                name = self.assert_page_name(assertValues[2])
                                if name == False:
                                    print('跳转{}到页面失败'.format(assertValues[2]))
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

                                            ta = DataAccess.get_xpath_menu_data(item[8], assertValues[2])
                                            text = self.get_text(self.get_xpath(ta[0][0]), second=1)
                                            new_page_list.append(text)
                                        except:
                                            logger.error('跳转的新页面时数据没有带过去')
                                            return False

                                print('old:', new_page_list)
                                # 关闭其他菜单页
                                self._closePages(page_name=assertValues[2], isCurPage=False)
                                # 校验跳转传值是否正确
                                res = False
                                l = 0
                                for x, y, item in zip(old_page_list, new_page_list, old_data):
                                    if x == y:
                                        logger.info(
                                            '跳转坐标（{row}行,{col列}），element_sn:{sn}跳转前:xpath:{xpath_old}、值：{xpath_old_value}-----跳转后:xpath:{xpath_new}、值：{xpath_new_value}'.format(
                                                row=assertValues[3], col=self.checkBoxAssertLine(assertValues[1]) + 1,
                                                sn=item[11], xpath_old=item[5], xpath_old_value=x, xpath_new=item[8],
                                                xpath_new_value=y))
                                        res = True
                                    else:
                                        logger.error(
                                            '跳转坐标（{row}行,{col列}）跳转传值错误error:element_sn:{sn}跳转前:xpath:{xpath_old}、值：{xpath_old_value}-----跳转后:xpath:{xpath_new}、值：{xpath_new_value}'.format(
                                                row=assertValues[3], col=self.checkBoxAssertLine(assertValues[1]) + 1,
                                                sn=item[11], xpath_old=item[5], xpath_old_value=x, xpath_new=item[8],
                                                xpath_new_value=y))
                                        l += 1
                                if l > 0:
                                    res = False
                                return res





                        except BaseException:
                            pass
                    except:
                        print('跳转验证失败')

        except:
            print('验证失败')

    def check_query_result(self, para, version=2):
        """

        :param para: 用例数据
        :param version: 1为老版本，2为新版本
        :return: 返回校验结果
        """
        esplain = {'11': '显示区未查询出结果', '12': '按条件查询出的结果与期望值不一致', '21': '跳转菜单页面不正确', '22': '跳转弹窗不正确', '23': '跳转tab页不正确'}
        rslt = DataAccess.get_case_result(para['TST_CASE_ID'])
        display_tab = '// *[text() =\'{}\']/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]'  # 根据XPATH判断显示区是否有值
        ls_check_rslt = {}
        for row in rslt:  # 根据rslt有几个值来判断要做几次校验
            assert_type = row[0]
            if assert_type == '11':
                assert_rslt = self.assert_context((By.XPATH, display_tab.format(row[1])))  # 判断是否有值
            elif assert_type == '12':
                assert_rslt = self.assertValue(row[1:])  # 判断值是否准确,item截取字符串，在转换成列表
            elif assert_type == '21':
                assert_rslt = self.clickSkip(row[1:], caseId=para['TST_CASE_ID'], caseData=para,
                                             version=version)  # 判断跳转的页面是否是指定页面,item截取字符串，在转换成列表
            elif assert_type == '22':
                assert_rslt = self.skip_windows_page(row[1:])
            elif assert_type == '23':
                assert_rslt = self.skip_tab_page(row[1:], caseId=para['TST_CASE_ID'], caseData=para)

            ls_check_rslt.update({assert_type: assert_rslt})

        result = True
        # 处理判断结果，具体那一步出错
        for item in ls_check_rslt.items():
            if item[1] == False:
                logger.error(
                    '用例编号:{case_id},错误类型:{type}'.format(case_id=para['TST_CASE_ID'], type=esplain[item[0]]))  # 出错具体原因

                print('用例编号:{case_id},错误类型:{type}'.format(case_id=para['TST_CASE_ID'], type=esplain[item[0]]))
                result = item[1]
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
        xpath = self.format_xpath(AssertResultLocators.DISPLAY_ELEMENT, column_name)
        num = self._find_elements(xpath)
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
        self.exec_script(script)

    def compare_str(self, one_str, two_str):
        res = []
        for x, y in zip(one_str, two_str):
            if x == y:
                res.append(1)
            else:
                res.append(0)
        return False if 0 in res else True

    def get_text(self, locator, second=0):
        el = self._find_displayed_element(locator)
        return el.get_attribute('value')

    def _closePages(self, page_name='工作台', isCurPage=True):
        """
        通过工作台或定位菜单页面，关闭当前页面或除当前页面外其他页面
        :param page_name: 当“工作台”时相当于清屏操作：即关闭所有窗口
        :param isCurPage:True-关闭其他所有页；False-关闭当前页
        """

        # ****定位到要右击的元素**
        loc = self.format_xpath(MenuLocators.CURRENT_MENU, page_name)

        right_click = self.driver.find_element(*loc)
        # 鼠标右键操作
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc))
        sleep(2)
        ActionChains(self.driver).context_click(right_click).perform()

        # 待定位右键菜单
        forMenu = '关闭其他所有页' if isCurPage or page_name == '工作台' else '关闭当前页'
        loc = self.format_xpath(MenuLocators.CLOSE_PAGES, forMenu)
        pe = self.format_xpath(MenuLocators.CLOSE_PAGES_SPE, forMenu)

        try:
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(loc))
        except:
            loc = pe
            print(loc)
        self.driver.find_element(*loc).click()


class AssertResultLocators:
    # 弹窗的关闭xpath
    WINDOWS_CLOSE = (By.XPATH,
                     '//*[@class=\" x-window x-window-plain x-resizable-pinned\"]/div[@class=\"x-window-tl\"]//div[@class=\"x-tool x-tool-close\"]')

    # 弹窗页面的
    WINDOWS_PAGE = (By.XPATH, '//*[@class=\" x-window x-window-plain x-resizable-pinned\"]')

    # 弹窗标题
    WINDOWS_NAME = (By.XPATH,
                    '//div[@class=\" x-window x-window-plain x-resizable-pinned\"]//div[@class=\"x-window-header x-unselectable x-window-draggable\"]//*[text()="{}"]')

    # tab页面获取所有文字
    TAB_PAGE_TEXT = (By.XPATH, '//*[@id="maintab"]')

    # 菜单页的名称
    MENU_NAME = (By.XPATH, "//span[@class=\"x-tab-strip-inner\"]/span[contains(text(),'{}')]")

    DISPLAY_ELEMENT = (
        By.XPATH, '// *[text() ="{}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]')

    # 显示区
    DISPLAY_LINE = (By.XPATH,
                    '(//*[text()="{0}"]/ancestor::div[@class="x-grid3-viewport"]//table[@class="x-grid3-row-table"]//tr)[{1}]/td[{2}]')

    # input输入框
    INPUT_BASE_GU = (By.XPATH, '//label[text()= "{}"]/../div[@class=\"x-form-element\"]//input')

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
