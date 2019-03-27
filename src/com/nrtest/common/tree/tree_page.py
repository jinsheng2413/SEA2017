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

from com.nrtest.common.base_page import Page
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.dictionary import Dict
from com.nrtest.common.logger import Logger
from com.nrtest.common.tree.tree_locators import *

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
        if bool(menu_page):  # 通过testCase子类基础初始化：com/nrtest/sea/testcase/demo/pbs5000.py
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

    def openLeftTree(self, node_no, by_tree_node=False):
        """
        打开左边树
        :param node_no:
        """
        try:
            node = Dict(eval(node_no))
            node_value = node['NODE_VALUE']
        except:
            # 不是数组时的默认处理
            node = {'NODE_FLAG': '01', 'NODE_VALUE': node_no}
            node_value = node_no

        node['NODE_VALUE'] = DataAccess.getTreeNode(node, by_tree_node).split(';')

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
        if self.tree_type[-1] == '0':  # 非复选框节点，最后一个叶子节点不处理
            self.node_list.pop()

        self.node_list.reverse()
        for node in self.node_list:
            node.click()

    def _operate_left_tree(self, node_info):
        """
        根据左边树节点信息，打开或收起节点信息
        :param node_info: 左边树节点信息
        :return:
        """
        node_flag = node_info['NODE_FLAG']
        if node_flag in ['01', '10']:  # 选择全模型
            items = node_info['NODE_VALUE']
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


class TreePBSPage(BaseTreePage):
    def _click_node_tab(self, node_tab_idx):
        if self.tree_type[0] != '4':
            node_tab = {'01': '全模型', '02': '搜索', '03': '收藏夹', '10': '全模型'}
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

    def openLeftTree(self, node_no):
        super().openLeftTree(node_no, True)


class TreePage(BaseTreePage):
    def _click_node_tab(self, node_tab_idx):
        if self.tree_type[0] != '4':
            node_tab = {'01': '供电区域', '02': '用户', '03': '终端', '04': '行业', '05': '电网结构', '06': '群组', '07': '单户综合'}
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
        if idx == levels and self.tree_type[1] == '0':
            if is_step_into:
                locator = self.format_xpath(TreeLocators.LEEF_NODE_IN_PARENT, (items[idx - 1], item))
                # *********带复选框的叶子节点，除勾选外，是否还需再点击一下
            else:
                if idx == 0:
                    locator = self.format_xpath(TreeLocators.LEEF_PROVINCE, item)
                else:
                    # 不带复选框的叶子节点只点击文本元素，不点击文本元素边上的图标元素
                    locator = self.format_xpath(TreeLocators.LEEF_NODE, item)
        else:
            if is_step_into:
                locator = self.format_xpath(TreeLocators.NODE_LEVEL_IN_PARENT, (items[idx - 1], item))
                # *********带复选框的叶子节点，除勾选外，是否还需再点击一下
            else:
                if idx == 0:
                    locator = self.format_xpath(TreeLocators.NODE_PROVINCE, item)
                else:
                    # 不带复选框的叶子节点只点击文本元素，不点击文本元素边上的图标元素
                    locator = self.format_xpath(TreeLocators.NODE_LEVEL, (item))
        # if is_step_into:
        #     if idx == levels and self.tree_type[1] == '0':
        #         locator = self.format_xpath(TreeLocators.LEEF_NODE_IN_PARENT, (items[idx - 1], item))
        #     else:
        #         locator = self.format_xpath(TreeLocators.NODE_LEVEL_IN_PARENT, (items[idx - 1], item))
        #     # *********带复选框的叶子节点，除勾选外，是否还需再点击一下
        # else:
        #     if idx == 0:
        #         locator = self.format_xpath(TreeLocators.NODE_PROVINCE, item)
        #     else:
        #         # 不带复选框的叶子节点只点击文本元素，不点击文本元素边上的图标元素
        #         if idx == levels and self.tree_type[1] == '0':
        #             locator = self.format_xpath(TreeLocators.LEEF_NODE, item)
        #         else:
        #             locator = self.format_xpath(TreeLocators.NODE_LEVEL, (item))

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
            sleep(1)

    def _other_left_tree(self, node_info):
        node_flag = node_info['NODE_FLAG']
        if node_flag in ('02', '03', '04', '12', '13', '14'):
            self.user_tab_query(node_flag, node_info['NODE_VALUE'])
        elif node_flag in ('05', '06', '07'):
            self.group_tab_query(node_flag, node_info['NODE_VALUE'])

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
        node_info.setdefault('NODE_VALUE', node_value.split(','))
        self.node_list = []
        self.tree_type = '50'
        self._operate_left_tree(node_info)


class TreeSingleUserPage(BaseTreePage):
    """
    应用于 统计查询-->综合查询-->单户综合查询菜单
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


class TreeQualityPage(BaseTreePage):
    """
    应用于 基本应用→数据采集管理→采集质量检查(new)
    """

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

        root_id = TreeQualityLocators.ROOT_IDS[items[0]]
        levels = len(items) - 1  # 总层级数-1
        if idx == levels:
            locator = self.format_xpath(TreeQualityLocators.LEEF_NODE, (root_id, item))
        else:
            if idx == 0:
                locator = self.format_xpath(TreeQualityLocators.NODE_ROOT, root_id)
            else:
                # 不带复选框的叶子节点只点击文本元素，不点击文本元素边上的图标元素
                locator = self.format_xpath(TreeQualityLocators.NODE_LEVEL, (root_id, item))
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
            is_click = attrs.endswith('plus') or attrs.endswith('collapsed') or curr_idx == node_levels

        # 状态不一致时点击
        if is_click:
            element.click()
            sleep(1)
