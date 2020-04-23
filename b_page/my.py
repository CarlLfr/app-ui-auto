#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/22
# @Author  : lfr

import time
from b_page.tab import Tab
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy as By

class MyPage(Tab):
    '''
    我的页面
    '''
    zhinan_loc = (By.ID, 'com.qekj.merchant:id/tv_zhinan')
    message_loc = (By.ID, 'com.qekj.merchant:id/tv_message')
    my_wallet_loc = (By.ID, 'com.qekj.merchant:id/rl_my_wallet')
    mokuaifei_loc = (By.ID, 'com.qekj.merchant:id/rl_mokuaifei')
    contract_loc = (By.ID, 'com.qekj.merchant:id/rl_contract')
    hotline_loc = (By.ID, 'com.qekj.merchant:id/rl_hotline')
    help_loc = (By.ID, 'com.qekj.merchant:id/rl_help')
    set_loc = (By.ID, 'com.qekj.merchant:id/rl_set')

    def enter_to_zhinan(self):
        '''进入指南'''
        self.zhinan_btn().click()
        time.sleep(0.5)

    def enter_to_message(self):
        '''进入消息'''
        self.message_btn().click()
        time.sleep(0.5)

    def enter_to_myWallet(self):
        '''进入我的钱包'''
        self.my_wallet_btn().click()
        time.sleep(0.5)

    def enter_to_mokuaifei(self):
        '''进入模块流量费'''
        self.mokuaifei_btn().click()
        time.sleep(0.5)

    def enter_to_contract(self):
        '''进入联系客服'''
        self.contract_btn().click()
        time.sleep(0.5)

    def enter_to_hotline(self):
        '''进入合作热线'''
        self.hot_line_btn().click()
        time.sleep(0.5)

    def enter_to_help(self):
        '''进入帮助中心'''
        self.help_btn().click()
        time.sleep(0.5)

    def enter_to_set(self):
        '''进入设置页操作'''
        self.set_btn().click()
        time.sleep(0.5)

    def zhinan_btn(self):
        '''指南按钮'''
        my_ele = self.get_visible_element(self.zhinan_loc)
        return my_ele

    def message_btn(self):
        '''信息按钮'''
        my_ele = self.get_visible_element(self.message_loc)
        return my_ele

    def my_wallet_btn(self):
        '''我的钱包'''
        my_ele = self.get_visible_element(self.my_wallet_loc)
        return my_ele

    def mokuaifei_btn(self):
        '''模块流量费'''
        my_ele = self.get_visible_element(self.mokuaifei_loc)
        return my_ele

    def contract_btn(self):
        '''联系客服'''
        my_ele = self.get_visible_element(self.contract_loc)
        return my_ele

    def hot_line_btn(self):
        '''合作热线'''
        my_ele = self.get_visible_element(self.hotline_loc)
        return my_ele

    def help_btn(self):
        '''帮助中心'''
        my_ele = self.get_visible_element(self.help_loc)
        return my_ele

    def set_btn(self):
        '''设置'''
        my_ele = self.get_visible_element(self.set_loc)
        return my_ele