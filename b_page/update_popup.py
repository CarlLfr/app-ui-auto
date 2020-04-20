#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/16
# @Author  : lfr

from b_page.basepage import BasePage
from b_page.login import LoginPage
from b_page.start_page import StartPage
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy as By
from common.base_driver import BaseDriver

class UpdatePopup(BasePage):
    '''版本更新弹窗'''
    update_loc = (By.ID, 'com.qekj.merchant:id/ll_update')
    cancel_loc = (By.ID, 'com.qekj.merchant:id/iv_cancel')

    def update_opera(self):
        '''更新版本'''
        return self.update_btn().click()

    def cancel_opera(self):
        '''取消更新'''
        return self.cancel_btn().click()

    def update_btn(self)->WebElement:
        '''立即更新按钮'''
        upd_ele = self.driver.get_visible_element(self.update_loc)
        return upd_ele

    def cancel_btn(self)->WebElement:
        '''取消更新按钮'''
        upd_ele = self.driver.get_visible_element(self.cancel_loc)
        return upd_ele

if __name__ == '__main__':
    driver = BaseDriver().android_driver()
    StartPage(driver).swipe_start()
    LoginPage(driver).login_opera('18768124236', '123456')
    UpdatePopup(driver).cancel_opera()