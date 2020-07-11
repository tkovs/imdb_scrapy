# -*- coding: utf-8 -*-

BOT_NAME = 'scrapy_imdb'

SPIDER_MODULES   = ['scrapy_imdb.spiders']
NEWSPIDER_MODULE = 'scrapy_imdb.spiders'

AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_ENABLED   = True
CONCURRENT_REQUESTS    = 10
DOWNLOAD_TIMEOUT       = 720
RETRY_HTTP_CODES       = 500, 503, 400
RETRY_TIMES            = 5

IMAGES_STORE = 'images/'

ITEM_PIPELINES = {
  'scrapy_imdb.pipelines.JsonWriterPipeline': 998,
  'scrapy_imdb.pipelines.MyImagesPipeline': 999,
}