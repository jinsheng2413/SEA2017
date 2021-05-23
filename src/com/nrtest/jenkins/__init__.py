# -*- coding:utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: __init__.py.py
@time: 2019/4/19 0019 10:38
@desc:
"""
import jenkins
#远程Jenkins的地址
jenkins_server_url = 'http://localhost:8080/jenkins/'

#用户名
user_id = 'admin'

#用户的token值(每个user有对应的token----如本文第3.1节所示)
# api_token = '88be3323ddd487ae8ace47d5c5abd8bd'

#登录密码
passwd = '123456'

# server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=passwd)

#使用  API_Token    进行Jenkins登录操作
server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=passwd)

server.create_job('empty', jenkins.EMPTY_CONFIG_XML)
jobs = server.get_jobs()
print(jobs)
my_job = server.get_job_config('cool-job')
print(my_job) # prints XML configuration
server.build_job('empty')
server.disable_job('empty')
server.copy_job('empty', 'empty_copy')
server.enable_job('empty_copy')
server.reconfig_job('empty_copy', jenkins.RECONFIG_XML)

server.delete_job('empty')
server.delete_job('empty_copy')

# build a parameterized job
# requires creating and configuring the api-test job to accept 'param1' & 'param2'
server.build_job('api-test', {'param1': 'test value 1', 'param2': 'test value 2'})
last_build_number = server.get_job_info('api-test')['lastCompletedBuild']['number']
build_info = server.get_build_info('api-test', last_build_number)
print(build_info)

# get all jobs from the specific view
jobs = server.get_jobs(view_name='View Name')
print(jobs)

