
# @Author: eclipse
# @Date: 2020-05-10 09:59:49
# @Last Modified by:   eclipse
# @Last Modified time: 2020-05-10 09:59:49

import requests
from lxml import etree


def create(path):  # 创建文件夹函数，输入路径
    import os
    path = path.strip()
    path = path.rstrip('\\')
    os.makedirs(path)


# create("D:\\acg")
Error = []
k = 0
for i in range(1, 11):
    url = "https://acg.fi/"
    header = {
        'Referer': 'http://moe321.com/',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'cookie': '__cfduid=d642e7af47ad8c6054735390a32e1f4851589069099',
    }
    formdata = {
        'type': 'catL1',
        'paged': i,
    }
    list_response = requests.post(url, headers=header, data=formdata)
    list_html = list_response.text
    list_element = etree.HTML(list_html)
    # print(list_html)
    temp = list_element.xpath(
        '//*[@id="main"]/div[2]/div/div/div[2]/h2/a//@href')
    html_urls = [i for i in temp if ('news' not in i)]
    # print(len(html_urls))
    # print((html_urls))
    for html_url in html_urls:
        response = requests.get(html_url, headers=header)
        html = response.content.decode()
        element = etree.HTML(html)
        img_urls = element.xpath(
            '//figure[@class="content-img-box"]/img//@src')
        # print(img_urls)
        # print((name))
        if (len(img_urls) == 0):
            continue
        else:
            create('D:\\acg\\{}'.format(str(k)))
            j = 0
            for img_url in img_urls:
                img = (requests.get(img_url)).content
                try:
                    path = "D:\\acg\\{}\\{}.png".format(str(k), str(j))
                    with open(path, 'wb') as f:
                        f.write(img)
                except Exception:
                    print('Error')
                    Error.append(str(k) + str(j))
                finally:
                    j += 1
            k += 1
    print('第%d页已完成' % i)
print(Error)
