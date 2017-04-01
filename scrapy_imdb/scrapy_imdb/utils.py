def fix_item(item):
	"""Fixes some *problems*"""
	
	item['title']       = fix_title(item['title'])
	item['metascore']   = check_metascore(item['metascore'])
	item['description'] = fix_description(item['description'])

	return item

def fix_description(description):
	"""Removes unnecessary characters
	
	In imdb, all movie descriptions start with '\n' and end with many spaces, 
	in addition to unicode characters. This function fixes this
	inconvenience.
	"""
	
	description = description.replace('\n', '')
	description.encode('utf-8')
	description = description[:-20]

	return description

def fix_title(title):
	"""Erases an space character before each title"""

	title = title[1:]

	return title

def check_metascore(metascore):
	"""Adds '/100' to metascores."""

	#some movies has no metascore, so scrapy returns null
	if metascore is not None:
		return metascore + '/100'

	return None