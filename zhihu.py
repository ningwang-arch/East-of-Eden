import requests
from urllib.parse import urlencode
import execjs
import hashlib
import json


def zhihu_question_id_spider(question):
    i = 0

    while True:
        data = {
            't': 'general',
            'q': question,  # 问题关键字或问题全名称
            'correction': 1,
            'offset': i,
            'limit': 20,
            'lc_idx': 0,
            'show_all_topics': 0,
        }
        i += 20
        refer_data = {'q': data['q']}
        url = "/api/v4/search_v3?" + urlencode(data)

        referer = "https://www.zhihu.com/search?type=content&{}".format(
            urlencode(refer_data))
        f = "+".join([
            "3_2.0", url, referer,
            '"AODaaONMvBGPTkx7RR7NicaHcqzhfD-29LM=|1597474398"'
        ])  # f= x-zse-83+url+referer+'cookie.d_c0'

        fmd5 = hashlib.new('md5', f.encode()).hexdigest()

        with open('g_encrypt.js', 'r') as f:
            ctx1 = execjs.compile(f.read(), cwd='C:/node_modules')
        # print(ctx1)
        encrypt_str = ctx1.call('b', fmd5)

        headers = {
            'cookie':
            'd_c0="AODaaONMvBGPTkx7RR7NicaHcqzhfD-29LM=|1597474398";',
            'referer':
            'https://www.zhihu.com/search?type=content&{}'.format(
                urlencode(refer_data)),
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
            'x-zse-83':
            '3_2.0',
            'x-zse-86':
            '1.0_{}'.format(
                encrypt_str)  # aXY0c7UBSXtpk0tyzwtqFhuBnBFXr72qZqY0reuBrHtx
        }
        # url = 'https://www.zhihu.com/api/v4/search_v3?' + urlencode(data)
        url = 'https://www.zhihu.com' + url
        response = requests.get(url, headers=headers)
        # print(response)
        page_data = json.loads(response.content.decode())['data']
        # print(page_data)
        if not page_data:
            break
        # print(data)
        for item in page_data:
            item_object = item['object']
            question_name_id_dict = {}
            if 'question' in item_object:
                question_name_id_dict['name'] = item_object['question'][
                    'name'].replace('<em>', '').replace('</em>', '')
                question_name_id_dict['id'] = item_object['question']['id']
                # print(question_name_id_dict)
                with open('{}.txt'.format(data['q']), 'a',
                          encoding='utf-8') as f:
                    f.write(
                        json.dumps(question_name_id_dict,
                                   ensure_ascii=False,
                                   indent=2))
                    f.write('\n')


if __name__ == '__main__':
    question = ''
    zhihu_question_id_spider(question)
