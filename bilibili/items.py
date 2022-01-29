# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()
    title = scrapy.Field()
    rank = scrapy.Field()
    play = scrapy.Field()
    like = scrapy.Field()
    follow = scrapy.Field()
    up = scrapy.Field()
