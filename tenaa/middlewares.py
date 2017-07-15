# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from scrapy.http import HtmlResponse

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class TenaaSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    outer_driver = webdriver.PhantomJS(executable_path=r'C:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe')


    def process_request(self, request, spider):
        self.outer_driver.get(request.url)

        # click button '查询符合条件的机型'
        elem = self.outer_driver.find_element_by_xpath('//*[@id="Table3"]/tbody/tr[5]/td[2]/img')


