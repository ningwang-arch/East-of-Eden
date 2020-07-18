# @Author: eclipse
# @Date: 2020-07-18 10:37:56
# @Last Modified by:   eclipse
# @Last Modified time: 2020-07-18 10:37:56

import requests
import time
import os
url = 'https://i.xinger.ink:4443/images.php'
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}
i = 0
num = int(input("请输入下载页数:"))
path = 'D:/testpic'
if not os.path.exists(path):
    os.makedirs(path)
while (i < num):
    response = requests.get(url, headers=headers)
    # print(response)
    name = str(int(time.time() * 100))
    img_path = 'D:/testpic/{}.jpg'.format(name)
    with open(img_path, 'wb') as f:
        f.write(response.content)
    i += 1
    print("第%d张已完成" % (i))
    if (i % 20 == 0):
        time.sleep(2)
