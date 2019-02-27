## Boss直聘爬虫
个人学习项目；通过scrapy_redis组件分布式爬取。代码完成时间大概在2018年11月左右，后续不提供更新维护

```
├── BossSpider
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
│       ├── boss.py  
│       ├── get_url.py  获取url存入redis；供从机爬取
│       ├── __init__.py
│       ├── proxies.json  免费代理
│       └── proxySpider.py  爬取免费代理供爬虫使用
├── README.md
└── scrapy.cfg
```
