# -*- coding: utf-8 -*-

BOT_NAME = 'imdb_crawler'

SPIDER_MODULES   = ['imdb_crawler.spiders']
NEWSPIDER_MODULE = 'imdb_crawler.spiders'

AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_ENABLED   = True
CONCURRENT_REQUESTS    = 10
DOWNLOAD_TIMEOUT       = 720
RETRY_HTTP_CODES       = 500, 503, 400
RETRY_TIMES            = 5

IMAGES_STORE = 'images/'

ITEM_PIPELINES = {
  'imdb_crawler.pipelines.JsonWriterPipeline': 998,
  'imdb_crawler.pipelines.MyImagesPipeline': 999,
}