# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Lagou_item(scrapy.Item):
    name = scrapy.Field()
    salary_min = scrapy.Field()
    salary_max = scrapy.Field()
    job_address = scrapy.Field()
    work_years = scrapy.Field()
    Enducation = scrapy.Field()
    job_type = scrapy.Field()
    job_advantage = scrapy.Field()
    job_bts = scrapy.Field()
    work_address = scrapy.Field()
    page = scrapy.Field()
    field = scrapy.Field()
    develp = scrapy.Field()
    scale = scrapy.Field()
    publish_time = scrapy.Field()
    pa_time = scrapy.Field()