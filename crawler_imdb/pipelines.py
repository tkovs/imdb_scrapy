import json
import scrapy

from scrapy.pipelines.images import ImagesPipeline
from itemadapter import ItemAdapter
from .utils import polishes_item

class JsonPipeline:
  def open_spider(self, spider):
    self.file = open('items.jl', 'w')

  def close_spider(self, spider):
    self.file.close()

  def process_item(self, item, spider):
    polished_item = polishes_item(item)
    line = json.dumps(dict(polished_item)) + '\n'
    self.file.write(line)
    return item

class ImagesPipeline(ImagesPipeline):
	def get_media_requests(self, item, info):
		for image_url in item['image_urls']:
			yield scrapy.Request(image_url, meta={'item': item})

	def file_path(self, request, response = None, info = None):
		item = request.meta['item']
		image_guid = request.url.split('/')[-1]
		
		return '{0}.jpg'.format(item['title'])