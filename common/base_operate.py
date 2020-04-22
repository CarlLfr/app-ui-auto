#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/15
# @Author  : lfr

import os
from ruamel import yaml
from config.path_config import TEST_ACCOUNT_PATH
from common.base_log import log


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

if __name__ == '__main__':
    # page_click(200, 400)
    path = TEST_ACCOUNT_PATH
    print(get_yaml_value(path, 'account_1'))