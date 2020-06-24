# @Author: eclipse
# @Date: 2020-06-24 10:36:43
# @Last Modified by:   eclipse
# @Last Modified time: 2020-06-24 10:36:43

import requests
from lxml import etree
import time
import ffmpeg.video
import os
headers = {
    'origin':
    'https://www.bilibili.com',
    'referer':
    'https://www.bilibili.com/v/douga/mmd/',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
}


class BiliSpider():
    def __init__(self, api):
        self.api = api

    def get_page_urls(self, api):
        response = requests.get(api, headers=headers)
        html = response.content.decode()
        html = eval(html)
        archives = html['data']['archives']
        aid = [i['aid'] for i in archives]
        page_urls = ['https://www.bilibili.com/video/av' + str(i) for i in aid]
        return page_urls

    def get_video_audio_url(self, video_url):
        response = requests.get(video_url, headers=headers)
        html = response.content.decode()
        element = etree.HTML(html)
        need_element = eval(
            str(element.xpath('/html/head/script[3]/text()')[0])
            [20:])['data']['dash']
        video_url = need_element['video'][0]["baseUrl"]
        audio_url = need_element['audio'][0]["baseUrl"]
        return video_url, audio_url

    def download_video_audio(self, video_url, audio_url):
        name = str(int(time.time()))
        video_path = "D:\\testvideo\\{}.mp4".format(name)
        audio_path = "D:\\testvideo\\{}.mp3".format(name)
        # 这里的path路径自定义,不过建议video和audio名称一致,便于区分
        self.save_content(video_url, video_path)
        self.save_content(audio_url, audio_path)
        output_path = "D:\\testvideo\\{}.mp4".format(str(int(time.time())))
        self.combine_video_audio(video_path, audio_path, output_path)
        os.remove(video_path)
        os.remove(audio_path)

    def save_content(self, url, path):
        session = requests.session()
        session.options(url=url, headers=headers)
        res = session.get(url=url, headers=headers, stream=True)
        chunk_size = 1024
        size = 0
        content_size = int(res.headers['content-length'])
        print("文件大小：" + str(round(float(content_size / 1024 / 1024), 4)) +
              "[MB]")
        with open(path, 'wb') as content:
            for chunk in res.iter_content(chunk_size=chunk_size):
                content.write(chunk)
                size = len(chunk) + size
                print('\r' + "已经下载：" + int(size / content_size * 100) * ">" +
                      " 【" + str(round(size / 1024 / 1024, 2)) + "MB】" + "【" +
                      str(round(float(size / content_size) * 100, 2)) + "%" +
                      "】",
                      end="")

    def combine_video_audio(self, video_path, audio_path, output_path):
        ffmpeg.video.combine_audio(video_path, audio_path, output_path)

    def run(self):
        page_urls = self.get_page_urls(self.api)
        i = 0
        for page_url in page_urls:
            video_url, audio_url = self.get_video_audio_url(page_url)
            self.download_video_audio(video_url, audio_url)
            i += 1
            if (i == 3):
                break


api = 'https://api.bilibili.com/x/tag/ranking/archives?tag_id=3274&rid=25&type=0&pn=1&jsonp=jsonp'
# api中可改变的部分为tag_id和pn  tag_id为你选择的标签,pn为第几页
# 比如说我选择的分区链接是 https://www.bilibili.com/v/douga/mmd/#/3274 那么tag_id就是3274
spider = BiliSpider(api)
spider.run()
'''
本程序中combine_video_audio函数使用了ffmpeg模块,需要预先下载exe程序并添加至path  官网链接为https://ffmpeg.zeranoe.com/builds/
同时python需要下载ffmpeg模块,并在ffmpeg.video模块中添加如下音视频组合函数:

def combine_audio(video_file, audiio_file, out_file):
    try:
        cmd ='(path) -i '+video_file+' -i '+audiio_file+' -acodec copy '+out_file
                    #path是你自己的ffmpeg路径,比如我的路径为D:/ffmpeg-4.2.  3-win64-static/bin/ffmpeg
        print(cmd)
        subprocess.call(cmd, shell=True)  # "Muxing Done
        print('Muxing Done')
        if res != 0:
            return False
        return True
    except Exception:
        return False

如果你选择使用格式工厂之类的应用自行组合,可以在程序中删除51-54行,75-76行
'''
