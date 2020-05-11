import requests
import re
import urllib.request
from bs4 import BeautifulSoup


def img(html, input_le):
    i = 0
    for y in input_le:
        soup = BeautifulSoup(html.content, 'html.parser')
        p = soup.select(y)
        print("[正在捕获...]")
        for x in p:
            x = str(x)
            pe = 'https:'
            get_codes = re.findall(r'src="(.+?g)"', x)
            for get_code in get_codes:
                i += 1
                if pe in get_code:
                    urllib.request.urlretrieve(get_code, r'E:\\AXM\%s.jpg' % i)
                    print("[1][%s.jpg/png]" % i)
                else:
                    urllib.request.urlretrieve(pe + get_code,
                                               r'E:\\AXM\%s.jpg' % i)
                    print("[1][%s.jpg/png]" % i)
    print("[捕获完毕][一共%s项]" % i)


def p(html, input_le):
    i = 0
    for y in input_le:
        soup = BeautifulSoup(html.content, 'html.parser')
        p = soup.select(y)
        for x in p:
            i += 1
            print(">>>:" + "%s" % i)
            print("[", x, "]")


def pan(html, input_le):
    i = 0
    for y in input_le:
        soup = BeautifulSoup(html.content, 'html.parser')
        p = soup.select(y)
        print("[正在捕获...]")
        for x in p:
            x = str(x)
            pe = 'https:'
            get_codes = re.findall(r'src="(.+?g)"', x)
            for get_code in get_codes:
                i += 1
                if pe in get_code:
                    urllib.request.urlretrieve(get_code, r'E:\\AXM\%s.jpg' % i)
                    print("[1][%s.jpg/png]" % i)
                else:
                    urllib.request.urlretrieve(pe + get_code,
                                               r'E:\\AXM\%s.jpg' % i)
                    print("[1][%s.jpg/png]" % i)


C1 = 'img'
print("-----爬虫控制面板----")
print("可用选项: /run(运行),/stop(退出系统)")
while True:
    sr = input(">>>:")
    if sr == "/run":
        Newurl = str(input("网页URL:"))
        input_l = "," + str(input("筛选的标签"))
        html = requests.get(Newurl)
        input_le = re.findall(r",(.+)", input_l)
        if C1 in input_le:
            img(html, input_le)
        elif C1 in input_le:
            img(html, input_le)
            if len(input_le) > 1:
                p(html, input_le)
        else:
            p(html, input_le)
    elif sr == "/stop":
        break
