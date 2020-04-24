#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/24
# @Author  : lfr

import time
from appium.webdriver import WebElement
from b_page.my import MyPage
from appium.webdriver.common.mobileby import MobileBy as By

class MyMessage(MyPage):
    '''
    我的-消息页
    '''
    msg_set_loc = (By.ID, 'com.qekj.merchant:id/iv_search_single')
    equipment_alarm_loc = (By.ID, 'com.qekj.merchant:id/rl_msg_set')
    early_warning_switch_loc = (By.XPATH, '//*[@text="投放器液位预警"]/../android.widget.Switch')

    text = "投放器液位预警"
    loc =  '//*[@text={}]/../android.widget.Switch'.format(text)

    def enter_to_message_switch(self):
        '''进入消息设置-设备告警，点击 投放器液位预警'''
        self.msg_set_btn().click()
        self.equipment_alarm_btn().click()
        time.sleep(1)

    def switch_opera(self):
        '''投放器液位预警开关操作'''
        self.early_warning_switch().click()
        time.sleep(1)

    def msg_set_btn(self):
        '''消息中心-设置按钮'''
        msg_ele = self.get_visible_element(self.msg_set_loc)
        return msg_ele

    def equipment_alarm_btn(self):
        '''消息设置页-设备告警选项'''
        msg_ele = self.get_visible_element(self.equipment_alarm_loc)
        return msg_ele

    def early_warning_switch(self):
        '''消息设置页-投放器液位预警开关'''
        msg_ele = self.get_visible_element(self.early_warning_switch_loc)
        return msg_ele