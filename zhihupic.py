import requests
import json
from lxml import etree
import os
import time
import urllib
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
total_path = 'D:/zhihupic'
if not os.path.exists(total_path):
    os.makedirs(total_path)
Error = []


def zhihuPicSpider(question_name_id_type_dict):
    question_name = question_name_id_type_dict['name']
    question_id = question_name_id_type_dict['id']
    question_type = question_name_id_type_dict['type']
    if question_type == 'question':
        downloadQuestionPic(question_name, question_id)
    elif question_type == 'article':
        downloadArticlePic(question_name, question_id)
    elif question_type == 'topic':
        downloadTopicPic(question_id)


def downloadQuestionPic(question_name, question_id):
    i = 0
    pic_path = total_path + ('/{}'.format(question_name))
    if not os.path.exists(pic_path):
        os.makedirs(pic_path)
    while True:
        url = 'https://www.zhihu.com/api/v4/questions/{}/answers?limit=5&offset={}'.format(
            question_id, i)
        i += 5
        response = requests.get(url, headers=headers)
        content = json.loads(response.content.decode())['data']
        if not content:
            break
        answer_ids = [item['id'] for item in content]
        for answer_id in answer_ids:
            answer_url = 'https://www.zhihu.com/question/{}/answer/{}'.format(
                question_id, answer_id)
            r = requests.get(answer_url, headers=headers)
            html = r.content.decode()
            element = etree.HTML(html)
            pic_urls = element.xpath('//noscript/img//@src')
            for pic_url in pic_urls:
                name = int(time.time() * 10)
                path = pic_path + ('/{}.jpg').format(name)
                try:
                    urllib.request.urlretrieve(pic_url, path)
                except Exception:
                    Error.append(pic_url)
    print(Error)


def downloadArticlePic(question_name, question_id):
    pic_path = total_path + ('/{}'.format(question_name))
    headers = {
        'cookie':
        'd_c0="APCXZd6qohGPTmue1c1c7hfx3Hud6CL6mKQ=|1595754204";',
        'origin':
        'https://zhuanlan.zhihu.com',
        'referer':
        'https://zhuanlan.zhihu.com/52dmtp',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    }
    url = 'https://zhuanlan.zhihu.com/p/{}'.format(question_id)
    res = requests.get(url, headers=headers)
    print(res)
    html = res.content.decode()
    element = etree.HTML(html)
    imgs_url = element.xpath('//figure/noscript/img//@data-original')
    if not os.path.exists(pic_path):
        os.makedirs(pic_path)
    for img_url in imgs_url:
        name = str(int(time.time() * 10))
        path = pic_path + ('/{}.jpg'.format(name))
        try:
            urllib.request.urlretrieve(img_url, path)
        except Exception:
            Error.append(img_url)
    print(Error)


def downloadTopicPic(question_id):
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
    }
    i = 0
    while True:
        url = 'https://www.zhihu.com/api/v4/topics/{}/feeds/top_activity?limit=10&after_id={}.00000'.format(
            question_id, i)
        i += 10
        reponse = requests.get(url, headers=headers)
        # print(response)
        data = json.loads(reponse.content.decode())['data']
        if not data:
            break
        # print(data)
        for item in data:
            if 'target' in item:
                target = item['target']
                question_name_id_type_dict = {}
                if 'type' in target:
                    if target['type'] == 'answer':
                        question_name_id_type_dict['name'] = target[
                            'question']['title'].replace('<em>', '').replace(
                                '</em>', '')
                        question_name_id_type_dict['id'] = target['question'][
                            'id']
                        question_name_id_type_dict['type'] = 'question'
                    elif target['type'] == 'article':
                        question_name_id_type_dict['name'] = target[
                            'title'].replace('<em>', '').replace('</em>', '')
                        question_name_id_type_dict['id'] = target['id']
                        question_name_id_type_dict['type'] = 'article'
                    else:
                        continue
                else:
                    continue
            zhihuPicSpider(question_name_id_type_dict)
            # print(question_name_id_type_dict)


if __name__ == '__main__':
    question_name_id_type_dict = {
        'name': '',  # 问题名称或者随便写,主要为分文件夹提供便利
        'id': 0,  # 问题的ID,自行查找
        'type':
        '',  # 问题类别 question/topic/article (question:问题 topic:话题 article:专栏文章)
    }
    zhihuPicSpider(question_name_id_type_dict)
