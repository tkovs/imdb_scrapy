import scrapy

class MovieItem(scrapy.Item):
    title       = scrapy.Field()
    duration    = scrapy.Field()
    genre       = scrapy.Field()
    description = scrapy.Field()
    stars       = scrapy.Field()
    director    = scrapy.Field()
    stars       = scrapy.Field()
    metascore   = scrapy.Field()