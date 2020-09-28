install: setup.py
		python3 setup.py install

run:
		scrapy crawl comingsoon

test:
		pytest

reset:
		rm -r build dist crawler_imdb.egg-info