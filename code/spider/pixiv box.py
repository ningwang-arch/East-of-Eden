# 这个爬虫对应的网站挂了  后续补充一个新网站对应的爬虫 爬虫结构没问题

# 2020.7.18 更新 这个网站恢复了,此爬虫可正常使用,之前更新的pixiv.py里的那个网站挂了
import requests
from lxml import etree
import re


def create(path):  # 创建文件夹函数，输入路径
    import os
    path = path.strip()
    path = path.rstrip('\\')
    os.makedirs(path)


create("D:\\pixiv box")  # 创建总文件夹pixiv box
Error = []  # 创建错误列表
for i in range(1, 13):
    list_url = "https://pixivbox.top/index.php/page/{}/".format(
        i)  # 构建列表url,一共有11�?
    # print(list_url)
    headers = {
        "Referer":
        "https://pixivbox.top/index.php/archives/143/",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
    }  # 构造请求头
    list_response = requests.get(list_url, headers=headers)
    list_html = list_response.content.decode()  # 获取每列表的网页源代�?
    # print(list_html)
    element_html = etree.HTML(list_html)  # 使用xpath提取数据
    html_url = element_html.xpath(
        "//a[@class ='item-link']/@href")  # 提取每列表专辑网址
    name = element_html.xpath(
        "//div[@class='item-link-text']//text()")  # 提取每列表专辑名�?
    number = element_html.xpath(
        "//span[@class='item-num']//text()")  # 提取每列表专辑图片数�?
    number = re.findall(r'[0-9]{1,3}', str(number))  # 使用正则表达式再提取数量数据
    # print(number)
    for k in range(len(html_url)):
        create("D:\\pixiv box\\{}".format(name[k]))  # 创建分文件夹
        html_response = (requests.get(
            html_url[k], headers=headers)).content.decode()  # 获取各专辑网页源代码
        element = etree.HTML(html_response)
        img_url = element.xpath(
            "//div[@class='post-item col-xs-6 col-sm-4 col-md-3 col-lg-2']//@data-src"
        )  # 提取每个专辑的图片url
        # print(img_url)
        # print(type(number[k]))  str
        # print(int(number[k])+1)
        try:
            for j in range(0, int(number[k])):
                img = (requests.get(
                    img_url[j],
                    headers=headers,
                )).content  # 设置延迟参数3�?
                path = "D:\\pixiv box\\{}\\{}.jpg".format(
                    name[k], (str(j + 1)).zfill(2))  # zfill数字补零
                with open(path, 'wb') as f:
                    f.write(img)
            print(name[k] + " is OK!")
        except Exception:
            Error.append(name[k])  # 记录无用的分文件�?
            print(name[k] + " is Error!")
print(Error)
