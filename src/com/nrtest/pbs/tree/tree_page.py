# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: tree_page.py
@time: 2019-01-09 9:31
@desc:
"""
import re
from time import sleep

from selenium.webdriver import ActionChains

from com.nrtest.common.BeautifulReport import BeautifulReport
from com.nrtest.common.base_page import Page
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.dictionary import Dict
from com.nrtest.common.logger import Logger
from com.nrtest.pbs.tree.tree_locators import TreePBSLocators, TreeLocators, TreeSingleUserLocators, LeftTreeLocators

# create a logger instance
logger = Logger(logger='BaseTreePage').getlog()
class BaseTreePage(Page):
    def __init__(self, parent_class, menu_page=None):
        """

        :param driver:
        :param menu_page:
        :param tree_type:
                20-含电压等级厂站树 11-并且带复选框
                30-厂站档案设备树   21-并且带复选框
                40-普通树         41-并且带复选框；采集运维-->手动对时
        """
        if bool(menu_page):  # 通过testCase子类基础初始化：com/nrtest/sea/testcase/demo_new/pbs5000.py
            driver = parent_class
            super().__init__(self, driver, menu_page)
        else:  # 通过实例化BaseTreePage子类对象初始化：test_consIntrgratedQuery_realTimeDataQry.py
            menu_page = parent_class.menuPage
            driver = parent_class.driver
            super().__init__(driver, menu_page)

        if bool(menu_page):
            self.tree_type = menu_page.tree_type
        else:
            self.tree_type = '20'

    def openLeftTree(self, node_no, op_mode=True):
        """
        打开左边树
        :param node_no:
        """
        try:
            node = Dict(eval(node_no))
            node_vale = node['NODE_VALE']
        except:
            # 不是数组时的默认处理
            node = {'NODE_FLAG': '01', 'NODE_VALUE': node_no}
            node_vale = node_no

        node['NODE_VALE'] = DataAccess.getTreeNode(node_vale).split(';')

        self._click_node_tab(node['NODE_FLAG'])
        self.node_list = []  # 用于左边树整体收起压栈
        # self.tree_node = node # 整体压栈时，gai
        self._operate_left_tree(node)

    def _click_node_tab(self, node_tab_idx):
        """
        左边树操作前的预处理，如选择左边树类型
        :param node_tab_idx:
        """
        pass

    def closeLeftTree(self):
        # node = deepcopy(self.tree_node)
        # node['NODE_VALE'].reverse()
        # self._operate_left_tree(node, False)
        if self.tree_type[-1] == 0:  # 非复选框节点，最后一个叶子节点不处理
            self.node_list.pop()

        self.node_list.reverse()
        for node in self.node_list:
                node.click()
    def closeLeftTree_double(self):
        loc = LeftTreeLocators.CLOSE_LFET_TREE
        loc_root = LeftTreeLocators.CLOSE_LFET_ROOT_TREE
        els = self._find_elements(loc)
        l = len(els)-1
        while l>=0:
            els[l].click()
            l -=1
        el = self._direct_find_element(loc_root)
        if el:
            el.click()

    def _operate_left_tree(self, node_info):
        """
        根据左边树节点信息，打开或收起节点信息
        :param node_info: 左边树节点信息
        :return:
        """
        node_flag = node_info['NODE_FLAG']
        if node_flag == '01':  # 选择全模型
            items = node_info['NODE_VALE']
            levels = len(items) - 1  # 总层级数-1
            for idx, item in enumerate(items):
                # 厂站间有重复节点名，如电压等级、厂站设备等
                locator = self._find_in_parent(item, idx, items)
                if self.tree_type[-1] == '1':  # 带复选框的左边树
                    els = self._find_elements(locator)
                    if bool(els):
                        self._node_click(els[0], idx, levels)
                        if idx == levels:
                            self._node_click(els[1], idx, levels, True)
                else:
                    # if idx == levels:  # 叶子节点只点击文本元素，不点击文本元素边上的图标元素
                    #     locator = (locator[0], locator[1].replace('/../span', ''))  # 该替换操作只对PBS5000有效
                    # el = self._find_element(locator)
                    el = self._find_displayed_element(locator)
                    if bool(el):
                        self._node_click(el, idx, levels)
        else:  # 选择其他节点
            self._other_left_tree(node_info)

    def _other_left_tree(self, node_info):
        pass

    def _find_in_parent(self, item, idx, items):
        pass

    def _node_click(self, element, curr_idx, node_levels, is_chk_node=False):
        """

        :param element:
        :param curr_idx:当前节点序号：0 开始
        :param node_levels:当前节点层级数：n -1
        :param is_chk_node: True-既有节点，同时带复选框；False-只有节点，没复选框
        """
        pass



    def into_iframe(self):
        self.intoIframe(LeftTreeLocators.ID)

    def main_page(self):
        self.driver.find_element(*LeftTreeLocators.MAIN_PAGE).click()

    def inputDate(self, value, is_multi_tab=False, new_idx=0, is_line=False):
        """
        新版日期输入框操作：没标签、没定义name或id时对可见日期选择框进行定位
        :param value:要输入的值:自定义标签名;第n个日期选择框;日期值【该值不填默认为1】：开始日期;1;2018-12-24
        :param is_multi_tab:菜单面内是否有多个TAB页
        :param new_idx:配置的idx因页面查询条件有变化时，替换为当前参数值
        """
        try:
            ls_values = value.split(';')
            # print(ls_values)
            if is_line:
                loc = self.format_xpath(self.baseLocators.QRY_LINE_LOCATORS, ls_values[0])
            else:
                loc = self.format_xpath(self.baseLocators.QRY_LOCATORS, ls_values[0])
            tmp = ls_values[1].strip()
            idx = new_idx
            if new_idx == 0:
                idx = 1 if len(tmp) == 0 else int(tmp)
            if idx <= 0:
                raise Exception('日期选择框调整顺序【{}】不对，请确认'.format(idx))

            el = self._find_displayed_element(loc, idx)
            self.driver.execute_script("arguments[0].value=arguments[1]", el, ls_values[2])
            # el.clear()
            # el.send_keys(ls_values[2])
            logger.info('日期选择框填写:{}'.format(value))
        except Exception as ex:
            logger.error('输入错误:{}\n{}'.format(value, ex))

    def curr_input(self, values,is_multi_elements=False,idx=1):
        """
        新版输入查询条件操作
        :param values:要输入的值
        :param is_multi_tab:菜单面内是否有多个TAB页
        :param is_multi_elements:菜单面内是否有多个重复元素
        """
        try:
            ls_values = values.split(';')
            loc = self.format_xpath(self.baseLocators.QRY_LOCATORS, ls_values[0])
            if is_multi_elements:
                el = self._find_displayed_element(loc,idx=idx)
            else:
                el = self._find_element(loc)
            el.clear()
            el.send_keys(ls_values[1])
            logger.info('list index out of range文本框输入:{}'.format(values))
        except AttributeError as ex:
            logger.error('输入错误:{}\n{}'.format(values, ex))

    def input(self, values, *locators):
        """
        方法名：input
        功能：文本框输入内容

        :param values: 文本框要输入的内容
        :param locators: 元素的位置
        :return: None
        """
        try:
            if values.find(';') > -1:
                self.curr_input(values)
            else:
                element = self._find_element(locators)
                # 输入前清空文本框
                element.clear()
                element.send_keys(values)
                logger.info('文本框输入:%s', values)
        except AttributeError as e:
            logger.error('输入错误:%s', values)

    def curr_click(self, is_multi_eles=False, btn_name='', idx=1):
        """
        新版点击方法
        :param is_multi_tab:菜单面内是否有多个TAB页
        :param btn_name:按钮元素文本值
        :param idx:第idx个可见按钮
        """
        try:
            btn_name = btn_name if bool(btn_name) else '查询'
            loc = self.format_xpath(self.baseLocators.QRY_BUTTON, btn_name)
            if is_multi_eles:
                el = self._find_displayed_element(loc, idx)
            else:
                el = self._find_element(loc)
            el.click()

            logger.info('点击元素：{}'.format(loc))
        except BaseException as e:
            logger.error('点击元素失败:{}\n{}'.format(loc, e))

    def selectDropDown(self, option, sleep_sec=0, is_multi_elements=False, is_equalText=False, is_line=False, idx=1):
        """
        下拉单选框选择
        :param option: 参数格式：查询条件标签名;查询条件
        :param is_multi_tab: 多Tab页时，如果查询条件有重复，则该值填True
        :param sleep_sec:休眠n秒
        :param is_multi_elements:是否存在重复元素
        :param is_equalText: True-下拉选择值需完全匹配，Fase-部分匹配
        :param byImg: 存在点下拉框下拉图标时，不能弹出下拉选择的问题，True-下拉框下拉图标，False-下拉框的INPUT
        """
        if (option.find(';') == -1):
            print('............请配置查询条件的标签值............')
        else:
            ls_option = option.split(';')
            if len(ls_option) == 2:
                item = ls_option[1]
            else:
                item = ls_option[2] if len(ls_option[2]) > 0 else ls_option[1]
            if bool(item):
                # 打开下拉框
                if is_line:
                    xpath = self.format_xpath(self.baseLocators.QRY_LINE_SELECT_DROP_DOWD, ls_option[0])
                else:
                    xpath = self.format_xpath(self.baseLocators.QRY_SELECT_DROP_DOWN, ls_option[0])

                if is_multi_elements:
                    el = self._find_displayed_element(xpath,idx=idx)
                    el.click()
                else:
                    self.click(xpath)

                if bool(sleep_sec):
                    sleep(sleep_sec)

                # 根据名称选择下拉框
                if is_equalText:
                    loc = self.format_xpath(self.baseLocators.QRY_SELECT_DROP_DOWN_ELE, item)
                else:
                    loc = self.format_xpath(self.baseLocators.QRY_SELECT_DROP_DOWN_ELE, item)
                self.click(loc)
            else:  # 选择值为空时，表示选择全部
                xpath = self.format_xpath(self.baseLocators.SEL_CHECKBOX_CLEAN, ls_option[0])
                el = self._find_displayed_element(xpath)
                self.driver.execute_script("arguments[0].value=arguments[1]", el, '')

    @BeautifulReport.add_popup_img()
    def btn_query(self, is_multi_tab=False, btn_name='', idx=1):
        """
        通用页面查询按钮
        :param is_multi_tab: 多Tab页时，如果查询按钮名有重复，则该值填True
        :param btn_name:按钮元素文本值
        :param idx:第idx个可见按钮
        """
        self.curr_click(is_multi_tab, btn_name=btn_name, idx=idx)
    def clickCheckBox(self, items,name=False,number=False):
        """
        选择多个复选框
        :param items: “xpath的说明;确定一组复选框的class;复选框的值比如：'1,2'”
        :param name: 以名称来确定复选框'选中,未选中'
        :param number: 以编号来确定复选框'1，2'
        :return:
        """
        try:
            if len(items.split(';')) > 2:
                is_group_check_box = items.split(';')[1]
            else:
                is_group_check_box = ''
            loc1 = (self.baseLocators.UNCHECK_BOX[0],
                     "//*[@class = " + '"' + is_group_check_box + '"' + "]" + self.baseLocators.UNCHECK_BOX[1])

            # 撤销已选项
            elements = self._find_elements(loc1)
            for el in elements:
                 if el.is_selected():
                        el.click()
            if items.find(';') >= 0:

                ls_items = (items.split(';')[2]).split(',')

            else:
                ls_items = items.split(',')
            if name:

                if ls_items[0] != '':
                    for item in ls_items:


                        if is_group_check_box != '':
                            name_xpath = (self.baseLocators.CHECK_BOX[0],"//*[@class = "+ '"'+is_group_check_box+'"'+"]" +self.baseLocators.CHECK_BOX[1])
                            loc = self.format_xpath(name_xpath, item)
                        else:
                            loc = self.format_xpath(self.baseLocators.CHECK_BOX, item)
                        self.click(loc)
            if number:
                if ls_items[0] != '':
                    for item in ls_items:

                        if is_group_check_box != '':
                            number_xpath = (self.baseLocators.UNCHECK_BOX[0],
                                     "(//*[@class = " + '"' + is_group_check_box + '"' + "]" + self.baseLocators.UNCHECK_BOX[
                                         1]+")[{}]")
                            loc = self.format_xpath(number_xpath, item)
                        else:
                            loc = self.format_xpath(self.baseLocators.CHECK_BOX, item)
                        self.click(loc)

        except BaseException as ex:
            print('点击复选框失败：{}'.format(ex))

    def clickRadioBox(self, option, is_multi_elements=False, name=False, number=False):
        """
        选择单选框
        :param option:
        :param is_multi_elements: 当有多个元素时，找到当前页面显示的
        :param is_group_elements: 当页面有不同的分组的单选框，通过在数据库配置class来进行分组
        :return:
        """
        try:
            if (option.find(';') == -1):
                item = option
            else:
                ls_option = option.split(';')
                item = ls_option[2] if len(ls_option[2]) > 0 else ls_option[1]

            if len(item) == 0:
                raise BaseException('单选框必须指定选择项：{}'.format(option))
            if name:
                    group_xpath = (self.baseLocators.CHECK_BOX[0],
                                   "//*[@class = " + '"' + ls_option[1] + '"' + "]" +
                                   self.baseLocators.RADIOBOX_INPUT2LABEL[
                                      1])
                    lis_item = item.split(',')
                    for it in lis_item:
                        xpath = self.format_xpath(group_xpath, item)
                        if is_multi_elements:
                            el = self._find_displayed_element(xpath)
                            el.click()
                        else:
                            self.click(xpath)
            elif number:
                group_xpath = (self.baseLocators.CHECK_BOX[0],
                               "//*[@class = " + '"' + ls_option[1] + '"' + "]" +
                               self.baseLocators.RADIOBOX_INPUT2LABEL_NUM[
                                   1])
                lis_item = item.split(',')
                for it in lis_item:
                    xpath = self.format_xpath(group_xpath, it)
                    if is_multi_elements:
                        el = self._find_displayed_element(xpath)
                        el.click()
                    else:
                        self.click(xpath)

            else:
             xpath = self.format_xpath(self.baseLocators.RADIOBOX_LABEL2INPUT, item)
             if is_multi_elements:
                 el = self._find_displayed_element(xpath)
                 el.click()
             else:
                 self.click(xpath)



        except BaseException as ex:
            print('点击单选框失败：{}'.format(ex))

    def click_button(self,value,is_multi_eles=False,idx=1):

       try:
           ls_option = value.split(';')
           loc = self.format_xpath(self.baseLocators.QRY_BUTTON, ls_option[1])
           if is_multi_eles:
               el = self._find_displayed_element(loc, idx)
           else:
               el = self._find_element(loc)
           el.click()

           logger.info('点击元素：{}'.format(loc))
       except BaseException as e:
           logger.error('点击元素失败:{}\n{}'.format(loc, e))
    def click_xpath(self,value,is_multi_eles=False,idx=1):
        """
        页面按钮是图片需要在处理xpath，在数据库配置xpath，来实现操作
        :param value: 配置的值'查询按钮;//*[@id='search_btn']'
        :param is_multi_eles:当有多个是，传入True来确定唯一值
        :param idx:来确认是第几个，默认是第一个
        :return:
        """
        try:
            ls_option = value.split(';')
            # loc = self.format_xpath(self.baseLocators.QRY_BUTTON, ls_option[1])
            loc = (self.baseLocators.QRY_BUTTON[0],ls_option[1])
            if is_multi_eles:
                el = self._find_displayed_element(loc, idx)
            else:
                el = self._find_element(loc)
            el.click()

            logger.info('点击元素：{}'.format(loc))
        except BaseException as e:
            logger.error('点击元素失败:{}\n{}'.format(loc, e))






class TreePBSPage(BaseTreePage):
    def _click_node_tab(self, node_tab_idx):
        if self.tree_type[0] != '4':
            node_tab = {'01': '全模型', '02': '搜索', '03': '收藏夹'}
            loc = self.format_xpath(TreePBSLocators.NODE_TAB, node_tab[node_tab_idx])
            self.click(loc)

    def _find_in_parent(self, item, idx, items):
        """
        在父节点范围内查找
        :param item:
        :return:
        """
        # 20-含电压等级厂站树； 11-并且带复选框
        # 30-厂站档案设备树；   31-并且带复选框
        # 40-普通树；         41-并且带复选框；采集运维-->手动对时
        is_step_into = False
        if self.tree_type[0] == '2':  # 20-含电压等级的厂站树
            is_step_into = bool(re.search(r'^\d{1,4}.[kK][vV]$', item))
        elif self.tree_type[0] == '3':  # 30-厂站档案设备
            is_step_into = item in ['线端', '刀闸', '发电机组', '电容器', '负荷', '开关']

        levels = len(items) - 1  # 总层级数-1
        if is_step_into:
            locator = self.format_xpath(TreePBSLocators.NODE_LEVEL_IN_PARENT, (idx - 1, items[idx - 1], idx, item))
        else:
            locator = self.format_xpath(TreePBSLocators.NODE_LEVEL, (idx, item))
            # 不带复选框的叶子节点只点击文本元素，不点击文本元素边上的图标元素
            if idx == levels and self.tree_type[1] == '0':
                # locator = (locator[0], locator[1].replace('/../span', ''))
                locator = self.format_xpath(TreePBSLocators.LEEF_NODE, (idx, item))

        return locator

    def _node_click(self, element, curr_idx, node_levels, is_chk_node=False):
        """

        :param element:
        :param curr_idx:当前节点序号：0 开始
        :param node_levels:当前节点层级数：n -1
        :param is_chk_node: True-既有节点，同时带复选框；False-只有节点，没复选框
        """
        self.node_list.append(element)
        attrs = element.get_attribute('class').strip()
        if is_chk_node:
            # 目前仅对pbs5000有效:判断当前节点是选中，不选中
            # 带复选框的左边树：不选中：class="button chk checkbox_false_full"  选中：class="button chk checkbox_false_part"
            is_click = attrs.endswith('full') or curr_idx == node_levels
        else:
            # 目前仅对pbs5000有效:判断当前节点是打开还是关闭
            is_click = attrs.endswith('close') or curr_idx == node_levels

        # 状态不一致时点击
        if is_click:
            element.click()
            sleep(0.3)


class TreePage(BaseTreePage):
    def _click_node_tab(self, node_tab_idx):
        if self.tree_type[0] != '4':
            node_tab = {'01': '供电区域', '02': '用户', '03': '终端', '04': '行业', '05': '电网结构', '06': '群组', '07': '单户综合','08':'全模型'}
            loc = self.format_xpath(TreeLocators.NODE_TAB, node_tab[node_tab_idx])
            self.click(loc)

    def _find_in_parent(self, item, idx, items):
        """
        在父节点范围内查找
        :param item:
        :param idx:
        :param items:
        :return:
        """
        # 20-供电区域； 11-并且带复选框
        # 30-行业；    31-并且带复选框
        # 40-普通树；   41-并且带复选框；
        # 50-群组
        is_step_into = False
        if self.tree_type[0] == '2':
            is_step_into = item == '直属用户'

        levels = len(items) - 1  # 总层级数-1
        if is_step_into:
            locator = self.format_xpath(TreeLocators.NODE_LEVEL_IN_PARENT, (items[idx - 1], item))
            # *********带复选框的叶子节点，除勾选外，是否还需再点击一下
        else:
            locator = self.format_xpath(TreeLocators.NODE_LEVEL, (item))
            # 不带复选框的叶子节点只点击文本元素，不点击文本元素边上的图标元素
            if idx == levels and self.tree_type[1] == '0':
                locator = self.format_xpath(TreeLocators.LEEF_NODE, item)

        # 对群组类型元素定位做特殊处理
        if self.tree_type == '50':
            locator = (locator[0], locator[1].replace(TreeLocators.TREE_DIV, self.group_node[1]))

        return locator

    def _node_click(self, element, curr_idx, node_levels, is_chk_node=False):
        """

        :param element:
        :param curr_idx:当前节点序号：0 开始
        :param node_levels:当前节点层级数：n -1
        :param is_chk_node: True-既有节点，同时带复选框；False-只有节点，没复选框
        """
        self.node_list.append(element)
        attrs = element.get_attribute('class').strip()

        if is_chk_node:
            # is_click = attrs.endswith(('full' if is_open else 'part')) or curr_idx == node_levels
            # @TODO 含复选框的树在此处理
            is_click = True
        else:
            # 关闭：class ="x-tree-ec-icon x-tree-elbow-end-plus"

            # 打开：class ="x-tree-ec-icon x-tree-elbow-end-minus"
            is_click = attrs.endswith('plus') or curr_idx == node_levels

        # 状态不一致时点击
        if is_click:
            element.click()
            sleep(0.3)

    def _other_left_tree(self, node_info):
        node_flag = node_info['NODE_FLAG']
        if node_flag in ('02', '03', '04'):
            self.user_tab_query(node_flag, node_info['NODE_VALE'])
        elif node_flag in ('05', '06', '07'):
            self.group_tab_query(node_flag, node_info['NODE_VALE'])

    def user_tab_query(self, node_flag, node_value, number=1):

        """
        选择左边树用户Tab页面，并根据节点类型，输入并查询相应结果
        :param node_flag: 节点分类
        :param node_value: 节点值
        :param number:查询结果显示的区域，number：代表第几个行，默认是1

        """
        # 根据node_flag选择相应的节点查询条件xpath，并输入查询条件
        # {02:代表用户编号，03：代表终端逻辑地址，04：电能表资产号}
        # {05:普通群组，06：重点用户群组，07：控制群组}
        # 点击用户标签页
        self._click_node_tab('02')

        self.input(node_value, *TreeLocators.USER_QRY_INPUT[node_flag])

        # 点击查询按钮
        self.click(TreeLocators.USER_BTN_QUERY)

        # 等待查询结果，最好通过其他途径判断查询已返回
        self.commonWait(TreeLocators.NODE_USER_TAB_RSLT_DEFAULT)
        self.clear(TreeLocators.USER_QRY_INPUT[node_flag])

        # 定位查询结果，默认选择第一行记录
        xpath = self.format_xpath(TreeLocators.NODE_USER_TAB_RSLT, node_value)
        print(xpath)

        self.click(xpath)
        # print('------------')

    def group_tab_query(self, node_flag, node_value, number=1):
        # 点击群组标签页
        # @TODO 还需考虑“群组”标签页滚动后才能找到
        self._click_node_tab('06')

        # 选择群组类型
        self.group_node = TreeLocators.GROUP_NODE[node_flag]
        el = self._find_displayed_element(self.group_node)
        attrs = el.get_attribute('class').strip()
        if attrs.endswith('collapsed'):
            el.click()

        node_info = {'NODE_FLAG': '01'}
        node_info.setdefault('NODE_VALE', node_value.split(','))
        self.node_list = []
        self.tree_type = '50'
        self._operate_left_tree(node_info)




class TreeSingleUserPage(BaseTreePage):
    """
    目前应用于统计查询-->综合查询-->单户综合查询菜单
    """
    def _find_in_parent(self, item, idx, items):
        """
        在父节点范围内查找
        :param item:
        :param idx:
        :param items:
        :return:
        """

        levels = len(items) - 1  # 总层级数-1
        locator = self.format_xpath(TreeSingleUserLocators.NODE_LEVEL, (item))
        # 不带复选框的叶子节点只点击文本元素，不点击文本元素边上的图标元素
        if idx == levels and self.tree_type[1] == '0':
            locator = self.format_xpath(TreeSingleUserLocators.LEEF_NODE, item)
        return locator

    def _node_click(self, element, curr_idx, node_levels, is_chk_node=False):
        """

        :param element:
        :param curr_idx:当前节点序号：0 开始
        :param node_levels:当前节点层级数：n -1
        :param is_chk_node: True-既有节点，同时带复选框；False-只有节点，没复选框
        """
        self.node_list.append(element)
        attrs = element.get_attribute('class').strip()

        # 关闭：class ="x-tree-ec-icon x-tree-elbow-end-plus"

        # 打开：class ="x-tree-ec-icon x-tree-elbow-end-minus"
        is_click = attrs.endswith('plus') or curr_idx == node_levels

        # 状态不一致时点击
        if is_click:
            element.click()
            sleep(0.3)

    def find_user_line(self, value):
        if value.find(';') > 0:
            value = value.split(';')[1]
        split_line_loc = self.format_xpath_multi(TreeSingleUserLocators.SPLIT_LINE, is_multi_tab=True)
        el_src = self._find_element(split_line_loc)

        target_loc = self.format_xpath_multi(TreeSingleUserLocators.DROP_TARGET, '终端地址', True)
        el_target = self._find_elements(target_loc)[0]

        ActionChains(self.driver).drag_and_drop(el_src, el_target).perform()
        sleep(2)
        elements = self._find_elements(TreeSingleUserLocators.TMNL_NODE)
        for el in elements:
            class_info = el.get_attribute('class')
            if class_info.endswith('collapsed'):
                el.click()
            xpath = self.format_xpath(TreeSingleUserLocators.USER_LINE, value)
            self.click(xpath)
        sleep(1)
        target_loc = self.format_xpath_multi(TreeSingleUserLocators.DROP_TARGET, '表资产号', True)
        el_target = self._find_elements(target_loc)[0]
        ActionChains(self.driver).drag_and_drop(el_src, el_target).perform()
        sleep(2)

    # def el_click(self, el):
    #     """
    #     触发元素click操作
    #     :param el: 元素实例
    #     """
    #
    #
    #     # js = 'arguments[0].click();'
    #     # js = 'var evt = document.createEvent("Event"); \
    #     #      evt.initEvent("click",true,true); \
    #     #      arguments[0].dispatchEvent(evt);'
    #     # js = 'var evt = document.createEvent("Event"); \
    #     # evt.initEvent("click", true, true); \
    #     # arguments[0].dispatchEvent(evt);'
    #
    #     # js = 'var ev = document.createEvent("HTMLEvents"); \
    #     #         ev.initEvent("click", false, true); \
    #     #         arguments[0].dispatchEvent(ev); '
    #
    #     self.driver.execute_script(js, el)

    def user_query(self, node_value):
        value = self.get_para_value(node_value)
        el = self._find_displayed_element(TreeSingleUserLocators.QRY_INPUT)
        el.clear()
        el.send_keys(value)

        # 点击查询按钮
        el_btn = self._find_displayed_element(TreeSingleUserLocators.BTN_QUERY)
        if bool(el_btn):
            el_btn.click()

        self.timeout_seconds = 10
        self.query_timeout()

        self.find_user_line(value)
