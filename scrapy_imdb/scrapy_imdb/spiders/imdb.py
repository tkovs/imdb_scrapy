# -*- coding: utf-8 -*-

import scrapy

from scrapy_imdb.items import MovieItem

class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['http://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth_1',]

    def parse(self, response):
        for movie in response.css('div.list_item'):
            item = MovieItem()

            item['title']       = movie.css('h4[itemprop=name] a::text').extract_first()
            item['genre']       = movie.css('span[itemprop=genre]::text').extract()
            item['stars']       = movie.css('span[itemprop=actors] a::text').extract()
            item['director']    = movie.css('span[itemprop=director] a::text').extract_first()
            item['duration']    = movie.css('time::text').extract_first()
            item['metascore']   = movie.css('div.metascore strong::text').extract_first()
            item['description'] = movie.css('div[itemprop=description]::text').extract_first()

            item['image_urls']  = [movie.css('div.image img::attr(src)').extract_first()]

            yield item