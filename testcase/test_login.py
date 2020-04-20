#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/16
# @Author  : lfr

import time
import unittest
from common.base_log import log
from common.base_driver import BaseDriver
from common.base_operate import get_yaml_value
from config.path_config import TEST_ACCOUNT_PATH
from b_page.login import LoginPage
from b_page.start_page import StartPage

class TestLogin(unittest.TestCase):
    '''
    验证登录功能是否正常。正确的用户名密码登录成功，错误的密码登录失败
    '''
    @classmethod
    def setUpClass(cls) -> None:
        '''初始化，进入登录页面'''
        log.info("----开始执行用例：登录-----")
        cls.driver = BaseDriver().android_driver()
        StartPage(cls.driver).swipe_start()
        return cls.driver

    def setUp(self) -> None:
        pass

    def test_login_abnormal(self):
        '''正确用户名，错误密码登录'''
        log.info("---验证 正确用户名、正确密码登录---")
        tel = get_yaml_value(TEST_ACCOUNT_PATH, 'account_1')
        pwd = get_yaml_value(TEST_ACCOUNT_PATH, 'pwd_1_wrong')
        lp = LoginPage(self.driver)
        lp.login_opera(tel, pwd)
        time.sleep(2)
        result = lp.is_exist_element("登录")
        self.assertTrue(result)
        time.sleep(2)

    def test_login_normal(self):
        '''正确用户名，正确密码登录'''
        log.info("---验证 正确用户名、错误密码登录---")
        tel = get_yaml_value(TEST_ACCOUNT_PATH, 'account_1')
        pwd = get_yaml_value(TEST_ACCOUNT_PATH, 'pwd_1_right')
        lp = LoginPage(self.driver)
        lp.login_opera(tel, pwd)
        time.sleep(2)
        result = lp.is_exist_element("立即升级")
        self.assertTrue(result)
        time.sleep(2)

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
