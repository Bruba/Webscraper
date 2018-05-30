# -*- coding: utf-8 -*-
import scrapy

from ICS_CERT import settings
from ICS_CERT.items import IcsCertItem


class IcsSpider(scrapy.Spider):
	name = "ics"
	allowed_domains = 'https://ics-cert.us-cert.gov'
	start_urls = [
		"https://ics-cert.us-cert.gov/advisories"
	]

	def parse(self, response):
		for link_list in response.xpath('//div[@class="view-content"]/div/ul/li/span[2]/span/a/@href').extract():
			yield scrapy.Request(response.urljoin(link_list), callback=self.parse_results, dont_filter=True)
		next_page = response.xpath('//li[@class="pager-next"]/a[@title="Go to next page"]/@href').extract_first()
		if next_page:
			yield scrapy.Request(response.urljoin(next_page), dont_filter=True)
			
	def parse_results(self, response):
		items = IcsCertItem()
		for sel in response.xpath('//body'):
			id = sel.xpath('.//*[@id="page-title"]/text()').extract_first()
			id = id[id.find('(') + 1:id.find(')')]
			items['id'] = id
			summary = sel.xpath('.//*[@id="page-sub-title"]/text()').extract_first()
			items['summary'] = summary
			field_items = sel.xpath('.//*[@id="ncas-content"]/div/div/div/h3/strong/text()').extract_first()
			items['field_items'] = field_items
			published_date = sel.xpath('.//*[@id="ncas-header"]/footer/text()').extract_first()
			published_date = published_date[published_date.find(':') + 2:]
			items['published_date'] = published_date
			Legal_Notice = sel.xpath('.//*/p/font//text()').extract()
			items['Legal_Notice'] = Legal_Notice
			vendor = sel.xpath('.//*[@id="ncas-content"]/div/div/div/p[1]/text()[normalize-space()]').extract_first()
			items['vendor'] = vendor
			Equipment = sel.xpath('.//*[@id="ncas-content"]/div/div/div/p[2]/text()[normalize-space()]').extract_first()
			items['Equipment'] = Equipment
			Vulnerabilities = sel.xpath('.//*[@id="ncas-content"]/div/div/div/p[3]/text()[normalize-space()]').extract_first()
			items['Vulnerabilities'] = Vulnerabilities
			Affected_Products = sel.xpath('.//*[@id="ncas-content"]/div/div/div/p[4]/text()').extract_first()
			items['Affected_Products'] = Affected_Products
			Impact = sel.xpath('.//*[@id="ncas-content"]/div/div/div/p[5]/text()').extract_first()
			items['Impact'] = Impact
			CVE_Numbers = sel.xpath('//*[@id="ncas-content"]/div//text()[starts-with(.,"CVE")]').extract()
			items['CVE_Numbers'] = CVE_Numbers
			yield items
		