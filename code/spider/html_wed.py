import re
import urllib.request


def get_content(url):
    html = urllib.request.urlopen(url)
    print("读取中...")
    try:
        content = html.read().decode(
            'utf-8')  # 此处根据抓取网站不同解码方式也不一样，有些是.decode('gbk')
    except UnicodeDecodeError:
        content = html.read().decode(
            'gbk')  # 此处根据抓取网站不同解码方式也不一样，有些是.decode('gbk')
    html.close()
    return content


def get_images(info):
    src = r'<img class="BDE_Image" src="(.+?\.jpg)"'
    comp = re.compile(src)
    get_codes = re.findall(comp, info)
    i = 1
    print("[正在捕获...]")
    for get_code in get_codes:
        urllib.request.urlretrieve(get_code, r'D:\\AXM\%s.jpg' % i)
        i = i + 1
        print("[1][%s.jpg/png]" % i)
    print("[捕获完毕][一共%s项" % i)


URL = str(input("网页链接:"))
info = get_content('%s' % URL)
get_images(info)
