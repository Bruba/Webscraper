# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CveMitreItem(scrapy.Item):
	CVE_ID = scrapy.Field()
	Description = scrapy.Field()
	Assigning_CNA = scrapy.Field()
	Date_Entry_Created = scrapy.Field()
