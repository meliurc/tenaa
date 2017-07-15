# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TenaaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()                     # url
    type = scrapy.Field()                    # 设备类型
    brand = scrapy.Field()                   # 品牌
    code = scrapy.Field()                    # code
    model = scrapy.Field()                   # 型号
    price = scrapy.Field()                   # 价格
    alias = scrapy.Field()                   # 别名，有可能就是设备报上来的code
    exposure_date = scrapy.Field()           # 上市日期
    phone_size = scrapy.Field()              # 手机尺寸
    sc_params = scrapy.Field()               # 外屏参数
    sc_resolution = scrapy.Field()           # 屏幕分辨率
    sc_size = scrapy.Field()                 # 屏幕尺寸
    cpu_model = scrapy.Field()               # cpu型号
    cpu_cnt = scrapy.Field()                 # cpu核心数
    cpuhz = scrapy.Field()                   # cpu主频
    ram = scrapy.Field()                     # RAM容量
    rom = scrapy.Field()                     # ROM容量
    batt = scrapy.Field()                    # 电池容量
    bk_resolution = scrapy.Field()           # 后置摄像头分辨率
    fr_resolution = scrapy.Field()           # 前置摄像头分辨率
    network = scrapy.Field()                 # 网络制式
    gyro = scrapy.Field()                    # 是否有陀螺仪
    nfc = scrapy.Field()                     # 是否有NFC
    fingerprint = scrapy.Field()             # 是否有指纹识别
    ps_screen = scrapy.Field()               # 是否是压力屏
    fast_charge = scrapy.Field()             # 是否有快速充电功能
    pass
