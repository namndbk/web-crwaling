import scrapy
from ..items import ImagecrawlItem
from scrapy.loader import ItemLoader
import shutil
from scrapy import Request
import wget
import os
import requests

class ImageCrawl(scrapy.Spider):

	name = "image"
	allowed_domains = ["https://www.jkforum.net/forum.php"]
	start_urls = [
		# "https://www.jkforum.net/thread-11304778-1-1.html?fbclid=IwAR0Y3L2FJpAuZMxZ06MfrpinkDCCjI7_8RuoCzRlDJAghY3AwbBgQ33Tu1Y",
		# "https://www.jkforum.net/thread-11886891-1-1.html"
		"https://www.jkforum.net/thread-11867343-1-1.html",
		"https://www.jkforum.net/thread-11304778-1-1.html",
	]
	count = 0

	def start_requests(self):
		for i, url in enumerate(self.start_urls):
			os.mkdir("images_{}".format(i + 1))
			yield Request(url=url, callback=self.parse)


	def parse(self, response):
		for url in response.xpath('//td[@class="t_f"]/ignore_js_op/img/@file').extract():
			self.count += 1
			path = "images_1"
			if self.count > 100:
				path = "images_2"
			resp = requests.get(url, stream=True)
			local_file = open(path + "/{}.jpg".format(str(self.count)), "wb")
			resp.raw.decode_content = True
			shutil.copyfileobj(resp.raw, local_file)
			del resp
			# wget.download(url)
			
