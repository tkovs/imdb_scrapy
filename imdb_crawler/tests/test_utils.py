from imdb_crawler.utils import *

def test_extract_year():
	mock_title = 'Saint Maud (2019)'
	year = extract_year(mock_title)
	expected_year = '2019'

	assert year == expected_year