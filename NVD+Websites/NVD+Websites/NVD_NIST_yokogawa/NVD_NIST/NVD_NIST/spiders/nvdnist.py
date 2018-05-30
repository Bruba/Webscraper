# -*- coding: utf-8 -*-
import scrapy

from NVD_NIST import settings
from NVD_NIST.items import NvdNistItem

class NvdnistSpider(scrapy.Spider):
	name = "nvdnist"
	start_urls = [
        "https://nvd.nist.gov/vuln/search/results?adv_search=false&form_type=basic&results_type=overview&search_type=all&query=yokogawa"
	]

	def parse(self, response):
		items = NvdNistItem()
		for sel in response.xpath('//table[@class="table table-striped table-hover"]//tr'):
			CVSS_Severity = sel.xpath('./td[2]/span//text()').extract()
			items['CVSS_Severity'] = CVSS_Severity
			for id in sel.xpath('./th/strong/a/text()').extract():
				items['id'] = id
			for summary in sel.xpath('./td/p/text()').extract():
				items['summary'] = summary
			for Date in sel.xpath('./td/span[@data-testid="vuln-published-on-1"]/text()').extract():
				items['Date'] = Date
				yield items
		next_page = response.xpath('//ul[@class="pagination"]/li/a[@aria-label="Next Page"]/@href').extract_first()
		if next_page:
			yield scrapy.Request(response.urljoin(next_page), dont_filter=True)