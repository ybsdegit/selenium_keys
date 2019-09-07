#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 1:56
# @Author  : Paulson
# @File    : get_by_local.py
# @Software: PyCharm
# @define  : function

class GetByLocal:
    def __init__(self, driver):
        self.driver = driver
    
    def get_local_element(self, key):
        """
        name=email
        :return:
        """
        by = key.split('=')[0]
        by_value = key.split('=')[1]
        if by == 'id':
            return self.driver.find_element_by_id(by_value)
        elif by == 'name':
            return self.driver.find_element_by_name(by_value)
        elif by == 'className':
            return self.driver.find_element_by_class_name(by_value)
        else:
            return self.driver.find_element_by_xpath(by_value)
        