# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: bg.py
@time: 2018/7/4 0004 17:15
@desc:
"""

from unittest import TestSuite, TestLoader, TextTestRunner

from com.nrtest.sea.testcase.stat_rey.reportMan.ItsChinese.test_tmnlInsertQuery import TestTmnlInsertQuery

suite = TestSuite()
suite.addTests(TestLoader().loadTestsFromTestCase(TestTmnlInsertQuery))
# tests = [TestGatherSuccessRate('test_epp_task_type')]
# suite.addTests(tests)


if __name__ == '__main__':
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
