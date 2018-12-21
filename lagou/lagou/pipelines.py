# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class LagouPipeline(object):
    def process_item(self, item, spider):
        return item

class Lagou_sql(object):

    def __init__(self):
        self.db = pymysql.connect('localhost', 'root', '123456', 'test')
        self.cursor = self.db.cursor()

    def process_item(self, item, spiders):
        sql = """INSERT INTO lagou(name, salary_min,salary_max, job_address, work_years, Enducation, job_type, job_advantage, job_bts,
        work_address, page, field, develp, scale,publish_time,pa_time ) 
        value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        # try:
        self.cursor.execute(sql, (item['name'], item['salary_min'],
                                  item['salary_max'],item['job_address'],
                                  item['work_years'], item['Enducation'],
                                  item['job_type'], item['job_advantage'],
                                  item['job_bts'], item['work_address'],
                                  item['page'], item['field'],
                                  item['develp'], item['scale'],
                                  item['publish_time'], item['pa_time']))
        self.db.commit()
        # except:
        #     # 调用rollback()执行数据回滚，相当于什么都没发生
        #     self.db.rollback()

    def close_book(self):
        self.db.close()

