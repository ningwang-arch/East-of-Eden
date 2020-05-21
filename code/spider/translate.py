# @Author: eclipse
# @Date: 2020-05-20 14:29:59
# @Last Modified by:   eclipse
# @Last Modified time: 2020-05-20 14:29:59


def getSalt():
    import time
    import random
    salt = int(time.time() * 1000) + random.randint(0, 10)
    return salt


def getMD5(content):
    import hashlib
    md5 = hashlib.md5()
    md5.update(content.encode('utf-8'))
    sign = md5.hexdigest()
    return sign


def getSign(word, salt):
    sign = "fanyideskweb" + word + str(salt) + "Nw(nmmbP%A-r6U3EUn]Aj"
    sign = getMD5(sign)
    return sign


def translation(word, language):
    import requests
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    salt = getSalt()
    formdata = {
        'i': word,
        'from': 'AUTO',
        'to': language,
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': str(salt),
        'sign': getSign(word, salt),
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }
    header = {
        'Cookie':
        'OUTFOX_SEARCH_USER_ID=-1445086561@10.108.160.19; JSESSIONID=aaaZv91-DK3vGd58b9Vix; OUTFOX_SEARCH_USER_ID_NCOO=1363510956.4233305; ___rl__test__cookies=1589945303642',
        'Referer':
        'http://fanyi.youdao.com/',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    try:
        response = requests.post(url, headers=header, data=formdata)
        result = eval(response.text)
        try:
            result = result['smartResult']['entries']
            while ('' in result):
                result.remove('')
            result = [i.replace('\n', '').replace('\r', '') for i in result]
        except Exception:
            result = result['translateResult'][0][0]['tgt']
            result = [i.replace('\n', '').replace('\r', '') for i in result]
            result = ''.join(result)
    except Exception:
        result = None
    print(result)
    print()


language = {
    '中法': 'fr',
    '中英': 'en',
    '中日': 'ja',
    '中韩': 'ko',
    '中德': 'de',
    '中俄': 're',
    '自动': 'AUTO'
}
print("其他语言翻译为中文请采用自动模式")
print("支持的语言种类:  中英\t中日\t中德\t中法\t中俄\t中韩\t自动")
while (True):
    lang = input("请输入翻译的语言种类(如中英)\\>>>")
    while (True):
        print("请输入你要翻译的内容(输入3901退出当前翻译)")
        content = input("\\>>>")
        if (content == '3901'):
            break
        translation(content, language[lang])
