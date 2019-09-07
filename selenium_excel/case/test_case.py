#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 2:13
# @Author  : Paulson
# @File    : test_case.py
# @Software: PyCharm
# @define  : function
# import sys
# sys.path.append(r"C:\Users\ybsde\PycharmProjects\Life_Process_Study\StudyPacticePython\selenium_pageObject\selenium_excel")

from util.opera_excel import OperaExcel
from base.base import ActionMethod


class TestCase:
    def __init__(self):
        self.handle_excel = OperaExcel()
        self.action_method = ActionMethod()
        
    def run_main(self):
        
        case_lines = self.handle_excel.get_lines()
        for i in range(1, case_lines):
            is_run = self.handle_excel.get_cell(i, 2)
            if is_run == "yes":
                case_num = self.handle_excel.get_cell(i, 0)
                print(f"开始测试: {case_num}")
                method = self.handle_excel.get_cell(i, 3)
                handle_value = self.handle_excel.get_cell(i, 4)
                send_value = self.handle_excel.get_cell(i, 5)
                # print(method, handle_value, send_value)
                if send_value == '':
                    if handle_value == '':
                        self.run_method(method)
                    else:
                        self.run_method(method, handle_value)
                else:
                    self.run_method(method, handle_value, send_value)

    def run_method(self, method, handle_value=None, send_value=None):
        """反射机制"""
        # print(method, handle_value, send_value)
        action_function = getattr(self.action_method, method)
        if send_value is None:
            if handle_value is None:
                action_function()
            else:
                action_function(handle_value)
        else:
            action_function(handle_value, send_value)
        
            
if __name__ == '__main__':
    test = TestCase()
    test.run_main()
