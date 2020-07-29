#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/16
# @Author  : lfr

import time
import unittest
import pytest
import os
from common import HTMLTestRunner
from config.path_config import TESTCASE_PATH, REPORT_PATH, LOG_PATH
from common.update_desired_caps import UpdateDesiredCaps
from common.base_install_app import IsInstallApp
from common.base_log import log
from common.base_removeFile import remove_file
from common.base_appiumServer import AppiumServer

def init_project():
    # log.info("========初始化测试环境========")
    # 清空log中之前的日志文件、report中之前的报告文件
    remove_file(LOG_PATH)
    remove_file(REPORT_PATH)

    # 启动appium服务
    # AppiumServer().start_appium()

    # 更新desired_caps
    UpdateDesiredCaps().update_desired_caps()
    # 判断测试机是否安装app，否则安装
    IsInstallApp().is_install_app()

def get_report():
    # 获取当前时间并指定时间格式
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    # 创建报告文件
    fp = open(REPORT_PATH + now + "_report.html", 'wb')
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="企鹅商家版AppUI自动化测试报告",
                                           description="测试用例情况")

    # 执行测试套件
    suite = unittest.defaultTestLoader.discover(TESTCASE_PATH, pattern='test_*.py')
    runner.run(suite)
    fp.close()


if __name__ == '__main__':
    log.info("========初始化测试环境========")
    init_project()
    # pytest.main(["-v", "testcase/", "--html=./report/report.html", "--reruns", "2", "--reruns-delay", "5"])
    pytest.main(["-v", "-s", "testcase/test_bath_position_management.py", "--html=./report/report.html"])
    log.info("========测试完成========")