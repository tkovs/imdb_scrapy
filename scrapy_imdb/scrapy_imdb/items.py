import scrapy

class MovieItem(scrapy.Item):
	title       = scrapy.Field()
	year        = scrapy.Field()
	duration    = scrapy.Field()
	genre       = scrapy.Field()
	description = scrapy.Field()
	director    = scrapy.Field()
	stars       = scrapy.Field()
	metascore   = scrapy.Field()

	image_urls  = scrapy.Field()
	images      = scrapy.Field()