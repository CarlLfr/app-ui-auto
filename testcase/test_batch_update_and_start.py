#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/06/23
# @Author  : lfr

import pytest
import unittest
from common.base_driver import BaseDriver
from common.base_log import log
from b_page.base_manage_device_management import DeviceManagement
from b_page.page_init import PageInit

class TestDevicesManagement(unittest.TestCase):
    '''
    基础管理，设备管理-批量修改、批量启动
    '''
    @classmethod
    def setUpClass(cls) -> None:
        '''初始化，登录进入首页'''
        log.info("-----开始执行用例：批量修改、批量启动设备-----")
        cls.driver = BaseDriver().android_driver()
        PageInit(cls.driver).init_to_home()

    def setUp(self) -> None:
        pass

    # @unittest.skip("调试，跳过")
    def test_01_batch_update_devices(self):
        '''验证批量修改设备'''
        log.info("验证批量修改设备")
        # ->全部应用->设备管理
        dm = DeviceManagement(self.driver)
        dm.enter_to_all_applications()
        dm.enter_to_devices_management()
        # 批量修改操作
        dm.batch_update_opera()
        # 断言是否修改成功
        toast_text = dm.get_toast_text()
        self.assertEqual(toast_text, dm.batch_update_success_toast)

    def test_02_batch_start_devices(self):
        '''验证批量启动设备'''
        log.info("验证批量启动设备")
        dm = DeviceManagement(self.driver)
        # 批量启动操作
        dm.batch_start_opera()
        # 断言是否操作成功
        toast_text = dm.get_toast_text()
        self.assertEqual(toast_text, dm.batch_start_success_toast)

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()