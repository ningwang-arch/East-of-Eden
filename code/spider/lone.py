# @Author: eclipse
# @Date: 2020-05-10 10:47:32
# @Last Modified by:   eclipse
# @Last Modified time: 2020-05-10 10:47:32

# 单张图片爬取
import requests
header = {
    'Referer': '',
    'User-Agent': '',
    'cookie': '',
}
url = ''
img = (requests.get(url)).content
# print(img)
path = "temp.jpg"
with open(path, 'wb') as f:
    f.write(img)
