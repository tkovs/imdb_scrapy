# -*- coding: utf-8 -*-
import json

from .utils import fix_description, fix_title, check_metascore

class JsonWriterPipeline(object):
	def open_spider(self, spider):
		self.file = open('movies.jl', 'wb')

	def close_spider(self, spider):
		self.file.close()

	def process_item(self, item, spider):
		item['title']       = fix_title(item['title'])
		item['metascore']   = check_metascore(item['metascore'])
		item['description'] = fix_description(item['description'])

		line = json.dumps(dict(item)) + '\n'
		self.file.write(line.encode())
		
		return item