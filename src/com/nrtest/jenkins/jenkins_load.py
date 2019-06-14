# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: jenkins_load.py
@time: 2019/4/19 0019 14:54
@desc:
"""
from com.nrtest.common.setting import Setting
import jenkins


class JzPythonJenkins(object):
    '''
    Installing:
        pip install python-jenkins

    Import:
        import jenkins
    '''

    def __init__(self):
        username = 'admin'
        password = '123456'
        url = 'http://localhost:8080/jenkins'
        timeout = 1
        self.server = self.Connect(url, username, password, timeout)

    def Used(self):
        self.get_version()

    def read_jop_config(self):
        with open(Setting.DEFAULT_CONFIG, 'r', encoding='utf-8') as file:
            str = file.read()
            return str


    def Connect(self, url, username, password, timeout):
        '''Create handle to Jenkins instance'''
        self.server = jenkins.Jenkins(url, username, password, timeout)
        return self.server

    def get_version(self):
        '''get jenkins version'''
        version = self.server.get_version()
        print(version)

    def create_project(self, name, config_xml=''):
        try:
            if self.assert_jop_exist(name):
                return
            print('--------')
            if config_xml != '':
                self.server.create_job(name, config_xml)
            else:
                self.server.create_job(name, jenkins.EMPTY_CONFIG_XML)
            self.server.assert_job_exists(name,'%sjop创建失败')
        except Exception as e:
            print(e)

    def delete_project(self, name):
        # 删除Project
        self.server.delete_job('empty')


    def get_config_info(self, jop_name, path=Setting.DEFAULT_CONFIG):
      try:
        my_job = self.server.get_job_config(jop_name)
        with open(path, 'w', encoding='utf-8') as file:
            file.write(my_job)
      except Exception:
          print('获取默认配置失败')

    def re_config_jop(self,jop_name,xml_file=''):
        self.server.reconfig_job(jop_name,xml_file)
    # 禁用项目
    def disable_project(self, name):
        self.server.disable_job(name)

    # 启用项目
    def enable_project(self, name):
        self.server.enable_job(name)

    # 构建项目
    def build_project(self, name):
        self.server.build_job(name)

    # 复制jop的配置
    def copy_project(self, name, copyname):
        self.server.copy_job(name, copyname)
        self.server.reconfig_job(name, jenkins.RECONFIG_XML)

    # 查看jop是否存在
    def assert_jop_exist(self, name):
        try:
            self.server.assert_job_exists(name, '你查询的%s不存在')
        except jenkins.JenkinsException as e:
            print(e)
            return True


    def get_output(self, name, num):
        contetn = self.server.get_build_console_output(name, num)
        print(contetn)
        return contetn



if __name__ == "__main__":
    JzPythonJenkins = JzPythonJenkins()
    JzPythonJenkins.view()
