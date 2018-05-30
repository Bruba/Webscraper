# -*- coding: utf-8 -*-
import scrapy
# import csv
# import os
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

from AUSCERT import settings
from AUSCERT.items import AuscertItem
# from scrapy import signals
# from scrapy.xlib.pydispatch import dispatcher


class AuscertSpider(scrapy.Spider):
	name = "auscert"
	allowed_domains = 'https://www.auscert.org.au'
	start_urls = [
		"https://www.auscert.org.au/search?q=siemens&order=score"
	]

	# CSV_TITLE = ["ID", "Date", "Summary"]
			
	# def __init__(self):
		# dispatcher.connect(self.spider_closed, signals.spider_closed)
		# self.csv_file = open("Results.csv", "wb")
		# self.csv_wr = csv.writer(self.csv_file, quoting=csv.QUOTE_ALL)
		# self.csv_wr.writerow(self.CSV_TITLE)
		
	# def spider_closed(self, spider):
		# self.csv_file.close()

	def parse(self, response):	
		# item = []
		items = AuscertItem()
		for sel in response.xpath('//div[@class="col-md-9"]/ul/li'):
			id = sel.xpath('./a/text()').extract_first()
			items['id'] = id
			date = sel.xpath('./span[@class="badge"]/text()').extract_first()
			items['date'] = date
			summary = " ".join(sel.xpath('./small//text()').extract()).strip()
			items['summary'] = summary
				
			# item.append(items)
			# self.csv_wr.writerow([id, date, summary])
			yield items
		next_page = response.xpath('//*[@id="next_link"]/@href').extract_first()
		if next_page:
			yield scrapy.Request(response.urljoin(next_page), dont_filter=True)