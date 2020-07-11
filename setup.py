from setuptools import setup

setup(
  name='imdb_crawler',
  packages=['imdb_crawler'],
  install_requires=[
    'scrapy',
    'image',
    'pytest',
  ],
)