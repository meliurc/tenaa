# -*- coding: utf-8 -*-
import re
import time
import scrapy
from selenium import webdriver
from tenaa.items import TenaaItem

class TenaaSpider2(scrapy.Spider):
    name = 'tenaa2'
    start_urls = ['http://shouji.tenaa.com.cn/mobile/mobileindex.aspx']

    def parse(self, response):
        pass


class TenaaSpider(scrapy.Spider):
    name = 'tenaa'
    start_urls = ['http://shouji.tenaa.com.cn/mobile/mobileindex.aspx']
    outer_driver = webdriver.PhantomJS(executable_path=r'C:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    inner_driver = webdriver.PhantomJS(executable_path=r'C:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe')

    def parse(self, response):
        print self.parse.__name__
        self.outer_driver.get(response.url)

        # click button '查询符合条件的机型'
        elem = self.outer_driver.find_element_by_xpath('//*[@id="Table3"]/tbody/tr[5]/td[2]/img')
        elem.click()
        time.sleep(5)
        body = self.outer_driver.execute_script("return document.documentElement.outerHTML;")

        # 生成request，把driver也传递过去
        request = scrapy.Request(self.start_urls[0], self.get_items, dont_filter=True)
        request.meta['body'] = body
        yield request

    def get_items(self, response):
        print self.get_items.__name__

        response = response.replace(body=response.meta['body'])
        # get phone url list
        href_list = response.xpath('//div[@id="showMobile"]//td[@width="152"]//td[@align="center"]//@href').extract()
        for href in href_list[:2]:
            url = response.urljoin(href)
            print url
            request = scrapy.Request(url, self.parse_detail_page, dont_filter=True)
            yield request

        if self.has_next_page(response):
            yield self.click_next_page(response)

    def has_next_page(self, response):
        pattern = re.compile('\d+')
        now_page = response.xpath('//span[@id="nowPage"]//text()').extract()[0]
        now_page_num = int(re.findall(pattern, now_page)[0])
        total_page = response.xpath('//span[@id="allPage"]//text()').extract()[0]
        total_page_num = int(re.findall(pattern, total_page)[0])
        print now_page_num, total_page_num
        if now_page_num < total_page_num:
            return True
        else:
            return False

    def click_next_page(self, response):
        # click next page
        elem = self.outer_driver.find_element_by_xpath('//*[@id="Table15"]/tbody/tr/td[5]/table/tbody/tr[2]/td/img')
        elem.click()
        time.sleep(5)
        body = self.outer_driver.execute_script("return document.documentElement.outerHTML;")

        # call get_item function
        request = scrapy.Request(self.start_urls[0], self.get_items, dont_filter=True)
        request.meta['body'] = body
        return request

    def parse_detail_page(self, response):
        print self.parse_detail_page.__name__

        # parse detail page
        item = TenaaItem()
        item['brand'] = response.xpath('//span[@id="lblPP"]/text()').extract()[0]
        item['code'] = response.xpath('//span[@id="lblXH"]/text()').extract()[0]
        item['phone_size'] = response.xpath(u'//td[text()="机身尺寸"]/following-sibling::td/text()').extract()[0]
        item['sc_params'] = response.xpath(u'//td[text()="外屏参数"]/following-sibling::td/text()').extract()[0]
        item['network'] = response.xpath(u'//td[text()="手机制式"]/following-sibling::td/text()').extract()[0]
        item['batt'] = response.xpath(u'//td[text()="电池额定容量"]/following-sibling::td/text()').extract()[0]

        # click '高级功能' tab and call parse features
        response = self.click_features_tab(response)
        return self.parse_features_tab(response, item)

    def click_features_tab(self, response):
        print self.click_features_tab.__name__
        self.inner_driver.get(response.url)

        elem = self.inner_driver.find_element_by_xpath('//img[@id="Senior"]')
        elem.click()
        time.sleep(5)
        body = self.inner_driver.execute_script("return document.documentElement.outerHTML;")
        return response.replace(body=body)

    def parse_features_tab(self, response, item):
        print self.parse_features_tab.__name__

        # parse advanced features page
        item['cpuhz'] = response.xpath(u'//td[text()="CPU主频"]/following-sibling::td/text()').extract()[0]
        item['ram'] = response.xpath(u'//td[text()="RAM内存容量"]/following-sibling::td/text()').extract()[0]
        item['rom'] = response.xpath(u'//td[text()="手机内存"]/following-sibling::td/text()').extract()[0]
        item['cpu_cnt'] = response.xpath(u'//td[text()="CPU内核数"]/following-sibling::td/text()').extract()[0]

        # reset inner_driver and yield item
        self.inner_driver = webdriver.PhantomJS(
            executable_path=r'C:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        yield item








