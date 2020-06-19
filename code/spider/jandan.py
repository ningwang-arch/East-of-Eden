# @Author: eclipse
# @Date: 2020-06-19 12:10:39
# @Last Modified by:   eclipse
# @Last Modified time: 2020-06-19 12:10:39

# 如果继续用时间戳命名文件,那么请不要随意更改图片文件命名方式
import requests
from lxml import etree
import time
url = 'https://jandan.net/ooxx/MjAyMDA2MTktMTIw#comments'
headers = {
    'cookie':
    'bad-click-load=on; nsfw-click-load=off; PHPSESSID=rn1drqkgkaft3otb3rl8mqeffn',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
}
Error = []


def spider(start_url):
    global Error
    response = requests.get(start_url, headers=headers)
    html = response.content.decode()
    element = etree.HTML(html)
    next_url = 'https:' + element.xpath(
        '//a[@title="Older Comments"]//@href')[0]
    temp_img_urls = element.xpath('//li/div/div/div[2]/p/a//@href')
    img_urls = ['https:' + i for i in temp_img_urls]
    for img_url in img_urls:
        name = str(int(time.time() * 1000))
        img = requests.get(img_url, headers=headers)
        try:
            path = 'D:\\testpic\\{}.jpg'.format(name)
            with open(path, 'wb') as f:
                f.write(img.content)
        except Exception:
            Error.append(img_url)
    return next_url


while (True):
    start_url = spider(start_url=url)
    url = start_url

print(Error)
