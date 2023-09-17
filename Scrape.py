import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.shell import inspect_response
import json

Websites = ["https://google.com"]

class spider(scrapy.Spider):
	DOWNLOAD_DELAY = 1
	ROBOTSTXT_OBEY = True
	name = "spider"
	start_urls = Websites
	user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
	D = {}
	links = []
	def start_requests(self):
		for W in self.start_urls:
			self.D[W] = []
			yield scrapy.Request(W, callback = self.ParseLinks)

	def ParseLinks(self, response):
		Link = response.xpath(".//").extract()
		for W in self.D:
			self.D[W] = Link
			for List in self.links:
				for L in List:
					yield response.follow(L, callback=self.ParseContent)
	
	def ParseContent(self, response):
		Post = response.xpath('//html').xpath().extract()

		with open("Quality central_text.txt",'w+') as file:
			file.write(term+'.txt.')
		
process = CrawlerProcess()
process.crawl(spider)
process.start()
