#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/20
# @Author  : lfr

import time
import sys
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
    login_ele = "登录"
    update_ele = "立即更新"
    cancel_el = 'com.qekj.merchant:id/iv_cancel'
    iknow_ele = "我知道了"
    home_ele = "首页"

    def init_to_home(self):
        '''滑动引导页进入登录页面，登录进入首页'''
        try:
            mobile = get_yaml_value(TEST_ACCOUNT_PATH, 'account_1')
            pwd = get_yaml_value(TEST_ACCOUNT_PATH, 'pwd_1_right')
            StartPage(self.driver).swipe_start()
            lp = LoginPage(self.driver)
            lp.login_opera(mobile, pwd)
            time.sleep(1)
            # 判断是否登录成功
            if lp.is_exist_element(self.update_ele):
                log.info("登录成功，进入首页...")
                self.update_cancel_opera()
                # 判断是否存在通知弹窗
                if lp.is_exist_element(self.cancel_el):
                    self.notice_cancel_opera()
                    # 判断是否存在"知道了"
                    if lp.is_exist_element(self.iknow_ele):
                        self.iknow_click_opera()
                    else:
                        pass
            elif lp.is_exist_element(self.cancel_el):
                log.info("登录成功，进入首页...")
                self.notice_cancel_opera()
            elif lp.is_exist_element(self.iknow_ele):
                log.info("登录成功，进入首页...")
                self.iknow_click_opera()
            elif lp.is_exist_element(self.home_ele):
                log.info("登录成功，进入首页...")
                pass
            else:
                log.error("初始化登录失败，终止自动化程序！！！")
                sys.exit(0)
        except Exception as e:
            log.error("进入首页失败：{}".format(e))

    def update_cancel_opera(self):
        '''判断登录后是否存在非强制更新弹窗，存在则点击取消按钮'''
        # result = self.is_exist_element(self.update_ele)
        # # print(result)
        # if result:
        #     UpdatePopup(self.driver).cancel_opera()
        # else:
        #     pass
        UpdatePopup(self.driver).cancel_opera()

    def notice_cancel_opera(self):
        '''判断是否有通知弹窗，有则点击关闭'''
        # result = self.is_exist_element(self.cancel_el)
        # if result:
        #     UpdatePopup(self.driver).cancel_opera()
        # else:
        #     pass
        UpdatePopup(self.driver).cancel_opera()

    def iknow_click_opera(self):
        '''登录后判断是否存在【我知道了】按钮，存在则点击'''
        # result = self.is_exist_element(self.iknow_ele)
        # # print(result)
        # if result:
        #     Iknow(self.driver).click_iknow_btn()
        # else:
        #     pass
        Iknow(self.driver).click_iknow_btn()

if __name__ == '__main__':
    driver = BaseDriver().android_driver()
    pi = PageInit(driver).init_to_home()