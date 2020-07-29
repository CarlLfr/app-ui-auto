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
    基础管理，设备管理-新增、编辑、删除
    '''
    @classmethod
    def setUpClass(cls) -> None:
        '''初始化，登录进入首页'''
        log.info("-----开始执行用例：新增、编辑、删除设备-----")
        cls.driver = BaseDriver().android_driver()
        PageInit(cls.driver).init_to_home()

    def setUp(self) -> None:
        pass

    # @unittest.skip("调试跳过")
    def test_01_add_device(self):
        '''验证新增设备'''
        log.info("验证新增设备")
        # ->全部应用->设备管理
        dm = DeviceManagement(self.driver)
        dm.enter_to_all_applications()
        dm.enter_to_devices_management()
        # 新增设备操作
        dm.add_device_opera()
        # 断言新增是否成功
        toast_text = dm.get_toast_text()
        self.assertEqual(toast_text, dm.add_success_toast)

    # @unittest.skip("脚本调试跳过")
    def test_02_search_edit_device(self):
        '''验证搜索设备、编辑设备'''
        log.info("验证搜索设备、编辑设备")
        # 搜索、编辑设备操作
        dm = DeviceManagement(self.driver)
        dm.search_edit_device_opera()
        # 断言是否编辑成功
        toast_text = dm.get_toast_text()
        self.assertEqual(toast_text, dm.edit_success_toast)

    # @unittest.skip("脚本调试跳过")
    def test_03_senior_set(self):
        '''验证设备详情页-高级设置'''
        log.info("验证设备详情页-高级设置")
        # 高级设置操作
        dm = DeviceManagement(self.driver)
        dm.senior_set_opera()
        # 断言是否设置成功
        toast_text = dm.get_toast_text()
        self.assertEqual(toast_text, dm.set_success_toast)

    def test_04_delete_device(self):
        '''验证删除设备'''
        log.info("验证删除设备")
        dm = DeviceManagement(self.driver)
        # 删除操作
        dm.delete_device_opera()
        # 断言是否删除成功
        # result = dm.is_exist_element(dm.device_manage_title)
        # self.assertTrue(result)
        toast_text = dm.get_toast_text()
        self.assertEqual(toast_text, dm.delete_success_toast)


    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()