
# @Author: eclipse
# @Date: 2020-05-05 19:10:26
# @Last Modified by:   eclipse
# @Last Modified time: 2020-05-05 19:10:26


import requests
from lxml import etree


def create(path):  # 创建文件夹函数，输入路径
    import os
    path = path.strip()
    path = path.rstrip('\\')
    os.makedirs(path)


# create("D:\\testpic")  # 创建总文件夹
Error = []
for i in range(8, 12):
    urls = 'https://wallhaven.cc/search?q=id%3A5&ref=fp&page={}'.format(i)
    proxy = {'http': 'http://202.115.142.147:9200'}
    header = {
        'referer':
        'https://wallhaven.cc/',
        'cookie':
        '__cfduid=d9569b967ebd227a7b27c7d63d19c11171588670405; XSRF-TOKEN=eyJpdiI6InMzTFNxNnNGakEzeFlMaW8rRFZGRVE9PSIsInZhbHVlIjoidGUrRTFpOGQ0MjBSdGZNTlJ2KzhERkFmaTdaQXZmRUR0djB2RDhRU3VWdnlTckhRRTY1Z1wvU3cyUkZoWkluT08iLCJtYWMiOiI5Y2RiZWU2OWZlMjFmZGExN2E5NjZiZjJiMzBjN2Y5MTlkMDRmMzAxZmJiMDZkYzkzZWVlNTViNWI3YWViMGZkIn0%3D; wallhaven_session=eyJpdiI6IkNLekc5Z2JGM3ZYalYwWFZESTlleUE9PSIsInZhbHVlIjoiV24wMFliVmhpd004NXpSQ3oxQkVEU0pNZFBzTnR5NU0rQnNZY1NCTHl2NVpvWjlCWmtSbzRaK2xzYzJENzVWUyIsIm1hYyI6IjUwODI0Y2FkNDZjNjZjNDI3NzM1Y2UyNTlkM2E1NzVkMjEwNjJlNzdlMzFhOWJkYTYyZWY1NTY3ZGQ5MzgxMDQifQ%3D%3D',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    }
    list_response = requests.get(urls, headers=header)
    list_html = list_response.content.decode()
    # print(list_html)
    element_html = etree.HTML(list_html)
    img_urls = element_html.xpath(
        '//*[@id="thumbs"]/section/ul/li/figure/a//@href')
    # print(img_urls)
    j = 0
    for url in img_urls:
        # print(url)
        name = str(((i - 2) * 24 + j))
        url_response = requests.get(url, headers=header).content.decode()
        element = etree.HTML(url_response)
        img_url = element.xpath('//*[@id="wallpaper"]//@src')[0]
        # print(img_url)
        img = requests.get(img_url, headers=header)
        try:
            path = "D:\\testpic\\{}.jpg".format(name)
            with open(path, 'wb') as f:
                f.write(img.content)
                print(name + ' OK')
        except Exception:
            Error.append(name)
            print(name + ' fail')
        finally:
            j += 1
print(Error)
