import feedparser as fp

URL = 'https://www.producthunt.com/feed'

def get_source():
	try:
		parsed_data = fp.parse(URL)
		return parsed_data
	except Exception:
		print('Unable to get the feeds')


def parse_source():
	feeds = get_source()
	feed_title = []
	feed_link = []
	feed_pub = []
	for entry in feeds.entries:
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

	return (feed_title, feed_link, feed_pub)


if __name__ == '__main__':
	parse_source()