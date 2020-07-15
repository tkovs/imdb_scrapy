from crawler_imdb.utils import *

mock_title = ' Saint Maud (2019)'
mock_metascore = '87    '

def test_polishes_year():
	year = polishes_year(mock_title)
	expected_year = '2019'

	assert year == expected_year

def test_polishes_title():
	title = polishes_title(mock_title)
	expected_title = 'Saint Maud'

	assert title == expected_title

def test_polishes_metascore():
	metascore = polishes_metascore(mock_metascore)
	expected_metascore = '87/100'

	assert metascore == expected_metascore