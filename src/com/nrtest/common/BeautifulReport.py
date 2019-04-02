# -*- coding: utf-8 -*-
"""
@Version: 1.0
@Project: BeautyReport
@Author: Raymond
@Data: 2017/11/15 下午5:28
@File: BeautifulReport.py
@License: MIT
"""

import base64
import json
import os
import platform
import sys
import time
import traceback
import unittest
from functools import wraps
from io import StringIO

from com.nrtest.common.setting import Setting
from com.nrtest.common.user_except import PopupError, TestImgError, TestSkipError, BtnQueryError

__all__ = ['BeautifulReport']

# HTML_IMG_TEMPLATE = """
#     <div align="center"><a href="data:image/png;base64, {}">
#     <img src="data:image/png;base64, {}" width="800px" height="500px" />
#     </a></div>
#     <br></br>
# """
HTML_IMG_TEMPLATE = """
    <div align="center">
    <img src="data:image/png;base64, {}" width="800px" height="500px" />
    </a></div>
    <br></br>
"""

class OutputRedirector():
    """ Wrapper to redirect stdout or stderr """

    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()


stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)

# SYSSTR = platform.system()
# SITE_PAKAGE_PATH = get_python_lib()

FIELDS = {
    'testPass': 0,
    'testResult': [
    ],
    'testName': '',
    'testAll': 0,
    'testFail': 0,
    'beginTime': '',
    'totalTime': '',
    'testSkip': 0
}

CASE_COSTS = {}

class PATH:
    """ all file PATH meta """
    config_tmp_path = os.path.dirname(__file__) + '{}template'.format('/' if platform.system() != 'Windows' else '\\')

class MakeResultJson:
    """ make html table tags """

    def __init__(self, datas: tuple):
        """
        init self object
        :param datas: 拿到所有返回数据结构
        """
        self.datas = datas
        self.result_schema = {}

    def __setitem__(self, key, value):
        """

        :param key: self[key]
        :param value: value
        :return:
        """
        self[key] = value

    def __repr__(self) -> str:
        """
            返回对象的html结构体
        :rtype: dict
        :return: self的repr对象, 返回一个构造完成的tr表单
        """
        keys = (
            'className',
            'methodName',
            'description',
            'spendTime',
            'status',
            'log',
        )
        for key, data in zip(keys, self.datas):
            self.result_schema.setdefault(key, data)
        return json.dumps(self.result_schema)


class ReportTestResult(unittest.TestResult):
    """ override"""

    def __init__(self, suite, stream=sys.stdout):
        """ pass """
        super(ReportTestResult, self).__init__()
        self.begin_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.start_time = 0
        self.stream = stream
        self.end_time = 0
        self.failure_count = 0
        self.error_count = 0
        self.success_count = 0
        self.skipped = 0
        self.verbosity = 1
        self.success_case_info = []
        self.skipped_case_info = []
        self.failures_case_info = []
        self.errors_case_info = []
        self.all_case_counter = 0
        self.suite = suite
        self.status = ''
        self.result_list = []
        self.case_log = ''
        self.default_report_name = '自动化测试报告'
        self.FIELDS = None
        self.sys_stdout = None
        self.sys_stderr = None
        self.outputBuffer = None

    @property
    def success_counter(self) -> int:
        """ set success counter """
        return self.success_count

    @success_counter.setter
    def success_counter(self, value) -> None:
        """
            success_counter函数的setter方法, 用于改变成功的case数量
        :param value: 当前传递进来的成功次数的int数值
        :return:
        """
        self.success_count = value

    def startTest(self, test) -> None:
        """
            当测试用例测试即将运行时调用
        :return:
        """
        unittest.TestResult.startTest(self, test)
        self.outputBuffer = StringIO()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.sys_stdout = sys.stdout
        self.sys_stdout = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector
        self.start_time = time.time()

    def stopTest(self, test) -> None:
        """
            当测试用例执行完成后进行调用
        :return:
        """
        self.end_time = '{0:.3}s'.format((time.time() - self.start_time))
        self.result_list.append(self.get_all_result_info_tuple(test))
        self.complete_output()

    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.sys_stdout:
            sys.stdout = self.sys_stdout
            sys.stderr = self.sys_stdout
            self.sys_stdout = None
            self.sys_stdout = None
        return self.outputBuffer.getvalue()

    def stopTestRun(self, title=None) -> dict:
        """
            所有测试执行完成后, 执行该方法
        :param title:
        :return:
        """
        FIELDS['testPass'] = self.success_counter
        for item in self.result_list:
            item = json.loads(str(MakeResultJson(item)))
            FIELDS.get('testResult').append(item)
        FIELDS['testAll'] = len(self.result_list)
        FIELDS['testName'] = title if title else self.default_report_name
        FIELDS['testFail'] = self.failure_count
        FIELDS['beginTime'] = self.begin_time
        end_time = int(time.time())
        start_time = int(time.mktime(time.strptime(
            self.begin_time, '%Y-%m-%d %H:%M:%S')))
        FIELDS['totalTime'] = str(end_time - start_time) + 's'
        FIELDS['testError'] = self.error_count
        FIELDS['testSkip'] = self.skipped
        self.FIELDS = FIELDS
        return FIELDS

    def get_all_result_info_tuple(self, test) -> tuple:
        """
            接受test 相关信息, 并拼接成一个完成的tuple结构返回
        :param test:
        :return:
        """

        try:
            # 点查询按钮到查询结果出来时之间的耗时时长
            cost_seconds = str(CASE_COSTS[test.tst_case_id])
        except:
            cost_seconds = '**'

        rows = []
        ln = 180  # 长度超过过时截断
        for i, log in enumerate(self.case_log):
            if log.startswith('File ') and len(log) > ln:
                rows.append([i, log])
        for row in rows:
            self.case_log[row[0]] = row[1][:ln] + ' \\'
            self.case_log.insert(row[0] + 1, row[1][ln:])

        return tuple([*self.get_testcase_property(test), cost_seconds + '/' + self.end_time, self.status, self.case_log])

    @staticmethod
    def error_or_failure_text(err) -> str:
        """
            获取sys.exc_info()的参数并返回字符串类型的数据, 去掉t6 error
        :param err:
        :return:
        """
        return traceback.format_exception(*err)

    def addSuccess(self, test) -> None:
        """
            pass
        :param test:
        :return:
        """
        logs = []
        output = self.complete_output()
        logs.append(output)
        if self.verbosity > 1:
            sys.stderr.write('ok ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('.')
        self.success_counter += 1
        self.status = '成功'
        self.case_log = output.split('\n')
        self._mirrorOutput = True  # print(class_name, method_name, method_doc)

    def addError(self, test, err):
        """
            add Some Error Result and infos
        :param test:
        :param err:
        :return:
        """
        logs = []
        output = self.complete_output()
        logs.append(output)
        logs.extend(self.error_or_failure_text(err))
        self.failure_count += 1
        self.add_test_type('失败', logs)
        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')

        self._mirrorOutput = True

    def addFailure(self, test, err):
        """
            add Some Failures Result and infos
        :param test:
        :param err:
        :return:
        """
        logs = []
        output = self.complete_output()
        logs.append(output)
        logs.extend(self.error_or_failure_text(err))
        self.failure_count += 1
        self.add_test_type('失败', logs)
        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')

        self._mirrorOutput = True

    def addSkip(self, test, reason) -> None:
        """
            获取全部的跳过的case信息
        :param test:
        :param reason:
        :return: None
        """
        logs = [reason]
        self.complete_output()
        self.skipped += 1
        self.add_test_type('跳过', logs)

        if self.verbosity > 1:
            sys.stderr.write('S  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('S')
        self._mirrorOutput = True

    def add_test_type(self, status: str, case_log: list) -> None:
        """
            abstruct add test type and return tuple
        :param status:
        :param case_log:
        :return:
        """
        self.status = status
        self.case_log = case_log

    @staticmethod
    def get_testcase_property(test) -> tuple:
        """
            接受一个test, 并返回一个test的class_name, method_name, method_doc属性
        :param test:
        :return: (class_name, method_name, method_doc) -> tuple
        """
        class_name = test.__class__.__qualname__
        method_name = test.__dict__['_testMethodName']
        method_doc = test.__dict__['_testMethodDoc'].replace(' ', '')
        return class_name, method_name, method_doc


class BeautifulReport(ReportTestResult):
    def __init__(self, suites):
        super(BeautifulReport, self).__init__(suites)
        self.suites = suites
        self.log_path = None
        self.title = '自动化测试报告'
        self.filename = 'report.html'
        self.case_id = ''

    def report(self, description, filename: str = None):
        """
            生成测试报告,并放在当前运行路径下
        :param filename: 生成文件的filename
        :param description: 生成文件的注释
        :return:
        """

        if filename:
            self.filename = filename if filename.endswith('.html') else filename + '.html'


        if description:
            self.title = description

        self.log_path = Setting.REPORT_PATH
        self.suites.run(result=self)
        self.stopTestRun(self.title)
        self.output_report()
        print('\n测试已全部完成, 可前往“{}”查看测试报告'.format(self.log_path))

    def output_report(self):
        """
            生成测试报告到指定路径下
        :return:
        """
        # template_path = self.config_tmp_path
        template_path = os.path.dirname(__file__) + '{}template'.format('/' if platform.system() != 'Windows' else '\\')
        report_path = Setting.REPORT_PATH

        with open(template_path, 'rb') as file:
            body = file.readlines()

        with open(report_path + self.filename, 'wb') as write_file:
            for item in body:
                if item.strip().startswith(b'var resultData'):
                    head = '    var resultData = '
                    item = item.decode().split(head)
                    item[1] = head + \
                              json.dumps(self.FIELDS, ensure_ascii=False, indent=4)
                    item = ''.join(item).encode()
                    item = bytes(item) + b';\n'
                write_file.write(item)

    @staticmethod
    def img2base(img_path: str, file_name: str) -> str:
        """
            接受传递进函数的filename 并找到文件转换为base64格式
        :param img_path: 通过文件名及默认路径找到的img绝对路径
        :param file_name: 用户在装饰器中传递进来的问价匿名
        :return:
        """
        with open(img_path + file_name, 'rb') as file:
            data = file.read()
        return base64.b64encode(data).decode()

    @staticmethod
    def get_screenshot(obj, img_path=None, fun_name=''):
        if not bool(img_path):
            img_path = Setting.IMG_PATH
        img_name = fun_name + '_' + time.strftime('%Y%m%d%H%M%S') + '.png'
        if 'save_img' in dir(obj):
            save_img = getattr(obj, 'save_img')
            save_img(img_path, img_name)
            print('<h3><font face="verdana">页面截图：</font></h3></br>')
            data = BeautifulReport.img2base(img_path, img_name)
            print(HTML_IMG_TEMPLATE.format(data))

    def add_test_img(*pargs):
        """
            接受若干个图片元素, 并展示在测试报告中
        :param pargs:
        :return:
        """

        def _wrap(func):
            @wraps(func)
            def __wrap(*args, **kwargs):
                img_path = Setting.IMG_PATH
                try:
                    result = func(*args, **kwargs)
                    # -----------------------
                    # 页面弹窗判断处理
                    img_name = time.strftime('%Y%m%d%H%M%S') + '_' + func.__name__ + '.png'
                    popup = getattr(args[0], 'popup')
                    dlg_src, action, info = popup(img_path, img_name, '', 4)
                    # action：00-没弹窗；01-截图，且抛异常；02-只截图，不抛异常；
                    #         03-既不截图，也不抛异常; 04-没弹窗时，也截图，抛异常
                    if action in ('01', '02', '04'):
                        print('<h3><font face="verdana">页面截图：</font></h3></br>')
                        data = BeautifulReport.img2base(img_path, img_name)
                        print(HTML_IMG_TEMPLATE.format(data))
                        if action in ['01', '04']:
                            raise TestImgError(info)
                except (PopupError, TestImgError, TestSkipError) as pe:
                    raise pe
                except BtnQueryError as bqe:
                    CASE_COSTS.update(bqe.get_qry_cost_sec)
                    BeautifulReport.get_screenshot(args[0], img_path, func.__name__)
                    raise bqe
                except Exception as ex:
                    BeautifulReport.get_screenshot(args[0], img_path, func.__name__)
                    # img_name = func.__name__ + '_' + time.strftime('%Y%m%d%H%M%S') + '.png'
                    # if 'save_img' in dir(args[0]):
                    #     save_img = getattr(args[0], 'save_img')
                    #     save_img(img_path, img_name)
                    #     print('<h3><font face="verdana">页面截图：</font></h3></br>')
                    #     data = BeautifulReport.img2base(img_path, img_name)
                    #     print(HTML_IMG_TEMPLATE.format(data))

                    # sys.exit(0)
                    raise ex

                print('<br></br>')

                if len(pargs) > 1:
                    for parg in pargs:
                        file = img_path + parg + '.png'
                        if os.path.isfile(file):
                            print('<h3><font face="verdana"><b>' + parg + '：</b></font></h3></br>')
                            data = BeautifulReport.img2base(img_path, parg + '.png')
                            print(HTML_IMG_TEMPLATE.format(data))
                    return result
                return result

            return __wrap

        return _wrap

    def add_popup_img(*pargs):
        """
            接受若干个图片元素, 并展示在测试报告中
        :param pargs:
        :return:
        """

        def _wrap(func):
            @wraps(func)
            def __wrap(*args, **kwargs):
                img_path = Setting.IMG_PATH
                fun_name = func.__name__
                if fun_name == 'start_case':
                    CASE_COSTS.update({args[1]['TST_CASE_ID']: '--'})

                result = func(*args, **kwargs)

                if fun_name == 'btn_query':  # 来自查询按钮
                    CASE_COSTS.update(result)

                dlg_title = ''
                if isinstance(result, dict):  # skip_to/skip_to_page的返回值
                    try:
                        dlg_title = result['DLG_TITLE']
                    except:
                        pass

                # 页面弹窗判断处理
                popup = getattr(args[0], 'popup')
                img_name = time.strftime('%Y%m%d%H%M%S') + '_' + func.__name__ + '.png'
                dlg_src, action, info = popup(img_path, img_name, dlg_title, *pargs)
                # action：00-没弹窗；01-截图，且抛异常；02-只截图，不抛异常；
                #        03-既不截图，也不抛异常; 04-没弹窗时，也截图，抛异常
                if action in ('01', '02', '04'):
                    print('<h3><font face="verdana">对话框截图：</font></h3></br>')
                    data = BeautifulReport.img2base(img_path, img_name)
                    print(HTML_IMG_TEMPLATE.format(data))
                if action in ['01', '04']:
                    raise PopupError(action, info if action == '04' else '对话框信息：{}'.format(info))

                if dlg_src == 6 and action == '03':  # 来自跳转，且有符合期望的弹窗：高级应用→问题交流平台→知识库管理  能点击弹窗，但tag_name不是链接（a）的情况
                    result['CLICKABLE'] = True

                return result

            return __wrap

        return _wrap
