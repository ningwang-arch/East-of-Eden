import requests
import time
from lxml import etree
from queue import Queue
import logging
import os
import re
import threading

logging.basicConfig(filename='/home/eclipse/Pictures/alpha.log',
                    level=logging.INFO,
                    format='%(asctime)s %(filename)s %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    filemode="w")

proxies = {
    'http': 'http://127.0.0.1:8889',
    'https': 'http://127.0.0.1:8889'
}  # This can be modified to your own proxy settings


headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}


class Spider:
    def __init__(self) -> None:
        self.base_path = '/the/path/you/choose/'
        self.base_url = 'https://wall.alphacoders.com/'
        self.headers = headers.copy()
        self.proxies = proxies
        self.categories = Queue()
        self.sub_info = Queue()
        self.create_path(self.base_path)

    def create_path(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def get_categories(self):
        """
        Get category link
        """
        response = requests.get(
            self.base_url, headers=self.headers, proxies=self.proxies)
        html = response.content.decode()
        element = etree.HTML(html)
        categories = element.xpath('//*[@id="categories"]/a//@href')
        # https://wall.alphacoders.com/by_category.php?id=1&name=Abstract+Wallpapers
        for _ in categories:
            url = self.base_url+_
            # print(url)
            self.categories.put(url)

    def get_page_num(self, url):
        """
        Get the number of pages
        """
        response = requests.get(
            url, headers=self.headers, proxies=self.proxies)
        html = response.content.decode()
        element = etree.HTML(html)
        page_num = int(element.xpath(
            '//*[@id="page_container"]/div[8]/div[2]/ul/li[10]/a/text()')[0])
        return page_num

    def get_sub_urls(self, url):
        """
        Build subpage information with links and categories
        """
        try:
            page_num = self.get_page_num(url)
            category = re.findall('name=(.+?)\+Wallpapers', url)[0]
            # https://wall.alphacoders.com/by_category.php?id=25&name=Products+Wallpapers&page=1
            for i in range(1, page_num+1):
                sub_url = url+('&page={}'.format(i))
                info = {'sub_url': sub_url, 'category': category}
                self.sub_info.put(info)
        except Exception:
            logging.info(url)

    def get_pictures_url(self, sub_url):
        """
        Get the picture link in a page
        """
        pics = []
        try:
            response = requests.get(
                sub_url, headers=self.headers, proxies=self.proxies)
            html = response.content.decode()
            element = etree.HTML(html)
            pics = element.xpath(
                '//div[@class="boxgrid"]/a/img//@src')
            pics = [_.replace('thumb-350-', '') for _ in pics]
        except Exception:
            logging.info(sub_url)
        return pics

    def keep_pics(self, path, pics=[]):
        """
        save the picture
        """
        for pic in pics:
            try:
                img = requests.get(pic, headers=self.headers,
                                   proxies=self.proxies)
                name = int(time.time()*100)
                sub_path = path+('{}.png'.format(name))
                with open(sub_path, 'wb') as f:
                    f.write(img.content)
            except Exception:
                logging.info(pic+(' target_path={}'.format(path)))

    def keep_one_page(self, info):
        """
        keep pictures or urls by category
        """
        category = info['category']
        sub_url = info['sub_url']
        pics = self.get_pictures_url(sub_url)

        # If you want to save the picture
        sub_path = self.base_path+('{}/'.format(category))
        self.create_path(sub_path)
        self.keep_pics(sub_path, pics)

        # If you just want to save the image link
        # text_path = self.base_path+('{}.txt'.format(category))
        # self.keep_urls(text_path, pics)

    def keep_urls(self, text_path, pics=[]):
        """
        save the image link
        """
        for _ in pics:
            with open(text_path, 'a+') as f:
                f.write(_)
                f.write('\n')

    def get_all_sub_info(self):
        while True:
            if self.categories.empty():
                break

            category_url = self.categories.get()
            self.get_sub_urls(category_url)
            self.categories.task_done()

    def keep_all(self):
        while True:
            info = self.sub_info.get()
            self.keep_one_page(info)
            self.sub_info.task_done()

    def run(self):
        thread_list = []
        self.get_categories()

        for i in range(5):
            t_info = threading.Thread(target=self.get_all_sub_info)
            thread_list.append(t_info)
        for i in range(32):
            t_keep = threading.Thread(target=self.keep_all)
            thread_list.append(t_keep)

        for thread in thread_list:
            thread.setdaemon = True
            thread.start()


if __name__ == '__main__':
    spider = Spider()
    spider.run()
