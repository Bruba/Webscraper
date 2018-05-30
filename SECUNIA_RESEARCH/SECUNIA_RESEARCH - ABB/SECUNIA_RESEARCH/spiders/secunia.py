# -*- coding: utf-8 -*-
import scrapy
import time
import re

from SECUNIA_RESEARCH import settings
from SECUNIA_RESEARCH.items import SecuniaResearchItem

from selenium import webdriver

class SecuniaSpider(scrapy.Spider):
	name = "secunia"
	start_urls = [
		"https://secuniaresearch.flexerasoftware.com/community/advisories/search/?search=ABB"
	]
	
	def __init__(self, *args, **kwargs):
		self.driver = webdriver.PhantomJS()	
	
	def parse(self, response):
		self.driver.get(response.url)
		login = self.driver.find_element_by_xpath('//*[@id="move-content"]/div[4]/div/div/p[1]/a').click()
		time.sleep(5)
		user_id = self.driver.find_element_by_xpath('//*[@id="sLoginUsername"]').send_keys('scrapy')
		password = self.driver.find_element_by_xpath('/html/body/div/div[1]/form/div/table//tr[2]/td[2]/input').send_keys('scrapymailnow')
		submit = self.driver.find_element_by_xpath('/html/body/div/div[1]/form/div/table//tr[4]/td[2]/input[1]').click()
		time.sleep(6)
		for repeat in range(1, 6):
			for i in range(1, 26):
				Release_Date = self.driver.find_element_by_xpath('//tr[@bgcolor="#FFFFFF"][' + str(i) + ']/td[2]/span').get_attribute('textContent')
				list_links = self.driver.find_element_by_xpath('//tr[@bgcolor="#FFFFFF"][' + str(i) + ']/td[1]/span/a').click()
				time.sleep(4)
				items = SecuniaResearchItem()
				Full = self.driver.find_element_by_xpath('//*[@id="move-content"]/div[6]/div/div ').text
				Title = self.driver.find_element_by_xpath('//*[@id="move-content"]/div[6]/div/div/div[1]/div[1]/h1').get_attribute('textContent')
				items['Title'] = Title
				items['Release_Date'] = Release_Date
				Last_Update = re.findall(r'\d\d\d\d\-\d\d\-\d\d(\d\d\d\d\-\d\d\-\d\d)',Full)
				items['Last_Update'] = Last_Update
				CVE_Reference = Full[Full.find('CVE Reference(s):') + 18:Full.find('Desc')]
				items['CVE_Reference'] = CVE_Reference
				Description = self.driver.find_element_by_xpath('//*[@id="move-content"]/div[6]/div/div/div[2]/div/p').get_attribute('textContent')
				items['Description'] = Description
				Solution = re.findall(r'Solution:\n(.*)',Full)
				items['Solution'] = Solution
				Provided_or_Discovered = re.findall(r'Provided and/or discovered by:\n(.*)',Full)
				items['Provided_or_Discovered'] = Provided_or_Discovered
				Original_Advisory = re.findall(r'Original Advisory:\n(.*)',Full)
				items['Original_Advisory'] = Original_Advisory
				yield items
				self.driver.back()
			next_page = self.driver.find_element_by_xpath('//*[@id="move-content"]/div[4]/div/div/div/table//tr[56]/td/a[contains(.,"Next")]')
			if next_page:
				next_page.click()
				time.sleep(4)