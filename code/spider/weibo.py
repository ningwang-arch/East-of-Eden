import requests
# from lxml import etree
import time
import random
false = False
Error = []
for i in range(1, 11):
    urls = 'https://m.weibo.cn/api/container/getSecond?containerid=1078036378721205_-_photoall&page={}&count=24&title=%E5%9B%BE%E7%89%87%E5%A2%99&luicode=10000011&lfid=1078036378721205'.format(
        i)
    header = {
        'cookie':
        'SUB=_2A25zt9y8DeRhGeFN6lEY8SfFyjmIHXVRW-T0rDV6PUJbktAfLRTykW1NQH3JDWFQwuULXJwhFPfovs6RAiCBwtV-; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW8bVfrGSRgH9yEqV8e8SOp5JpX5KzhUgL.FoM0eKe4eK.4eK-2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNe0201K241K2f; SUHB=0A0JDVn6J9KegP; SSOLoginState=1588833516; _T_WM=36665697718; MLOGIN=1; WEIBOCN_FROM=1110006030; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D1078036378721205%26fid%3D1078036378721205_-_photoall%26uicode%3D10000012; XSRF-TOKEN=c40a4c',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response = requests.get(urls, headers=header)
    html = response.content.decode()
    # print(html)
    html = eval(html)
    img_urls = []
    temp = html["data"]
    # print(type(temp))
    cards = (temp["cards"])
    # print(len(cards))
    for items in cards:
        # print(type(items))
        temp = items["pics"]
        # print(len(temp))
        for item in temp:
            res = item['pic_big'].replace("\\", '')
            # print(type(item))
            img_urls.append(res)
    # print(len(img_urls))
    # print(img_urls)
    j = 0
    for img_url in img_urls:
        name = str(((i - 1) * 24 + j))
        img = (requests.get(img_url, headers=header)).content
        try:
            path = "D:\\weibo\\{}.jpg".format(name)
            with open(path, 'wb') as f:
                f.write(img)
        except Exception:
            print(name + ' is fail')
            Error.append(name)
        finally:
            j += 1
            time.sleep(random.randint(1, 3))
    print('第%d页已完成' % i)
    time.sleep(random.randint(10, 20))
print(Error)
