#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/04/15
# @Author  : lfr

import os
import sys
import inspect

class GetCurrentItems:
    '''
    获取当前文件路径、当前文件名、当前类名、当前函数名、当前所在行数
    '''
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance

    def __init__(self):
        pass

    @staticmethod
    def get_current_file_path():
        '''返回当前文件路径'''
        return __file__

    @staticmethod
    def get_current_file_name():
        '''返回当前文件名'''
        return os.path.split(__file__)[-1]

    def get_current_class_name(self):
        '''返回当前正在运行的类名'''
        return self.__class__.__name__

    @staticmethod
    def get_current_function_name():
        '''返回当前正在运行的函数名'''
        return inspect.stack()[1][3]

    @staticmethod
    def get_current_lineno():
        '''返回当前正在运行所在行号'''
        return sys._getframe().f_lineno

p = GetCurrentItems()

if __name__ == '__main__':
    print(p.get_current_file_path())
    # print(p.get_current_lineno())