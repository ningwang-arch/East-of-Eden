# @Author: eclipse
# @Date: 2020-05-08 14:25:51
# @Last Modified by:   eclipse
# @Last Modified time: 2020-05-08 14:25:51

import requests
from lxml import etree
header = {
    'referer':
    'https://www.mzitu.com/227700/84',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
Error = []


def create(path):  # 创建文件夹函数，输入路径
    import os
    path = path.strip()
    path = path.rstrip('\\')
    os.makedirs(path)


def get_picture(url, name):
    response = requests.get(url, headers=header)
    html = response.content.decode()
    element = etree.HTML(html)
    url_next = element.xpath('//div[@class="main-image"]/p/a//@href')[0]
    try:
        img_url = element.xpath('//div[@class="main-image"]/p/a/img//@src')[0]
        img = requests.get(img_url, headers=header)

        path = "D:\\mzitu\\{}.jpg".format(name)
        with open(path, 'wb') as f:
            f.write(img.content)
    except Exception:
        Error.append(name)
        print(name + ' is fail')
    return url_next


# create("D:\\mzitu")  # 文件夹可预创建,如果用函数创建,后续更换起始节点需注释此步
i = 1983
url_start = 'https://www.mzitu.com/207786/26'
while (i < 2012):
    url = get_picture(url_start, str(i))
    url_start = url
    i += 1
print(Error)
