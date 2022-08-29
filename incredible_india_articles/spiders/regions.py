'''
IT458 - Assignment 1
Inverted Index Representation

By:
  Gaurang Jitendra Velingkar
  191IT113

-- UNUSED --
This script scrapes "region" based articles from www.incredibleindia.org.

'''

import scrapy

class GetArticles(scrapy.Spider):
	name = 'regions'
	start_urls = [
		'https://www.incredibleindia.org/content/incredible-india-v2/en/destinations/states/delhi.html'
	]
	allowed_domains = ['www.incredibleindia.org']

	def parse(self, response):
		all_links = response.css('.mega-list a::attr(href)').getall()

		for data in response.css("div.read-more-hide"):
			all_paragraphs = data.css('p ::text').getall()

			with open(f'articles/{response.url.split("/")[-1].replace("html", "")}txt', 'w') as f:
				f.write(''.join(all_paragraphs).replace(u'\n', u'').replace(u'\xa0', u'\n'))

			for link in all_links:
				yield response.follow(response.urljoin(link), callback=self.parse_final_link)

	def parse_final_link(self, response):
		for data in response.css("div.read-more-hide"):
			all_paragraphs = data.css('p ::text').getall()

			with open(f'articles/{response.url.split("/")[-1].replace("html", "")}txt', 'w') as f:
				f.write(''.join(all_paragraphs).replace(u'\n', u'').replace(u'\xa0', u'\n'))