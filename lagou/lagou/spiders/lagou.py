# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from pyquery import PyQuery as pd
from lagou.items import Lagou_item
from datetime import datetime

class LaogouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['http://www.lagou.com/']

    rules = (
        Rule(LinkExtractor(allow=r'zhaopin/.*?/'), follow=True),
        Rule(LinkExtractor(allow=r'jobs/.*?.html'), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        if response:
            doc = pd(response.text)
            # 获取职位名称
            job_name = doc('.position-content .position-content-l .job-name span').text()
            # 就业薪资
            salary = ''.join(response.xpath('//span[@class="salary"]/text()').extract()).strip().replace('k', '000').split('-')
            salary_max = salary[1]
            salary_min = salary[0]
            # 就业地点
            job_address = ''.join(response.xpath('//dd[@class="job_request"]/p/span[2]/text()').extract()).replace('/', '')
            # 工作经验
            work_years = ''.join(response.xpath('//dd[@class="job_request"]/p/span[3]/text()').extract()).replace('/', '')
            # 学历要求
            Enducation = ''.join(response.xpath('//dd[@class="job_request"]/p/span[4]/text()').extract()).replace('/', '')
            # 工作类型
            job_type = ''.join(response.xpath('//dd[@class="job_request"]/p/span[5]/text()').extract())
            # 工作优势
            job_advantage = ''.join(response.xpath('//dd[@class="job-advantage"]/p/text()').extract())
            # 获取职位要求：
            job_bts = doc('.job_bt div p').text()
            # 获取公司地址
            work_address = doc('.job-address .work_addr').text().replace('查看地图', '')
            # 公司主页
            page = response.css('.c_feature li a::text').extract_first('')
            # 领域
            field = ''.join(response.xpath('//ul[@class="c_feature"]/li[1]/text()').extract()).strip()
            # 发展阶段
            develp = ''.join(response.xpath('//ul[@class="c_feature"]/li[2]/text()').extract()).strip()
            # 规模
            scale = ''.join(response.xpath('//ul[@class="c_feature"]/li[3]/text()').extract()).strip()
            # 招聘发布时间
            publish_time = ''.join(response.xpath('//p[@class="publish_time"]/text()').extract())
            # 爬取时间
            pa_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            item = Lagou_item()
            item['name'] = job_name
            item['salary_min'] = salary_min
            item['salary_max'] = salary_max
            item['job_address'] = job_address
            item['work_years'] = work_years
            item['Enducation'] = Enducation
            item['job_type'] = job_type
            item['job_advantage'] = job_advantage
            item['job_bts'] = job_bts
            item['work_address'] = work_address
            item['page'] = page
            item['field'] = field
            item['develp'] = develp
            item['scale'] = scale
            item['publish_time'] = publish_time
            item['pa_time'] = pa_time

            print(item)
            print('======================================================')
            yield item


