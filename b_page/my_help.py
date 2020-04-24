#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/23
# @Author  : lfr

import time
from appium.webdriver import WebElement
from b_page.my import MyPage
from appium.webdriver.common.mobileby import MobileBy as By

class MyHelp(MyPage):
    '''
    联系客服，合作热线，帮助中心
    '''
    # 联系客服
    ask_text = "提现到账时间"
    answer_text = "目前商户提现一般为24小时内到账，特殊情况48小时内到账。"

    # 合作热线
    hotline_text = "服务热线："

    # 帮助中心
    problem_text = "模块指示灯识别办法"
    help_back_loc = (By.ID, "com.qekj.merchant:id/ll_back")


    def contract_opera(self):
        '''联系客服操作'''
        self.ask_btn().click()
        time.sleep(2)

    def ask_btn(self):
        '''联系客服-问题-体现到账时间'''
        my_ele = self.get_text_element(self.ask_text)
        return my_ele



    def hot_line(self):
        '''合作热线页面-"服务热线："text'''
        my_ele = self.get_text_element(self.hotline_text)
        return my_ele



    def help_opera(self):
        '''帮助中心操作 点击 模块指示灯识别办法'''
        self.problem_btn().click()
        time.sleep(2)

    def help_back_opera(self):
        '''帮助中心点击返回我的操作'''
        self.help_back_btn().click()
        time.sleep(1)

    def problem_btn(self):
        '''帮助中心-问题'''
        my_ele = self.get_text_element(self.problem_text)
        return my_ele

    def help_back_btn(self):
        '''帮助中心-返回按钮'''
        my_ele = self.get_visible_element(self.help_back_loc)
        return my_ele
