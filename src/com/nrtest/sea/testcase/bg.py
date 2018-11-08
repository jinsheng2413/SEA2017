# -*- coding: utf-8 -*-

"""
@author: 郭春彪
@license: (C) Copyright 2018, Nari.
@file: bg.py
@time: 2018/7/4 0004 17:15
@desc:
"""

import unittest

from com.nrtest.sea.testcase.stat_rey.synthQuery.test_AllCollectSuccessRate import TestAllCollectSuccessRate

suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
    TestAllCollectSuccessRate))
# tests = [TestGatherSuccessRate('test_epp_task_type')]
# suite.addTests(tests)


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
