
# @Author: eclipse
# @Date: 2020-05-09 10:25:34
# @Last Modified by:   eclipse
# @Last Modified time: 2020-05-09 10:25:34

# 此爬虫需用户自建符合要求的文件夹
import requests
Error = []
for i in range(1, 11):
    # 通过更改cid的值可以爬取不同分类的图片 360new:最新壁纸 36:4K专区 6:美女模特  30:爱情美图 9:风景大片 15:小清新 26:动漫卡通 11明星风尚 14:萌宠动物 5:游戏壁纸 12:汽车天下 10:炫酷时尚 29:月历壁纸 7:影视剧照 13:节日美图 22:军事天地 16:劲爆体育 18:baby秀 35:文字控
    url = 'https://www.tool2.cn/Include/BiZhiAPI.php?cid=360new&start={}&count=30'.format(
        30 * (i - 1))
    header = {
        'referer':
        'https://www.tool2.cn/bizhi',
        'cookie':
        'PHPSESSID=evvbeu1munvfh5603sd6vo5l36; security_session_verify=777753b568d3b8f3000c1ff22fab7f36',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    }
    response = requests.get(url, headers=header)
    html = response.content.decode()
    html = eval(html)
    # print(html)
    temp_list = html["data"]
    img_urls = []
    for url in temp_list:
        temp = url['url']
        res = temp.replace('\\', '')
        img_urls.append(res)
    # print(img_urls[0])
    j = 0
    for img_url in img_urls:
        name = str(((i - 1) * 30 + j))
        img = (requests.get(img_url, headers=header)).content
        try:
            path = "D:\\tool2new\\{}.jpg".format(name)
            with open(path, 'wb') as f:
                f.write(img)
        except Exception:
            print(name + ' is fail')
            Error.append(name)
        finally:
            j += 1
    print('第%d页已完成' % i)
print(Error)
