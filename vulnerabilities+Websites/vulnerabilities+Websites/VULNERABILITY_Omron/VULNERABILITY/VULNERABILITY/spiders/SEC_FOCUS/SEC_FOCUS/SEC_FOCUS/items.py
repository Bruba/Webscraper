# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SecFocusItem(scrapy.Item):
	Title = scrapy.Field()
	Bugtraq_ID = scrapy.Field()
	CVE = scrapy.Field()
	Published = scrapy.Field()
	Credit = scrapy.Field()
	Vulnerable = scrapy.Field()