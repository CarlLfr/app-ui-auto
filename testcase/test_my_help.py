#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/23
# @Author  : lfr

import time
import unittest
from common.base_driver import BaseDriver
from common.base_log import log
from b_page.my_help import MyHelp
from b_page.page_init import PageInit

class TestHelp(unittest.TestCase):
    '''
    验证联系客服、合作热线、帮助中心
    '''
    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        '''初始化，登录进入首页'''
        log.info("-----开始执行用例：联系客服，合作热线，帮助中心-----")
        self.driver = BaseDriver().android_driver()
        PageInit(self.driver).init_to_home()

    # @unittest.skip("脚本调试，跳过")
    def test_01_contract_kefu(self):
        '''验证联系客服，咨询提现到账时间'''
        log.info("验证联系客服，咨询提现到账时间")
        # ->我的->联系客服
        mh = MyHelp(self.driver)
        mh.enter_to_my()
        mh.enter_to_contract()

        # 点击问题验证
        mh.contract_opera()
        result = mh.new_is_exist_element(mh.answer_text)
        self.assertTrue(result)

    # @unittest.skip("跳过")
    def test_02_hotline(self):
        '''验证合作热线页面展示'''
        log.info("验证合作热线页面展示")
        # ->我的->合作热线
        mh = MyHelp(self.driver)
        mh.enter_to_my()
        mh.enter_to_hotline()

        # 断言页面是否有"服务热线："字样
        result = mh.new_is_exist_element("服务热线：")
        self.assertTrue(result)

    # @unittest.skip("脚本调试，跳过")
    def test_03_help_center(self):
        '''验证帮助中心，查看模块指示灯识别办法'''
        log.info("验证帮助中心，查看模块指示灯识别办法")
        # ->我的->帮助中心
        mh = MyHelp(self.driver)
        mh.enter_to_my()
        mh.enter_to_help()

        # 点击问题验证
        mh.help_opera()
        result = mh.new_is_exist_element("黄色灯：为信号指示灯")
        self.assertTrue(result)

    def tearDown(self) -> None:
        self.driver.quit()

    @classmethod
    def tearDownClass(cls) -> None:
        pass