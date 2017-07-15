# -*- coding: utf-8 -*-

# Scrapy settings for tenaa project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tenaa'

SPIDER_MODULES = ['tenaa.spiders']
NEWSPIDER_MODULE = 'tenaa.spiders'
LOG_LEVEL = 'INFO'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tenaa (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'tenaa.middlewares.TenaaSpiderMiddleware': 500,
}