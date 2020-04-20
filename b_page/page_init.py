#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/15
# @Author  : lfr

import time
from b_page.basepage import BasePage
from b_page.start_page import StartPage
from b_page.login import LoginPage
from b_page.update_popup import UpdatePopup
from b_page.iknow import Iknow
from common.base_operate import get_yaml_value
from common.base_log import log
from config.path_config import TEST_ACCOUNT_PATH
from common.base_driver import BaseDriver

class PageInit(BasePage):
    '''
    执行用例（登录用例除外）时先滑动引导页进入登录页面，并登录进入首页
    '''
    x_ele = "立即更新"
    iknow_ele = "我知道了"

    def init_to_home(self):
        '''滑动引导页进入登录页面，登录进入首页'''
        try:
            mobile = get_yaml_value(TEST_ACCOUNT_PATH, 'account_1')
            pwd = get_yaml_value(TEST_ACCOUNT_PATH, 'pwd_1_right')
            StartPage(self.driver).swipe_start()
            LoginPage(self.driver).login_opera(mobile, pwd)
            time.sleep(2)

            # 先判断是否有非强制更新弹窗，再判断是否有提示
            self.is_exist_update(self.driver)
            time.sleep(1)
            self.is_exist_iknow(self.driver)
            time.sleep(1)
            log.info("---登录成功，进入首页---")
        except Exception as e:
            log.error("进入首页失败：{}".format(e))

    def is_exist_update(self, driver):
        '''判断登录后是否存在非强制更新弹窗，存在则点击取消按钮'''
        result = self.is_exist_element(self.x_ele)
        print(result)
        if result == True:
            UpdatePopup(driver).cancel_opera()
        else:
            pass

    def is_exist_iknow(self, driver):
        '''登录后判断是否存在【我知道了】按钮，存在则点击'''
        result = self.is_exist_element(self.iknow_ele)
        print(result)
        if result == True:
            Iknow(driver).click_iknow_btn()
        else:
            pass

if __name__ == '__main__':
    driver = BaseDriver().android_driver()
    pi = PageInit(driver).init_to_home()