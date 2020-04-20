#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/20
# @Author  : lfr

from b_page.basepage import BasePage
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy as By

class Iknow(BasePage):
    '''
    第一次安装App登录进入首页后的提示页面“我知道了”
    '''
    iknow_loc = (By.ID, 'com.qekj.merchant:id/ll_iknow')

    def click_iknow_btn(self):
        '''点击我知道了'''
        self.iknow_btn().click()

    def iknow_btn(self):
        '''“我知道了”按钮'''
        iknow_ele = self.get_visible_element(self.iknow_loc)
        return iknow_ele