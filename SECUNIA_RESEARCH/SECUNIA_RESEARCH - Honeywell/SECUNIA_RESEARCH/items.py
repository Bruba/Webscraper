# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SecuniaResearchItem(scrapy.Item):
	Title = scrapy.Field()
	Release_Date = scrapy.Field()
	Last_Update = scrapy.Field()
	CVE_Reference = scrapy.Field()
	Description = scrapy.Field()
	Solution = scrapy.Field()
	Provided_or_Discovered = scrapy.Field()
	Original_Advisory = scrapy.Field()