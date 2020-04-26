#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/23
# @Author  : lfr

import time
import unittest
from common.base_driver import BaseDriver
from common.base_log import log
from b_page.my_message import MyMessage
from b_page.page_init import PageInit

class TestMyMessage(unittest.TestCase):
    '''
    我的-消息中心
    '''
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        '''初始化，登录进入首页页面'''
        log.info("-----开始执行用例：消息中心-----")
        self.driver = BaseDriver().android_driver()
        PageInit(self.driver).init_to_home()

    def test_01_my_message(self):
        '''验证消息中心-消息设置-设备告警开关是否正常（默认开启状态）'''
        log.info("验证消息中心-消息设置-设备告警开关是否正常（默认开启状态）")
        # ->我的->消息中心->消息设置（开关页）
        mm = MyMessage(self.driver)
        mm.enter_to_my()
        mm.enter_to_message()
        mm.enter_to_message_switch()
        # 点击关闭投放器液位预警开关，断言开关状态
        mm.switch_opera()
        r_1 = mm.is_exist_element("OFF")
        self.assertTrue(r_1)

        # 再次点击开启投放器液位预警开关
        mm.switch_opera()
        r_2 = mm.is_exist_element("OFF")
        self.assertFalse(r_2)

    def tearDown(self) -> None:
        self.driver.quit()

    @classmethod
    def tearDownClass(cls) -> None:
        pass