
# @Author: eclipse
# @Date: 2020-05-10 08:15:07
# @Last Modified by:   eclipse
# @Last Modified time: 2020-05-10 08:15:07


import requests
from lxml import etree
import json

for i in range(1, 11):
    url = "https://so.gushiwen.org/shiwen/default_0AA{}.aspx".format(i)
    header = {
        'cookie':
        'login=true',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response = requests.get(url, headers=header)
    html = response.content.decode()
    element = etree.HTML(html)
    temp = element.xpath('//div[@class="cont"]/p/a//@href')
    content_urls = []
    for j in range(len(temp)):
        if ((j + 1) % 3 == 1):
            content_urls.append(temp[j])
    id_list = [i[31:43] for i in content_urls]
    content_list = []
    k = 0
    for content_url in content_urls:
        list_response = requests.get(content_url, headers=header)
        list_html = list_response.content.decode()
        list_element = etree.HTML(list_html)
        item = {}
        item["title"] = (
            list_element.xpath('//div[@class="cont"]/h1//text()'))[0]
        item["dynasty"] = (
            list_element.xpath('//p[@class="source"]/a[1]/text()'))[0]
        item["author"] = (
            list_element.xpath('//p[@class="source"]/a[2]/text()'))[0]
        temp = '//*[@id="%s"]//text()' % (("contson" + id_list[k]))
        item["content"] = ''.join(list_element.xpath(temp)).replace(
            '  ', '').replace('\n', '').replace('\u3000', '')
        item["tag"] = (','.join(
            list_element.xpath(
                '//div[@class="left"]/div[2]//div[@class="tag"]//text()')
        ).replace('\n', '')).replace(',', '') if list_element.xpath(
            '//div[@class="left"]/div[2]//div[@class="tag"]//text()') else ''
        content_list.append(item)
        k += 1
    with open('shici.txt', 'a', encoding='utf-8') as f:
        for content in content_list:
            f.write(json.dumps(content, ensure_ascii=False, indent=2))
            f.write('\n')
    print('第%d页已完成' % i)
