'''
IT458 - Assignment 1
Inverted Index Representation

By:
  Gaurang Jitendra Velingkar
  191IT113

This script scrapes 100 articles from www.incredibleindia.org

'''

import scrapy

class GetArticles(scrapy.Spider):
	name = 'articles'
	start_urls = [
		'https://www.incredibleindia.org/content/incredible-india-v2/en/experiences/spiritual/hinduism.html',			# Spiritual
		'https://www.incredibleindia.org/content/incredible-india-v2/en/experiences/spiritual/christianity.html',		# Spiritual
		'https://www.incredibleindia.org/content/incredible-india-v2/en/experiences/food-and-cuisine/north.html',		# Food & Cuisine
		'https://www.incredibleindia.org/content/incredible-india-v2/en/experiences/food-and-cuisine/west.html',		# Food & Cuisine
		'https://www.incredibleindia.org/content/incredible-india-v2/en/experiences/nature-and-wildlife/lakes.html',	# Nature & Wildlife
		'https://www.incredibleindia.org/content/incredible-india-v2/en/experiences/nature-and-wildlife/deserts.html',	# Nature & Wildlife
		'https://www.incredibleindia.org/content/incredible-india-v2/en/experiences/adventure/adventure-on-land.html',	# Adventure
		'https://www.incredibleindia.org/content/incredible-india-v2/en/experiences/adventure/adventure-in-sky.html',	# Adventure
		'https://www.incredibleindia.org/content/incredible-india-v2/en/experiences/heritage/forts-and-palaces.html',	# Heritage
		'https://www.incredibleindia.org/content/incredible-india-v2/en/experiences/heritage/rock-architecture.html',	# Heritage
		'https://www.incredibleindia.org/content/incredible-india-v2/en/experiences/Shopping.html',						# Shopping
		'https://www.incredibleindia.org/content/incredible-india-v2/en/experiences/yoga-and-wellness/ayurveda.html'	# Yoga & Wellness
	]
	allowed_domains = ['www.incredibleindia.org']

	def parse(self, response):
		for data in response.css("div.read-more-hide"):
			all_paragraphs = data.css('p ::text').getall()
			all_links = data.css('p a::attr(href)').getall()

			# Save all paragraphs in a file with the same name as the URL
			with open(f'articles/{response.url.split("/")[-1].replace("html", "")}txt', 'w') as f:
				f.write(''.join(all_paragraphs).replace(u'\n', u'').replace(u'\xa0', u'\n'))

			# Extract text from all links in the list
			for link in all_links:
				yield response.follow(response.urljoin(link), callback=self.parse)
