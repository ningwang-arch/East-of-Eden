import requests
import time
import threading
from queue import Queue
from lxml import etree


class ComicSpider(object):
    def __init__(self, temp_url):
        self.temp_url = temp_url
        self.headers = {
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'referer':
            'https://i.acg.blue/explore/recent/?list=users&sort=date_desc&page=1'
        }
        self.url_queue = Queue()
        self.html_queue = Queue()
        self.content_queue = Queue()

    def get_url_list(self):
        for i in range(1, 11):
            self.url_queue.put(self.temp_url.format(i))

    def parse_content_list(self):
        while True:
            url = self.url_queue.get()
            response = requests.get(url, self.headers)
            content = response.content.decode()
            self.html_queue.put(content)
            self.url_queue.task_done()

    def get_imgs_url_list(self):
        while True:
            html_str = self.html_queue.get()
            html = etree.HTML(html_str)
            temp_urls = html.xpath(
                '//*[@id="list-recent-images"]/div[1]/div/div[1]/a/img//@src')
            imgs_list = [i.replace('md.', '') for i in temp_urls]
            self.content_queue.put(imgs_list)
            self.html_queue.task_done()

    def get_imgs_content(self, url):
        img = requests.get(url, headers=self.headers).content
        return img

    def save_url(self):
        while True:
            imgs_list = self.content_queue.get()
            for img_url in imgs_list:
                name = str(int(time.time()))
                path = "D:\\testpic\\{}.jpg".format(name)
                with open(path, 'wb') as f:
                    img = self.get_imgs_content(img_url)
                    f.write(img)
            self.content_queue.task_done()

    def run(self):
        thread_list = []

        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)

        for i in range(3):
            t_parse = threading.Thread(target=self.parse_content_list)
            thread_list.append(t_parse)

        for i in range(3):

            t_html = threading.Thread(target=self.get_imgs_url_list)
            thread_list.append(t_html)

        for i in range(20):
            t_save = threading.Thread(target=self.save_url)
            thread_list.append(t_save)

        for t in thread_list:
            t.setdaemon = True
            t.start()
        for q in [self.url_queue, self.html_queue, self.content_queue]:
            q.join()


url_temp = 'https://i.acg.blue/explore/recent/?list=images&sort=date_desc&page={}'
comicspider = ComicSpider(url_temp)
comicspider.run()
