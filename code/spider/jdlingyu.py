
# @Author: eclipse
# @Date: 2020-05-06 15:28:56
# @Last Modified by:   eclipse
# @Last Modified time: 2020-05-06 15:28:56


import requests
from lxml import etree
# import re


def create(path):  # 创建文件夹函数，输入路径
    import os
    path = path.strip()
    path = path.rstrip('\\')
    os.makedirs(path)


create("D:\\jdlingyu")
Error = []
for i in range(11, 21):
    url = 'https://www.jdlingyu.mobi/collection/meizitu'
    formdata = {'type': 'collection1495', 'paged': i}
    header = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
    }
    url_response = requests.post(url, data=formdata, headers=header)
    url_html = url_response.text
    # print(url_html)
    element_html = etree.HTML(url_html)
    html_urls = element_html.xpath(
        '//*[@id="main"]/div/div/div/div/h2/a//@href')  # 获取每个合集的链接
    html_names = element_html.xpath(
        '//*[@id="main"]/div/div/div/div/h2/a/text()')  # 获取合集名
    #  print(html_urls)
    j = 0
    for html_url in html_urls:
        create("D:\\jdlingyu\\{}".format(html_names[j]))
        html_response = (requests.get(html_url,
                                      headers=header)).content.decode()
        element = etree.HTML(html_response)
        img_urls = element.xpath('//*[@id="content-innerText"]/p/img//@src')
        # print(img_urls)
        k = 0
        for img_url in img_urls:
            img = requests.get(img_url, headers=header)
            try:
                path = "D:\\jdlingyu\\{}\\{}.jpg".format(html_names[j], str(k))
                with open(path, 'wb') as f:
                    f.write(img.content)
            except Exception:
                print('Error')
                Error.append(html_names[j] + str(k))
            finally:
                k += 1
        print(html_names[j] + ' is OK,共' + str(k) + '张')
        j += 1
print(Error)
