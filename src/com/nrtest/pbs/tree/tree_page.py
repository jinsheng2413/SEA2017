# -*- coding: utf-8 -*-

"""
@author: 李建方
@license: (C) Copyright 2018, Nari.
@file: left_tree_manage.py
@time: 2019-01-09 9:31
@desc:
"""
import re
from copy import deepcopy
from time import sleep

from com.nrtest.common.base_page import Page
from com.nrtest.common.data_access import DataAccess
from com.nrtest.common.dictionary import Dict
from com.nrtest.pbs.tree.tree_locators import TreeLocators


class TreePage(Page):
    def __init__(self, driver, menu_page=None, tree_type='11'):
        super().__init__(self, driver, menu_page)
        self.tree_type = tree_type


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
        self._operate_left_tree(node)
        self.tree_node = node

    def colseLeftTree(self):
        node = deepcopy(self.tree_node)
        node['NODE_VALE'].reverse()
        self._operate_left_tree(node, False)

    def _operate_left_tree(self, node_info, is_open=True):
        """
        根据左边树节点信息，打开或收起节点信息
        :param node_info: 左边树节点信息
        :param is_open: True-打开左边树；False-收起左边树
        :return:
        """
        node_flag = node_info['NODE_FLAG']
        if node_flag == '01':  # 选择全模型
            items = node_info['NODE_VALE']
            ln = len(items) - 1
            for idx, item in enumerate(items):
                new_idx = idx if is_open else ln - idx

                # 厂站间有重复节点名，如电压等级、厂站设备等
                if self._find_in_sub(item):
                    # 厂站范围内找节点
                    if is_open:
                        parent_idx = idx - 1
                    else:
                        parent_idx = idx + 1
                    locator = self.format_xpath(TreeLocators.NODE_LEVEL_IN_SUB, (parent_idx, items[parent_idx], new_idx, item))
                else:
                    locator = self.format_xpath(TreeLocators.NODE_LEVEL, (new_idx, item))

                if self.tree_type == '13':  # 带复选框的左边树
                    els = self._find_elements(locator)
                    el = els[0]
                    
                    if idx == ln:
                        node_status = self._node_status(els[1], is_open, idx, ln, 2)
                        # 状态不一致时点击
                        if node_status:
                            el.click()
                            sleep(0.3)
                else:
                    el = self._find_element(locator)

                if bool(el):
                    node_status = self._node_status(el, is_open, idx, ln)
                    # 状态不一致时点击
                    if node_status:
                        el.click()
                        sleep(0.3)

        else:  # 选择其他节点
            # self.menuPage.btn_user_nodes(node_flag, node_vale)  # 该方法细节待实现
            pass

    def _find_in_sub(self, item):
        is_step_into = False
        # 10-普通树；
        # 11-含电压等级厂站树；
        # 12-厂站档案设备树；
        # 13-普通树基础上带复选框；采集运维-->手动对时
        if self.tree_type == '11':  # 11-含电压等级的厂站树
            is_step_into = bool(re.search(r'^\d{1,4}.k[vV]$', item))
        elif self.tree_type == '12': # 12-厂站档案设备
            is_step_into = item in ['线端', '刀闸', '发电机组', '电容器', '负荷', '开关']

        return is_step_into

    def _node_status(self, element, is_open, curr_idx, tree_len, img_type=1):
        """

        :param element:
        :param is_open:
        :param curr_idx:
        :param tree_len:
        :param img_type: 1-点节点打开或收起；2-点节点中选中或取消选择复选框
        :return:
        """
        is_click = True
        if img_type == 1:
            # 目前仅对pbs5000有效:判断当前节点是打开还是关闭
            attrs = element.get_attribute('class').strip()
            is_click = attrs.endswith(('close' if is_open else 'open')) or curr_idx == tree_len
        elif img_type == 2:
            # 目前仅对pbs5000有效:判断当前节点是选中，不选中
            # 带复选框的左边树：不选中：class="button chk checkbox_false_full"  选中：class="button chk checkbox_false_part"
            attrs = element.get_attribute('class').strip()
            is_click = attrs.endswith(('full' if is_open else 'part')) or curr_idx == tree_len
        return is_click