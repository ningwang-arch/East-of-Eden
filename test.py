import requests
from lxml import etree
import re

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
}

print('\n')
print('*' * 20, '1：下载单个视频', '*' * 20)
print('*' * 20, '2：下载系列专辑视频(支持多集数)', '*' * 20)
print('\n')

number = int(input('请输入你要爬取的视频系列：'))


def download_single_video():  # 下载单个视频

    avnumber = input(
        '请输入av/bv号：'
    )  # https://www.bilibili.com/video/BV1AT4y137NH?spm_id_from=333.851.b_7265706f7274466972737432.4
    video_path = input(r'请输入保存文件的绝对路径(文件夹)：')
    video_url = 'https://www.bilibili.com/video/%s' % avnumber
    data = {'bilibiliurl07255': video_url, 'zengqiang': 'true'}

    res = requests.post('https://xbeibeix.com/api/bilibili/',
                        data=data,
                        headers=headers)
    print(res.text)
    xml = etree.HTML(res.text)

    title = xml.xpath('//div[@class="input-group mb-2"]/input/@value')[
        0]  # 获取标题
    mp4_url = xml.xpath('//textarea[@class="form-control"]/text()')[
        1]  # 会跳转到一个新网页，此页面播放视频
    print("mp4_url" + mp4_url)
    mp4urls = re.sub('http://upos-hz-mirrorakam.akamaized.net',
                     'http://upos-sz-mirrorcos.bilivideo.com', mp4_url)
    print("mp4urls" + mp4urls)

    print('正在下载：', title)

    res = requests.get(mp4urls, headers=headers)

    with open(file=str(video_path + '/') + title + '.mp4', mode='wb') as f:
        f.write(res.content)
        f.close()
        print('下载完成：', title)


def download_multiple_video():  # 下载多个视频
    avnumber = input('请输入av/bv号：')
    video_number = int(input('请输入要下载的集数(输入最后一集的集数)：'))
    video_path = input('请输入保存文件的绝对路径：')

    for page in range(1, video_number + 1):
        video_url = 'https://www.bilibili.com/video/%s?p=%d' % (avnumber, page)

        data = {'bilibiliurl07255': video_url, 'zengqiang': 'true'}

        res = requests.post('/', data=data, headers=headers)

        xml = etree.HTML(res.text)

        title = xml.xpath(
            '//div[@class="input-group mb-2"]//input[1]/@value')[0]

        print(title)

        # mp4_url = xml.xpath('//div[@class="input-group mb-2"]//span/a/@href')[1]
        mp4_url = xml.xpath('//textarea[@class="form-control"]/text()')[1]

        mp4urls = re.sub('http://upos-hz-mirrorakam.akamaized.net',
                         'http://upos-sz-mirrorcos.bilivideo.com', mp4_url)
        print('正在下载：', title)
        res = requests.get(mp4urls, headers=headers)

        with open(file=str(video_path + '/') + title + '.mp4', mode='wb') as f:
            f.write(res.content)
            f.close()
            print('下载完成：', title)


# BV1AT4y137NH

if number == 1:
    download_single_video()

elif number == 2:
    download_multiple_video()
