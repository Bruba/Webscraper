# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IcsCertItem(scrapy.Item):
    id = scrapy.Field()
    summary = scrapy.Field()
    field_items = scrapy.Field()
    published_date = scrapy.Field()
    Legal_Notice = scrapy.Field()
    vendor = scrapy.Field()
    Equipment = scrapy.Field()
    Vulnerabilities = scrapy.Field()
    Affected_Products = scrapy.Field()
    Impact = scrapy.Field()
    CVE_Numbers = scrapy.Field()