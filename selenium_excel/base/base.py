#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 1:35
# @Author  : Paulson
# @File    : BaseDriver.py
# @Software: PyCharm
# @define  : function
import time

from selenium import webdriver
from util.get_by_local import GetByLocal
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.find_element_by_id('kw').click()
# driver.find_element_by_id('kw').send_keys("selenium")
# driver.find_element_by_id('su').click()


class ActionMethod:
    # def __init__(self, browser=None):
    #     if browser is None:
    #         self.browser = "Chrome"
    #     else:
    #         self.browser = browser
    #     self.driver = None
    #     pass

    def open_browser(self, *args):
        """打开浏览器"""
        # self.driver = None
        browser = args[0]
        print(browser)
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
            
    def get_url(self, *args):
        """打开 url"""
        url = args[0]
        self.driver.get(url)
        
    def get_element(self, *args):
        """定位方式"""
        key = args[0]
        get_by_element = GetByLocal(self.driver)
        element = get_by_element.get_local_element(key)
        return element
    
    def element_send_keys(self, *args):
        """对元素进行输入"""
        
        key, value = args[0], args[1]
        element = self.get_element(key)
        element.send_keys(value)
        
    def click_element(self, *args):
        """点击元素"""
        key = args[0]
        element = self.get_element(key)
        element.click()
        
    def sleep_time(self):
        """等待"""
        time.sleep(3)
        
    def close_browser(self):
        """关闭浏览器"""
        self.driver.quit()
     
     
    