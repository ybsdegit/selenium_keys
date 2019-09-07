#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 2:11
# @Author  : Paulson
# @File    : opera_excel.py
# @Software: PyCharm
# @define  : function


import xlrd


class OperaExcel:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = '../dataconfig/selenium.xlsx'
        else:
            self.file_path = file_path
        self.excel = self.get_excel()
    
    def get_excel(self):
        tables = xlrd.open_workbook(self.file_path)
        return tables
    
    def get_sheet(self, i=None):
        if i is None:
            i = 0
        sheet_data = self.excel.sheets()[i]
        return sheet_data
    
    def get_lines(self):
        """获取行数"""
        lines = self.get_sheet().nrows
        return lines
    
    def get_cell(self, row, cell):
        """获取单元格内容"""
        data = self.get_sheet().cell(row, cell).value
        return data


if __name__ == '__main__':
    opera = OperaExcel()
    print(opera.get_lines())
    print(opera.get_cell(0, 1))
