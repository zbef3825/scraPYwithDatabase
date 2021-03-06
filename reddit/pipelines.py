# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class mongodbpipeline(object):


	def __init__(self):

		connection = pymongo.MongoClient('mongodb://localhost:27017/')
		db = connection['REDDIT_DATABASE']
		self.collection = db.posts
		print "MongoDB Pipeline Initiated!"

	def process_item(self, item, spider):
		print "Reorganizing json files..."
		post_num = {}
		postcount = 0
		value_count = 0
		key_count = 0
		#add postnumber index

		for value in item['post_title']:

			
			if postcount == 0:
				pass
			else:
				post_num.pop('post'+str(postcount), None)

			postcount += 1
			post_num['post'+str(postcount)] = {}

			for key in item:
				post_num['post'+str(postcount)][key] = item[key][value_count]



			value_count += 1
			self.collection.insert(dict(post_num))

		print "Saving jsons to MongoDB"

		
		


		
		return post_num
