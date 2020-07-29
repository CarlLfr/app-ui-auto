#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/05/20
# @Author  : lfr

import os

def remove_file(d_path):
    '''删除指定文件夹下所有的文件，.gitkeep除外'''
    file_list = os.listdir(d_path)
    for f in file_list:
        if f != '.gitkeep':
            file_path = os.path.join(d_path, f)
            # print(file_path)
            rm_command = 'rm -rf '+file_path
            os.system(rm_command)

if __name__ == '__main__':
    # 删除当天日志文件
    file_path = '/android_app_ui_autotest/qiekj-app-ui-autotest/log/'
    remove_file(file_path)
