#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/17
# @Author  : lfr

import time
from b_page.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy as By
from common.base_driver import BaseDriver

class StartPage(BasePage):
    '''
    启动页
    '''
    open_loc = (By.ID, 'com.qekj.merchant:id/btn_open')

    def swipe_start(self):
        '''滑动引导页，进入登录页'''
        for i in range(2):
            time.sleep(2)
            self.swipe_to_left()

        self.open_btn().click()
        time.sleep(2)

    def open_btn(self):
        '''立即进入按钮'''
        return self.get_presence_element(self.open_loc)

if __name__ == '__main__':
    driver  = BaseDriver().android_driver()
    StartPage(driver).swipe_start()