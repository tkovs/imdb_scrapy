# -*- coding: utf-8 -*-

from scrapy            import Spider
from scrapy_imdb.items import MovieItem

class ImdbSpider(Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/movies-coming-soon/?ref_=inth_cs',]

    def parse(self, response):
        for movie in response.css('div.list_item'):
            item = MovieItem()

            item['title']       = movie.css('h4 a::text').extract_first()
            item['year']        = item['title']
            item['genre']       = movie.css('.cert-runtime-genre span:not([class^="ghost"])::text').extract()
            item['stars']       = movie.css('.txt-block')[1].css('a::text').extract()
            item['director']    = movie.css('.txt-block a::text').extract_first()
            item['duration']    = movie.css('time::text').extract_first()
            item['metascore']   = movie.css('span.metascore::text').extract_first()
            item['description'] = movie.css('.outline::text').extract_first().strip()

            item['image_urls']  = movie.css('img.poster::attr(src)').extract()

            yield item