#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/06/29
# @Author  : lfr

import os
import time
from common.base_log import log
from config.path_config import IMEI_PATH, NQT_PATH, SIMULATOR_PHOTO_PATH

class PushSomethingToPhone(object):
    '''
    向测试机或者模拟器指定文件发送文件
    '''
    def __init__(self, something_path_list, phone_path):
        self.something_path_list = something_path_list
        self.phone_path = phone_path

    def is_exist_file(self):
        '''判断文件是否存在'''
        adb_command = 'adb shell ls ' + self.phone_path
        with os.popen(adb_command) as f:
            f_list = f.read().splitlines()
        result = all(file in f_list for file in self.something_path_list)
        return f_list, result

    def judge_exist_file_and_push(self):
        '''判断文件是否存在，不存在则发送文件至目标文件夹'''
        f_list, result = self.is_exist_file()
        if len(f_list) == 2 and result:
            pass
        elif len(f_list) == 0:
            for p in self.something_path_list:
                self.push_to_phone(p)
        else:
            self.rm_target_file()
            for p in self.something_path_list:
                self.push_to_phone(p)

    def rm_target_file(self):
        '''删除目标文件夹里的所有文件'''
        adb_rm_command = 'adb shell rm ' + self.phone_path + '/*'
        os.system(adb_rm_command)
        time.sleep(1)

    def push_to_phone(self, something_path):
        '''发送文件至手机目标文件夹'''
        adb_push_command = 'adb push ' + something_path + ' ' + self.phone_path
        os.system(adb_push_command)
        time.sleep(0.1)

def push_photos_to_phone_or_not():
    something_path_list = [IMEI_PATH, NQT_PATH]
    simulator_phone_path = SIMULATOR_PHOTO_PATH
    pst = PushSomethingToPhone(something_path_list, simulator_phone_path)
    # pst.judge_exist_file_and_push()
    r_bool = pst.is_exist_file()[1]
    return r_bool

if __name__ == '__main__':
    push_photos_to_phone_or_not()


