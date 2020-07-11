def polishes_item(item):
  item['title'] = polishes_title(item['title'])
  item['year'] = polishes_year(item['year'])
  item['metascore'] = polishes_metascore(item['metascore'])
  item['description'] = polishes_description(item['description'])

  return item

def polishes_description(description):
  description = description.replace('\n', '')
  description = description.strip()

  return description

def polishes_title(title):
  title = title[1:-7]

  return title

def polishes_metascore(metascore):
  if metascore is None:
    return metascore

  return metascore.strip() + '/100'

def polishes_year(year):
  return year[-5:-1]