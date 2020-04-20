#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/15
# @Author  : lfr

import os
import time
from config.path_config import REPORT_PATH

def report_path():
    reportPath = os.path.join(REPORT_PATH, '{}_test_report'.format(time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))))
    return reportPath

if __name__ == '__main__':
    print(report_path())