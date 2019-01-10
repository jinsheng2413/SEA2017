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
        self.operate_left_tree(node)
        self.tree_node = node

    def colseLeftTree(self):
        node = deepcopy(self.tree_node)
        node['NODE_VALE'].reverse()
        self.operate_left_tree(node, False)

    def operate_left_tree(self, node_info, is_open=True):
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
                if bool(re.search(r'^\d{1,4}.k[vV]$', item)):
                    # 厂站范围内找节点
                    if is_open:
                        parent_idx = idx - 1
                    else:
                        parent_idx = idx + 1
                    locator = self.format_xpath(TreeLocators.NODE_LEVEL_IN_SUB, (parent_idx, items[parent_idx], new_idx, item))
                else:
                    locator = self.format_xpath(TreeLocators.NODE_LEVEL, (new_idx, item))
                el = self._find_element(locator)
                if bool(el):
                    # 目前仅对pbs5000有效
                    attrs = el.get_attribute('class').strip()
                    node_status = attrs.endswith(('close' if is_open else 'open')) or idx == ln
                    # 状态不一致时点击
                    if node_status:  # and is_open:
                        el.click()
                        sleep(0.3)
        else:  # 选择其他节点
            # self.menuPage.btn_user_nodes(node_flag, node_vale)  # 该方法细节待实现
            pass
