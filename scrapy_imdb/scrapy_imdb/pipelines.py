# -*- coding: utf-8 -*-
import json
import scrapy

from scrapy.pipelines.images import ImagesPipeline
from .utils                  import fix_item

class JsonWriterPipeline(object):
	def open_spider(self, spider):
		self.file = open('movies.jl', 'wb')

	def close_spider(self, spider):
		self.file.close()

	def process_item(self, item, spider):
		item = fix_item(item)
		line = json.dumps(dict(item)) + '\n'

		self.file.write(line.encode())
		
		return item

class MyImagesPipeline(ImagesPipeline):
	def get_media_requests(self, item, info):
		for image_url in item['image_urls']:
			yield scrapy.Request(image_url, meta={'item': item})

	def file_path(self, request, response = None, info = None):
		item = request.meta['item']
		image_guid = request.url.split('/')[-1]
		
		return 'full/{0}.jpg'.format(item['title'])
