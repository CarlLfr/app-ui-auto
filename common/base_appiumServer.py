#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/21
# @Author  : lfr

import os
import time
from common.base_log import log

class AppiumServer:
    '''
    启动、停止appium服务
    '''
    def check_port(self):
        pass

    def start_appium(self):
        '''启动appium服务'''
        try:
            os.system('start appium -a 127.0.0.1 -p 4723')
            time.sleep(5)
            log.info("启动appium服务...")
        except Exception as e:
            log.error("appium启动失败：{}".format(e))

    def quit_appium(self):
        '''停止appium服务'''
        process = os.popen('netstat -aon |findstr 4723').read()
        print(process)
        pid = process.replace(' ', '').split('LISTENING')[1]
        m = os.popen('taskkill -f -pid %s' % pid)
        # print(m.read())
        log.info("appium服务已停止...")

if __name__ == '__main__':
    ap = AppiumServer()
    ap.start_appium()
    time.sleep(10)
    ap.quit_appium()