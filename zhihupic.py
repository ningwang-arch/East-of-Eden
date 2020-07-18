import requests
import json
from lxml import etree
import os
import time
import urllib
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
total_path = 'D:/zhihupic'
if not os.path.exists(total_path):
    os.makedirs(total_path)
Error = []


def zhihuPicSpider(question_id):
    i = 0
    while True:
        url = 'https://www.zhihu.com/api/v4/questions/{}/answers?limit=5&offset={}'.format(
            question_id, i)
        i += 5
        response = requests.get(url, headers=headers)
        content = json.loads(response.content.decode())['data']
        if not content:
            break
        answer_ids = [item['id'] for item in content]
        for answer_id in answer_ids:
            answer_url = 'https://www.zhihu.com/question/{}/answer/{}'.format(
                question_id, answer_id)
            r = requests.get(answer_url, headers=headers)
            html = r.content.decode()
            element = etree.HTML(html)
            pic_urls = element.xpath('//noscript/img//@src')
            for pic_url in pic_urls:
                name = int(time.time() * 10)
                path = total_path + ('/{}.jpg').format(name)
                try:
                    urllib.request.urlretrieve(pic_url, path)
                except Exception:
                    Error.append(pic_url)
    print(Error)


if __name__ == '__main__':
    question_id = 376376914
    zhihuPicSpider(question_id)
