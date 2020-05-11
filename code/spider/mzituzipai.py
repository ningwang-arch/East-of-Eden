
# @Author: eclipse
# @Date: 2020-05-08 16:18:01
# @Last Modified by:   eclipse
# @Last Modified time: 2020-05-08 16:18:01


import requests
from lxml import etree

Error = []
j = 351
for i in range(1, 41):
    url = 'https://www.mzitu.com/zipai/comment-page-{}/#comments'.format((i))
    header = {
        'referer':
        'https://www.mzitu.com/zipai/comment-page-1/',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    response = requests.get(url, headers=header)
    html = response.content.decode()
    # print(html)
    element = etree.HTML(html)
    img_urls = element.xpath('//img[@class="lazy"]//@data-original')
    # print(img_urls)
    # print(len(img_urls))
    for img_url in img_urls:
        img = requests.get(img_url, headers=header)
        try:
            path = "D:\\testpic\\{}.jpg".format(str(j))
            with open(path, 'wb') as f:
                f.write(img.content)
        except Exception:
            print(str(j) + ' is fail')
            Error.append(str(j))
        finally:
            j += 1
    print('第%d页已完成' % i)
print(Error)
