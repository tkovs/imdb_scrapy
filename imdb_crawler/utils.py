def fix_item(item):
	"""Fixes some *problems*"""
	
	item['title']       = fix_title(item['title'])
	item['year']        = extract_year(item['year'])
	item['metascore']   = check_metascore(item['metascore'])
	item['description'] = fix_description(item['description'])

	return item

def extract_year(year):
	return year[-5:-1]

def fix_description(description):
	"""Removes unnecessary characters
	
	In imdb, all movie descriptions start with '\n' and end with many spaces, 
	in addition to unicode characters. This function fixes this
	inconvenience.
	"""
	
	description = description.replace('\n', '')
	description.encode('utf-8')
	description = description.strip()

	return description

def fix_title(title):
	"""Erases an space character before each title"""

	title = title[1:-7]

	return title

def check_metascore(metascore):
	"""Adds '/100' to metascores."""

	#some movies has no metascore, so scrapy returns null
	if metascore is not None:
		return metascore.strip() + '/100'

	return None