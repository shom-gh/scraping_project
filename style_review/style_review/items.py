# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StyleReviewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    brewery = scrapy.Field()
    beer_type = scrapy.Field()
    abv = scrapy.Field()
    rating = scrapy.Field()
    rank = scrapy.Field()
    location1 = scrapy.Field()
    location2 = scrapy.Field()
    rdev = scrapy.Field()
    score = scrapy.Field()
    look = scrapy.Field()
    smell = scrapy.Field()
    taste = scrapy.Field()
    feel = scrapy.Field()
    overall = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()

    url_beer = scrapy.Field()
    url_brewery = scrapy.Field()
    url_beer_type = scrapy.Field()
    url_author = scrapy.Field()