#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/13
# @Author  : lfr

'''
项目路径配置
'''
import os

# 项目根目录路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# config文件路径
CONFIG_PATH = BASE_PATH + '/config/'
# driver配置文件desired_caps.py路径
DESIRED_CAPS_YAML_PATH = CONFIG_PATH + 'desired_caps'
# 测试账号存储文件路径
TEST_ACCOUNT_PATH = CONFIG_PATH + 'test_account'

# app文件夹路径
APP_PATH = BASE_PATH + '/app/'

# 日志文件存储路径
LOG_PATH = BASE_PATH + '/log/'

# 截图文件存储路径
SCREENSHOTS_PATH = BASE_PATH + '/screenshots/'

# 测试用例存储路径
TESTCASE_PATH = BASE_PATH + '/testcase/'

# 测试报告存储路径
REPORT_PATH = BASE_PATH + '/report/'



if __name__ == '__main__':
    print(DESIRED_CAPS_YAML_PATH)