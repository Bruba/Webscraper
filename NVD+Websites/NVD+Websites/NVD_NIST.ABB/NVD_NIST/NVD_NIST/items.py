# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NvdNistItem(scrapy.Item):
    id = scrapy.Field()
    summary = scrapy.Field()
    CVSS_Severity = scrapy.Field()
    Date = scrapy.Field()