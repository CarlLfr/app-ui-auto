#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/21
# @Author  : lfr

import time
from appium.webdriver import WebElement
from b_page.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy as By

class Tab(BasePage):
    '''
    tab包含：首页，报表，管理，我的
    '''
    home_loc = (By.XPATH, "//*[@text='首页']")
    report_loc = (By.XPATH, "//*[@text='报表']")
    manage_loc = (By.XPATH, "//*[@text='管理']")
    my_loc = (By.XPATH, "//*[@text='我的']")

    def enter_to_home(self):
        '''进入首页'''
        self.home_tab().click()

    def enter_to_report(self):
        '''进入报表页'''
        self.report_tab().click()

    def enter_to_manage(self):
        '''进入管理页'''
        self.manage_tab().click()

    def enter_to_my(self):
        '''进入我的页'''
        self.my_tab().click()

    def home_tab(self):
        '''首页tab按钮'''
        tab_ele = self.get_visible_element(self.home_loc)
        return tab_ele

    def report_tab(self):
        '''报表tab按钮'''
        tab_ele = self.get_visible_element(self.report_loc)
        return tab_ele

    def manage_tab(self):
        '''报表tab按钮'''
        tab_ele = self.get_visible_element(self.manage_loc)
        return tab_ele

    def my_tab(self):
        '''报表tab按钮'''
        tab_ele = self.get_visible_element(self.my_loc)
        return tab_ele