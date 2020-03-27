# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from all.settings import mongodb_host,mongodb_port,mongodb_name,mongodb_sheet
class AllPipeline(object):

    def __init__(self):

        host = mongodb_host
        port = mongodb_port
        dbname = mongodb_name
        sheetname = mongodb_sheet
        cur = pymongo.MongoClient(host=host, port=port)
        mydb = cur[dbname]
        self.post = mydb[sheetname]
    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item