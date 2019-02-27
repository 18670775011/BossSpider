# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位
    job = scrapy.Field()
    # 薪水
    salary = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 要求
    require = scrapy.Field()
    # 公司名
    company_name = scrapy.Field()
    # 公司规模
    company_size = scrapy.Field()
    # 职位描述
    job_info = scrapy.Field()
    # 公司介绍
    company_info = scrapy.Field()

    # 如果是一个公司招多人的情况
    jobs = scrapy.Field()

class JobItem(scrapy.Item):
    # 岗位
    datail_job = scrapy.Field()
    # 薪资
    datail_salary = scrapy.Field()
    # 位置
    datail_require = scrapy.Field()
