import requests
import json
headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}
i = 0
while True:
    url = 'https://www.zhihu.com/api/v4/topics/19868718/feeds/top_activity?limit=10&after_id={}.00000'.format(
        i)
    i += 10
    reponse = requests.get(url, headers=headers)
    # print(response)
    data = json.loads(reponse.content.decode())['data']
    if not data:
        break
    # print(data)
    for item in data:
        question_title_id_dict = {}
        if 'question' in item['target']:
            # print(item)
            question_title_id_dict['title'] = item['target']['question'][
                'title']
            question_title_id_dict['id'] = item['target']['question']['id']
            with open('zhihu_question_id.txt', 'a', encoding='utf-8') as f:
                f.write(
                    json.dumps(question_title_id_dict,
                               ensure_ascii=False,
                               indent=2))
                f.write('\n')
# print(len(question__title_id_list))
