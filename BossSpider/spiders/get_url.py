import requests
from selenium import webdriver
from lxml import etree
import json
import redis

url = "https://www.zhipin.com/"


def creat_url():
    driver = webdriver.Chrome()

    driver.get(url=url)

    html_tree = etree.HTML(driver.page_source)

    city_list = html_tree.xpath("//div[@class='dorpdown-city']//li/@data-val")

    job_list = html_tree.xpath("//div[@class='job-menu']//a/@href")

    job_code = []

    for job in job_list:
        job_code.append(job.split("-")[-1])

    # 拼接url
    for city in city_list:
        for job in job_code:
            yield "https://www.zhipin.com/c" + city + "-" + job


def write_to_redis(url_list):
    rds = redis.StrictRedis(host='10.36.133.177', port=6379, db=0)
    for url in url_list:
        rds.lpush(url)









