import requests
from bs4 import BeautifulSoup
from time import sleep
import json


# 获取代理
def request_daili_list(url, count, headers):
    """

    :param url: 代理网站的url
    :param count: 页数
    :param headers:  请求头
    :return: Response.text
    """
    for i in range(1, count+1):
        page_url = url + str(i)
        res = requests.get(url=page_url, headers=headers)
        sleep(6)
        yield res.text


# 解析代理
def anylasis_agent(html):
    """

    :param html: 需要解析的网页
    :return: 返回一个列表;存储代理IP:port
    """
    soup = BeautifulSoup(html, "lxml")
    # 提取ip代理
    ip_list = soup.select("[data-title='IP']")
    cotegaries = soup.select("[data-title='类型']")
    ports = soup.select("[data-title='PORT']")
    proxies = []

    for i in range(len(ip_list)):
        proxy = {cotegaries[i].get_text(): ip_list[i].get_text() + ":" + ports[i].get_text()}
        proxies.append(proxy)
    return proxies


# 验证代理
def verify_proxeis(proxies, headers):
    """

    :param proxies: 代理
    :param headers: 请求头
    :return: 列表；可用代理
    """
    available_proxies = []
    for proxy in proxies:
        if requests.get(url="http://www.baidu.com/", headers=headers, proxies=proxy, timeout=2).status_code == 200:
            # 代理可用
            print("可用代理:", proxy)
            available_proxies.append(proxy)
        else:
            print("不可用代理:", proxy)
    return available_proxies


# 写入本地
def write_to_json(proxies):
    """

    :param proxies: 可用代理
    :return:
    """
    # 格式化代理
    url_list = []
    for proxy in proxies:
        for key, val in proxy.items():
            url_list.append(key + "://" + val)

    proxies_dict = {"proxies": url_list}
    with open("proxies.json", 'w', encoding='utf-8') as fp:
        fp.write(json.dumps(proxies_dict))


if __name__ == '__main__':
    url = "https://www.kuaidaili.com/free/inha/"
    # 请求头
    headers = {"user-agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

    # 请求代理页面
    html_pages = request_daili_list(url, 10, headers=headers)
    # 解析出代理列表
    proxies = []
    for page in html_pages:
        proxies += anylasis_agent(page)
    print(proxies)
    # 验证代理
    proxies = verify_proxeis(proxies, headers)

    # 将经过验证的代理写入本地
    write_to_json(proxies)

















