import scrapy
from scrapy import Request
import requests
import shutil
import os


class ImageCrawl(scrapy.Spider):

	name = "instagram"
	allowed_domains = ["https:/www.instagram.com"]

	start_urls = [
		"https://www.instagram.com/choanhsocool"
	]

	def start_requests(self):
		for url in self.start_urls:
			# name = url.split("/")[-1]
			# os.mkdir("image_{}".format(name))
			yield Request(url=url, callback=self.parse)

	def parse(self, response):
		for url in response.css(".Nnq7C.weEfm .v1Nh3 kIKUG._bz0w .a ::attr(href)").getall():
			print(url, end="=============")
