import requests
from lxml import etree
from PIL import Image
import re
# import re


def create(path):  # 创建文件夹函数，输入路径
    import os
    path = path.strip()
    path = path.rstrip('\\')
    os.makedirs(path)


#  create("D:\\testpic")
Error = []  # 创建错误列表
for i in range(1, 11):
    if (i == 1):
        list_url = 'http://pic.netbian.com/4kdongman/index.html'
    else:
        list_url = 'http://pic.netbian.com/4kdongman/index_{}.html'.format(i)
    header = {
        'Referer': 'http://pic.netbian.com/index.html',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        'cookie': '__cfduid=d72b56fddfbff3f1b275c40c13184345c1588501223',
    }
    list_response = requests.get(list_url, headers=header)
    list_html = list_response.content.decode('GBK')
    # print(list_html)
    element_html = etree.HTML(list_html)
    image_urls = element_html.xpath('//*[@id="main"]/div[3]/ul/li/a/@href')

    name = element_html.xpath('//*[@class="clearfix"]/li/a/b//text()')
    # print(image_urls)
    # print(name)
    j = 0
    for url in image_urls:
        url = 'http://pic.netbian.com/' + url
        # print(url)
        url_response = requests.get(url, headers=header).content.decode('GBK')
        element = etree.HTML(url_response)
        temp = element.xpath(
            '//*[@id="main"]/div[2]/div[2]/div[1]/a/text()')[0]
        size = re.findall(r'\d*\d', temp)
        img_url = 'http://pic.netbian.com/' + element.xpath(
            '//*[@id="img"]/img/@src')[0]
        # print(img_url)
        img = requests.get(img_url, headers=header)
        try:
            path = "D:\\testpic\\{}.png".format(name[j])
            with open(path, 'wb') as f:
                f.write(img.content)
                img = Image.open(path)
                img = img.resize((int(size[0]), int(size[1])),
                                 Image.ANTIALIAS)  # 改变大小 抗锯齿
                # print(img.size)
                img.save(path, quality=95)
                print(name[j] + ' OK')
        except Exception:
            Error.append(name[j])
            print(name[j] + ' fail')
        finally:
            j += 1

print(Error)
