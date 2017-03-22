# -*- coding: utf-8 -*-

BOT_NAME = 'scrapy_imdb'

SPIDER_MODULES = ['scrapy_imdb.spiders']
NEWSPIDER_MODULE = 'scrapy_imdb.spiders'

CONCURRENT_REQUESTS = 10
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_MAX_DELAY = 60
DOWNLOAD_TIMEOUT = 720
RETRY_TIMES = 5
RETRY_HTTP_CODES = 500, 503, 400

ITEM_PIPELINES = {
    "scrapy_imdb.pipelines.JsonWriterPipeline": 999,
}
