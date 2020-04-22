#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/22
# @Author  : lfr

import time
import unittest
from common.base_log import log
from common.base_driver import BaseDriver
from common.base_operate import get_yaml_value
from config.path_config import TEST_ACCOUNT_PATH
from b_page.page_init import PageInit
from b_page.my_set import MySet
from b_page.login import LoginPage
from b_page.update_popup import UpdatePopup

class ModifyPwd(unittest.TestCase):
    '''
    验证修改密码功能
    '''
    @classmethod
    def setUpClass(cls) -> None:
        '''初始化进入App首页'''
        log.info("----开始执行用例：修改密码-----")
        cls.driver = BaseDriver().android_driver()
        PageInit(cls.driver).init_to_home()

    def setUp(self) -> None:
        pass

    def test_01_modify_pwd(self):
        '''验证能否修改密码'''
        log.info("验证能否修改密码")
        # ->我的->设置
        ms = MySet(self.driver)
        ms.enter_to_my()
        ms.enter_to_set()
        # 修改密码操作
        old_pwd = get_yaml_value(TEST_ACCOUNT_PATH, 'old_pwd_s')
        new_pwd = get_yaml_value(TEST_ACCOUNT_PATH, 'new_pwd_s')
        ms.change_pwd(old_pwd, new_pwd)

        # 判断是否修改成功
        result = ms.is_toast_exist("修改成功")
        self.assertTrue(result)
        time.sleep(2)

    def test_02_modify_pwd(self):
        '''验证修改后的密码能否登录'''
        log.info("验证修改后的密码能否登录")
        tel = get_yaml_value(TEST_ACCOUNT_PATH, 'account_1')
        pwd = get_yaml_value(TEST_ACCOUNT_PATH, 'new_pwd_s')
        lp = LoginPage(self.driver)
        lp.login_opera_again(tel, pwd)
        log.info("登录操作")
        time.sleep(2)
        # 断言是否登录成功
        result = False
        if lp.is_exist_element("立即更新"):
            result = True
            # 有则点击取消
            UpdatePopup(self.driver).cancel_opera()
        elif lp.is_exist_element("首页"):
            result = True
        self.assertTrue(result)
        time.sleep(2)

        # 为不影响后面的测试，需将密码还原成旧密码
        ms = MySet(self.driver)
        ms.enter_to_my()
        ms.enter_to_set()
        # 修改密码操作
        old_pwd = get_yaml_value(TEST_ACCOUNT_PATH, 'new_pwd_s')
        new_pwd = get_yaml_value(TEST_ACCOUNT_PATH, 'old_pwd_s')
        ms.change_pwd(old_pwd, new_pwd)
        time.sleep(2)

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()