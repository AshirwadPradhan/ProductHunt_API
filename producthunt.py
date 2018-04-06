import feedparser as fp
import json
from collections import OrderedDict

URL = 'https://www.producthunt.com/feed'
title = []
link = []
pub = []

def get_source():
	try:
		parsed_data = fp.parse(URL)
		return parsed_data
	except Exception:
		print('Unable to get the feeds')


def parse_source(number_of_links=10):
	feeds = get_source()
	feed_title = []
	feed_link = []
	feed_pub = []
	for i,entry in enumerate(feeds.entries):
		if i < number_of_links:
			try:
				feed_title.append(entry.title)
			except AttributeError:
				print('Unable to get title')

			try:
				feed_link.append(entry.link)
			except AttributeError:
				print('Unable to get link')

			try:
				feed_pub.append(entry.published)
			except AttributeError:
				print('Unable to get date published')
		else:
			break

	return (feed_title, feed_link, feed_pub)



title, link, pub  = parse_source()

feed_dict = OrderedDict()
for i in range(len(title)):
	temp_dict = {'title':title[i], 'link':link[i], 'pub':pub[i]}
	feed_dict['news'+str(i)] = temp_dict

try:
	json_feed_dict = json.dumps(feed_dict)
except Exception:
	print('Error coverting data to json object')