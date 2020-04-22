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
from b_page.update_popup import UpdatePopup
from b_page.iknow import Iknow
from b_page.my_set import MySet

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

    def test_01_login_abnormal(self):
        '''正确用户名，错误密码登录'''
        log.info("---验证正确用户名、正确密码登录---")
        tel = get_yaml_value(TEST_ACCOUNT_PATH, 'account_1')
        pwd = get_yaml_value(TEST_ACCOUNT_PATH, 'pwd_1_wrong')
        lp = LoginPage(self.driver)
        lp.login_opera(tel, pwd)
        time.sleep(2)
        result = lp.is_exist_element("登录")
        self.assertTrue(result)
        time.sleep(2)

    def test_02_login_normal(self):
        '''正确用户名，正确密码登录'''
        log.info("---验证正确用户名、正确密码登录---")
        tel = get_yaml_value(TEST_ACCOUNT_PATH, 'account_1')
        pwd = get_yaml_value(TEST_ACCOUNT_PATH, 'pwd_1_right')
        lp = LoginPage(self.driver)
        lp.login_opera(tel, pwd)
        time.sleep(2)
        # 判断是否登录成功
        result = False
        if lp.is_exist_element("立即更新"):
            result = True
            UpdatePopup(self.driver).cancel_opera()
            if lp.is_exist_element("我知道了"):
                Iknow(self.driver).click_iknow_btn()
        else:
            if lp.is_exist_element("我知道了"):
                result = True
                Iknow(self.driver).click_iknow_btn()
            else:
                if lp.is_exist_element("首页"):
                    result = True
        self.assertTrue(result)
        time.sleep(1)

    def test_03_logout(self):
        '''退出登录'''
        log.info("---验证退出登录---")
        # 进入我的->设置
        ms = MySet(self.driver)
        ms.enter_to_my()
        ms.enter_to_set()
        # 点击退出登录
        ms.logout_opera()

        # 断言是否退出成功
        time.sleep(1)
        result = ms.is_exist_element("验证码登录")
        self.assertTrue(result)

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
