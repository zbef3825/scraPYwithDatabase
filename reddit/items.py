# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class redditItems(scrapy.Item):
	post_title = scrapy.Field()
	post_link = scrapy.Field()
	post_rating = scrapy.Field()
	post_comment_link = scrapy.Field()
	post_sub = scrapy.Field()