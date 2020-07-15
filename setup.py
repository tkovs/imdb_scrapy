from setuptools import setup

setup(
  name='crawler_imdb',
  packages=['crawler_imdb'],
  install_requires=[
    'scrapy',
    'image',
    'pytest',
  ],
)