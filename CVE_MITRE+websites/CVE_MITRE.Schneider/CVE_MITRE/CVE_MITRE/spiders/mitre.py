# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import scrapy

from CVE_MITRE import settings
from CVE_MITRE.items import CveMitreItem


class MitreSpider(scrapy.Spider):
	name = "mitre"
	start_urls = [
		"http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=schneider",
	]

	def parse(self, response):
		for list in response.xpath('//*[@id="TableWithRules"]/table//tr/td[1]/a/@href').extract():
			yield scrapy.Request(response.urljoin(list), callback=self.parse_results, dont_filter=True)
			
	def parse_results(self, response):
		items = CveMitreItem()
		for sel in response.xpath('//div[@id="GeneratedTable"]'):
			CVE_ID = sel.xpath('./table//tr[2]/td[1]/h2/text()').extract_first()
			items['CVE_ID'] = CVE_ID
			Description = "".join(sel.xpath('./table//tr[4]/td//text()').extract()).strip()
			items['Description'] = Description
			Assigning_CNA = sel.xpath('./table//tr[9]/td/text()').extract_first()
			items['Assigning_CNA'] = Assigning_CNA
			Date_Entry_Created = sel.xpath('./table//tr[11]/td[1]/b/text()').extract_first()
			items['Date_Entry_Created'] = Date_Entry_Created
			yield items