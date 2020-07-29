#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/15
# @Author  : lfr

import os
import time
from ruamel import yaml
from config.path_config import TEST_ACCOUNT_PATH
from common.base_log import log
from appium.webdriver.common.touch_action import TouchAction


def page_click(x, y):
    '''根据坐标点 点击页面'''
    click_command = 'adb shell input tap ' + str(x) + ' ' + str(y)
    os.system(click_command)

def get_yaml_value(p, k):
    '''获取yaml文件中key对应的值'''
    try:
        with open(p, 'r', encoding='utf-8') as f:
            cont = yaml.load(f.read(), Loader=yaml.RoundTripLoader)
            val = cont[k]
        return val
    except Exception as e:
        log.error("获取{}对应的值失败：{}".format(k, e))

class SwitchElement:
    '''
    元素向上滑动。场景如，新增限时优惠-优惠期开始、优惠期结束
    '''
    def __init__(self, driver, target_ele, reference_ele):
        self.driver = driver
        self.target_ele = target_ele
        self.reference_ele = reference_ele

    def top_left_coordinate(self, ele):
        '''获取元素左上角的坐标'''
        top_left_point = ele.location
        x = top_left_point['x']
        y = top_left_point['y']
        return x, y

    def switch_element_up(self):
        '''向上滑动，滑动距离为目标元素左上角到参考元素左上角的垂直距离'''
        t_x = self.top_left_coordinate(self.target_ele)[0]  # 目标元素左上角横坐标
        t_y = self.top_left_coordinate(self.target_ele)[1]  # 目标元素左上角纵坐标
        r_x = self.top_left_coordinate(self.reference_ele)[0]  # 参考元素左上角横坐标
        r_y = self.top_left_coordinate(self.reference_ele)[1]   # 参考元素左上角纵坐标
        # 滑动后的坐标
        x = t_x
        y = r_y
        time.sleep(1)
        # 滑动目标元素
        TouchAction(self.driver).long_press(self.target_ele, r_x, r_y).move_to(x=x, y=y).release().perform()
        time.sleep(1)


if __name__ == '__main__':
    # page_click(200, 400)
    path = TEST_ACCOUNT_PATH
    print(get_yaml_value(path, 'account_1'))