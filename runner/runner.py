#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/16
# @Author  : lfr

import time
import unittest
from common import HTMLTestRunner
from config.path_config import TESTCASE_PATH, REPORT_PATH
from common.update_desired_caps import UpdateDesiredCaps
from common.base_install_app import IsInstallApp
from common.base_log import log
from common.base_appiumServer import AppiumServer

suite = unittest.defaultTestLoader.discover(TESTCASE_PATH, pattern='test_*.py')

if __name__ == '__main__':
    log.info("-----初始化测试环境-----")
    # 启动appium服务
    AppiumServer().start_appium()

    # 更新desired_caps
    UpdateDesiredCaps().update_desired_caps()
    # 判断测试机是否安装app，否则安装
    IsInstallApp().is_install_app()

    # 获取当前时间并指定时间格式
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    # 创建报告文件
    fp = open(REPORT_PATH + now + "_report.html", 'wb')
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="企鹅商家版AppUI自动化测试报告",
                                           description="测试用例情况")

    # 执行测试套件
    runner.run(suite)
    fp.close()

    # 停止appium服务
    AppiumServer().quit_appium()

    log.info("-----测试完成-----")