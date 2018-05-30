# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CveDetailsItem(scrapy.Item):
    CVE_ID = scrapy.Field()
    CWE_ID = scrapy.Field()
    No_of_Exploits = scrapy.Field()
    Vulnerability_Types = scrapy.Field()
    Publish_Date = scrapy.Field()
    Update_Date = scrapy.Field()
    Score = scrapy.Field()
    Gained_Access_Level = scrapy.Field()
    Access = scrapy.Field()
    Complexity = scrapy.Field()
    Authentication = scrapy.Field()
    Conf = scrapy.Field()
    Integ = scrapy.Field()
    Avail = scrapy.Field()
    Summary = scrapy.Field()