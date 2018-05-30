# -*- coding: utf-8 -*-
import scrapy

from SEC_FOCUS import settings
from SEC_FOCUS.items import SecFocusItem

class SecSpider(scrapy.Spider):
	name = "sec"
	start_urls = [
		"https://www.securityfocus.com/bid"
	]

	def parse(self, response):
		for list in response.xpath('//div[@style="padding: 4px;"]/a[position() mod 2 = 1]/@href').extract():
			yield scrapy.Request(response.urljoin(list), callback=self.parse_results, dont_filter=True)
		next_page = response.xpath('//*[@id="articleTools"]/span[2]/a[contains(.,"Next")]/@href').extract_first()
		if next_page:
			yield scrapy.Request(response.urljoin(next_page), callback=self.parse, dont_filter=True)
			
	def parse_results(self, response):
		items = SecFocusItem()
		for sel in response.xpath('//div[@id="vulnerability"]'):
			Title = sel.xpath('./span[@class="title"]/text()').extract_first()
			items['Title'] = Title
			Bugtraq_ID = "".join(sel.xpath('./table//tr[1]/td[2]/text()').extract()).strip()
			items['Bugtraq_ID'] = Bugtraq_ID
			CVE = "".join(sel.xpath('./table//tr[3]/td[2]/text()').extract()).strip()
			items['CVE'] = "".join(CVE).strip()
			Published = "".join(sel.xpath('./table//tr[6]/td[2]/text()').extract()).strip()
			items['Published'] = Published
			Credit = "".join(sel.xpath('./table//tr[8]/td[2]/text()').extract()).strip()
			items['Credit'] = Credit
			Vulnerable = "".join(sel.xpath('./table//tr[9]/td[2]/text()[1]').extract()).strip()
			items['Vulnerable'] =  Vulnerable
			yield items