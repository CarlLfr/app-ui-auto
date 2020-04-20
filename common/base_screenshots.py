#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/15
# @Author  : lfr

import os
import time
from config.path_config import SCREENSHOTS_PATH
from common.base_tools import p

class Screenshots:
    '''
    封装截图并保存方法
    '''
    def __init__(self, driver, screenshotsName):
        self.driver = driver
        self.screenshotsName = screenshotsName

    def screen_shot(self):
        '''截图并保存方法'''
        dir_path = self.make_dir()
        tm = self.get_time()
        path = dir_path + '/' + tm + self.screenshotsName + '.png'
        self.driver.get_screenshot_as_file(path)

    def get_day(self):
        '''获取当前时间戳'''
        day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        return day

    def get_time(self):
        tm = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
        return tm

    def make_dir(self):
        '''获取文件夹路径，不存在则创建'''
        day = self.get_day()
        dir_path = SCREENSHOTS_PATH + day
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        return dir_path

if __name__ == '__main__':
    pass