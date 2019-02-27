# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

# 导入随机选择模块
import random
# 导入官方文档对应的HttpProxyMiddleware
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware
import json
class IPPOOLS(HttpProxyMiddleware):
    def __init__(self,ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        # 随机选择一个代理ip
        thisip = random.choice(self.read_ippools())
        print("当前的代理ip为:",thisip)
        request.meta["proxy"] = thisip

    # 定义一个辅助函数，用于读取代理池
    def read_ippools(self):
        with open("./proxies.json",'r',encoding='utf-8') as fp:
            ip_json = json.load(fp)
            return ip_json["proxies"]



