# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: common_page.py
@time: 2018/6/25 0025 14:53
@desc:
"""
from com.nrtest.common.base_page import Page
from com.nrtest.sea.locators.other.menu_common_man_pageLocators import SecurityCommonManPageLocators


class Common_page(Page):
    # 【左边树】
    def btn_left_add(self):
        self.click(*SecurityCommonManPageLocators.BTN_LEFT_ADD)

    # 选中省份
    def btn_select_province(self):
        self.click(*SecurityCommonManPageLocators.BTN_LEFT_MENU_ELETRIC)

    # 选择公司
    def btn_select_company(self, number):
        lr = self.get_select_locator(
            SecurityCommonManPageLocators.BTN_COMPANY, number)
        print(lr)
        self.click(*lr)

    # 点击系统管理
    def btn_sys_man(self):
        self.click(*SecurityCommonManPageLocators.BTN_SYS_MANAGE)

    # 点击系统配置管理
    def btn_sys_config_man(self):
        self.click(*SecurityCommonManPageLocators.BTN_SYS_CONFIG_MAN)

    # 点击数据字典管理
    def btn_data_dic_man(self):
        self.click(*SecurityCommonManPageLocators.BTN_DATA_DIC_MAN)

    # 点击日志管理
    def btn_log_man(self):
        self.click(*SecurityCommonManPageLocators.BTN_LOG_MAN)

    # 点击系统登陆日志
    def btn_sys_login_log(self):
        self.click(*SecurityCommonManPageLocators.BTN_SYS_LOGIN_LOG)

    # 点击系统操作日志
    def btn_sys_operation_log(self):
        self.click(*SecurityCommonManPageLocators.BTN_SYS_OPERATION_LOG)

    # 点击升级日志
    def btn_upgrade_log(self):
        self.click(*SecurityCommonManPageLocators.BTN_SYS_UPGRADE_LOG)

    # 点击双向箭头
    def btn_left_arrow(self):
        self.click(*SecurityCommonManPageLocators.BTN_LEFT_MENU)

    # 选中省份
    def btn_select_province(self):
        self.click(*SecurityCommonManPageLocators.BTN_LEFT_MENU)
        self.click(*SecurityCommonManPageLocators.BTN_LEFT_MENU_ELETRIC)

    # 系统使用情况统计
    def btn_man_sys_use_count(self):
        self.click(*SecurityCommonManPageLocators.BTN_SYS_USE_SITUATION_COUNT)

    # 用户分布情况统计
    def btn_man_use_distribution_count(self):
        self.click(*SecurityCommonManPageLocators.BTN_SYS_USER_DISTRIBUTION_COUNT)

    # 菜单使用情况统计
    def btn_man_menu_use_distribution_count(self):
        self.click(*SecurityCommonManPageLocators.BTN_SYS_MENU_DISTRIBUTION_COUNT)

    # 信息定制
    def btn_information_customization(self):
        self.click(*SecurityCommonManPageLocators.BTN_INFORMATION_CUSTOMIZATION)

    # 悬停推送信息定制
    def hover_push_information_customization(self):
        self.hover(
            *SecurityCommonManPageLocators.BTN_PUSH_INFORMATION_CUSTOMIZATION)

    # 点击信息设置
    def btn_information_make(self):
        self.click(*SecurityCommonManPageLocators.BTN_INFORMATION_MAKE)

    # 重要信息推出
    def btn_imp_Inf_push(self):
        self.click(*SecurityCommonManPageLocators.BTN_IMPORTANT_INFORMATION_PUSH)

    # 监控台定制
    def btn_moitor_cust(self):
        self.click(*SecurityCommonManPageLocators.BTN_MONITOR_CUSTOMIZATION)

    # 工作台定制
    def btn_work_cust(self):
        self.click(*SecurityCommonManPageLocators.BTN_WORK_CUSTOMIZATION)

    # 选择省分公司
    def btn_select_province(self):
        self.click(*SecurityCommonManPageLocators.BTN_LEFT_MENU_ELETRIC)

    # 电价参数下发
    def btn_ele_price_para(self):
        self.click(*SecurityCommonManPageLocators.BTN_ELE_PRICE_PARA)

    # 多步骤省公司
    def btn_select_province_more(self):

        hp = self.page_assert_body()
        if hp is True:
            print('------------------------------------')
        elif hp is False:
            self.click(*SecurityCommonManPageLocators.BTN_LEFT_MENU)
            self.click(*SecurityCommonManPageLocators.BTN_LEFT_MENU_ELETRIC)
        else:
            print('省份选择错误')

    # 菜单使用明细
    def btn_menu_detail(self):
        self.click(*SecurityCommonManPageLocators.BTN_MENU_DETAIL)

    # 数据字典管理
    def btn_tab_data_dic(self):
        self.rightClick(*SecurityCommonManPageLocators.BTN_TAB_DATA_DIC)

    # 关闭其他所有页面
    def btn_close_other_all_page(self):
        self.click(*SecurityCommonManPageLocators.BTN_CLOSE_OTHER_ALL_PAGE)

    # 关闭当前页面
    def btn_close_now_page(self):
        self.click(*SecurityCommonManPageLocators.BTN_NOW_PAGE)

    # 确定
    def btn_confirme(self):
        self.click(*SecurityCommonManPageLocators.BTN_CONFIRME)

    # 菜单使用统计
    def btn_mer_menu_use_count(self):
        self.click(*SecurityCommonManPageLocators.BTN_MER_MENU_USE_COUNT)

    def assert_value(self):
        op = self.assert_context(*SecurityCommonManPageLocators.VAL)
        print(op)
        return op

    def page_assert_body(self):
        op = self.assert_body('电网结构')
        return op

    # 点击权限密码管理
    def btn_pwd_manage(self):
        self.click(*SecurityCommonManPageLocators.BTN_PWD_MANAGE)

    # 点击操作员管理
    def btn_operator_manage(self):
        self.click(*SecurityCommonManPageLocators.BTN_OPERATOR_MANAGE)

    # 角色管理
    def btn_role_manage(self):
        self.click(*SecurityCommonManPageLocators.BTN_ROLE_MANAGE)

    # 权限管理
    def btn_sec_manage(self):
        self.click(*SecurityCommonManPageLocators.BTN_SEC_MANAGE)

    # 模板管理
    def btn_tem_manage(self):
        self.click(*SecurityCommonManPageLocators.BTN_TEM_MANAGE)

    # 终端参数
    def btn_zhongduan(self):
        self.click(*SecurityCommonManPageLocators.BTN_ZHONGDUAN)

    # 【高级应用】
    def btn_advApp(self):
        self.click(*SecurityCommonManPageLocators.BTN_ADVAPP)

    # 费控管理
    def btn_fei_mange(self):
        self.click(*SecurityCommonManPageLocators.BTN_FEI_MANGE)

    # 本地费控
    def hover_local_fei_mange(self):
        self.hover(*SecurityCommonManPageLocators.BTN_LOCAL_FEI_MANGE)

    # 专变用户费控管理
    def btn_specil_user_fei_mange(self):
        self.click(*SecurityCommonManPageLocators.BTN_SPE_USER_FEI_MANGE)

    # 低压用户余额查看

    def btn_low_user_money_check(self):
        self.click(*SecurityCommonManPageLocators.BTN_LOW_USER_MONEY_CHECK)

    # 专变用户余额查看
    def btn_spe_user_money_check(self):
        self.click(*SecurityCommonManPageLocators.BTN_SPE_USER_MONEY_CHECK)

    # 统计查询
    # 【一级菜单】
    # 统计查询
    def btn_statrey(self):
        self.click(*SecurityCommonManPageLocators.BTN_STATREY)

    # 统计查询
    def btn_stat_rey(self):
        self.click(*SecurityCommonManPageLocators.BTN_STAT_REY)

    # 【二级菜单】
    # 统计查询→综合查询
    def btn_synthquery(self):
        self.click(*SecurityCommonManPageLocators.BTN_SYNTHQUERY)

    # 【数据分析】
    def btn_dataanalyse(self):
        self.click(*SecurityCommonManPageLocators.BTN_DATAANALYSE)

    # 【三级菜单】
    # 统计查询→综合查询→用户数据查询
    def btn_userdataquery(self):
        self.click(*SecurityCommonManPageLocators.BTN_USERDATAQUERY)

    # 负荷分析
    def hover_loadanalyse(self):
        self.hover(*SecurityCommonManPageLocators.HOVER_LOADANALYSE)

    # 统计查询→综合查询→终端数据查询
    def btn_terminaldataquery(self):
        self.click(*SecurityCommonManPageLocators.BTN_TERMINALDATAQUERY)

    # 负荷排名分析
    def btn_loadanalyse_rank(self):
        self.click(*SecurityCommonManPageLocators.BTN_LOADANALYSE_RANK)

    # 统计查询→综合查询→配变数据查询
    def btn_publicdataquery(self):
        self.click(*SecurityCommonManPageLocators.BTN_PUBLICDATAQUERY)

    # 统计查询→综合查询→线路数据查询
    def btn_linedataquery(self):
        self.click(*SecurityCommonManPageLocators.BTN_LINEDATAQUERY)

    # 专变用户月查看
    def btn_specialUserBalanceQuery(self):
        self.click(*SecurityCommonManPageLocators.BTN_SPECIAL_USER_BALANCE_CHECK)

    # 负荷特性分析
    def btn_load_speciality_analyse(self):
        self.click(*SecurityCommonManPageLocators.BTN_LOAD_SPECIALITY_ANALYSE)

    # 低压用户购电参数下发
    def btn_lowUserBuyParaGiveOut(self):
        self.click(*SecurityCommonManPageLocators.BTN_LOW_USER_BUY_PARA_GIVEOUT)

    # 本地费控执行统计
    def btn_localFeiMangeExecutCount(self):
        self.click(
            *SecurityCommonManPageLocators.BTN_LOCAL_FEI_MANAGE_EXECUTE_COUNT)

    # 费控情况统计
    def btn_localFeiMangeExecutCount_dis_count(self):
        self.click(
            *SecurityCommonManPageLocators.BTN_LOCAL_FEI_MANAGE_EXECUTE_COUNT_DISTRRIBUTIONC)

    # 费控情况明细
    def btn_localFeiMangeExecutCount_dis_detail(self):
        self.click(
            *SecurityCommonManPageLocators.BTN_LOCAL_FEI_MANAGE_EXECUTE_COUNT_DISTRRIBUTIOND)

    # 费控投入调试
    def btn_cust_control_commssioning(self):
        self.click(*SecurityCommonManPageLocators.BTN_CUST_CONTROL_COMMISSIONING)

    # 电费控
    def btn_ele_cust_mange(self):
        self.click(*SecurityCommonManPageLocators.BTN_ELE_CUST_MANAGE)
