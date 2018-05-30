# -*- coding: utf-8 -*-
import scrapy
# import csv
import re

from CVE_DETAILS import settings
from CVE_DETAILS.items import CveDetailsItem
# from scrapy import signals
# from scrapy.xlib.pydispatch import dispatcher


class CveSpider(scrapy.Spider):
	name = "cve"
	allowed_domains = 'https://www.cvedetails.com'
	start_urls = [
		"https://www.cvedetails.com/vulnerability-list/vendor_id-109/Siemens.html" 
	]

	# CSV_TITLE = [
			# "CVE ID", "CWE ID", "No of Exploits", "Vulnerability Types", "Publish Date", "Update Date", "Score", 
			# "Gained Access Level", "Access", "Complexity", "Authentication", "Conf", "Integ", "Avail", "Summary"
	# ]
			
	# def __init__(self):
		# dispatcher.connect(self.spider_closed, signals.spider_closed)
		# self.csv_file = open("Results.csv", "wb")
		# self.csv_wr = csv.writer(self.csv_file, quoting=csv.QUOTE_ALL)
		# self.csv_wr.writerow(self.CSV_TITLE)
		
	# def spider_closed(self, spider):
		# self.csv_file.close()

	def parse(self, response):
		# item = []
		items = CveDetailsItem()
		for sel in response.xpath('//table[@class="searchresults sortable"]//tr'):
			for CVE_ID in sel.xpath('./td[2]/a/text()').extract():
				items['CVE_ID'] = CVE_ID
			for CWE_ID in sel.xpath('./td[3]/a/text()').extract():
				items['CWE_ID'] = CWE_ID
			for No_of_Exploits in sel.xpath('./td[4]/text()').extract():
				items['No_of_Exploits'] = No_of_Exploits
			for Vulnerability_Types in sel.xpath('./td[5]/text()').extract():
				Vulnerability_Types = re.sub(r'^\s+','',Vulnerability_Types)
				items['Vulnerability_Types'] = Vulnerability_Types
			for Publish_Date in sel.xpath('./td[6]/text()').extract():
				items['Publish_Date'] = Publish_Date
			for Update_Date in sel.xpath('./td[7]/text()').extract():
				items['Update_Date'] = Update_Date
			for Score in sel.xpath('./td[8]/div/text()').extract():
				items['Score'] = Score
			for Gained_Access_Level in sel.xpath('./td[9]/text()').extract():
				items['Gained_Access_Level'] = Gained_Access_Level
			for Access in sel.xpath('./td[10]/text()').extract():
				items['Access'] = Access
			for Complexity in sel.xpath('./td[11]/text()').extract():
				items['Complexity'] = Complexity
			for Authentication in sel.xpath('./td[12]/text()').extract():
				items['Authentication'] = Authentication
			for Conf in sel.xpath('./td[13]/text()').extract():
				items['Conf'] = Conf
			for Integ in sel.xpath('./td[14]/text()').extract():
				items['Integ'] = Integ
			for Avail in sel.xpath('./td[15]/text()').extract():
				items['Avail'] = Avail
			for Summary in sel.xpath('./td[@class="cvesummarylong"]/text()[normalize-space()]').extract():
				Summary = re.sub(r'^\s+','',Summary)
				items['Summary'] = Summary
				
				# item.append(items)
				# self.csv_wr.writerow([CVE_ID, CWE_ID, No_of_Exploits, Vulnerability_Types, Publish_Date, Update_Date, Score, Gained_Access_Level, Access, Complexity, Authentication, Conf, Integ, Avail, Summary])
				yield items