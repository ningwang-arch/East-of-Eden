import time
import requests
import os
Error = []
headers = {
    'cookie':
    '__cfduid=d4174d29c11fb1c9afe7bea60f12984aa1592793036',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
}
f = open('gif_imgs.txt', 'r')
lines = f.readlines()
for line in lines:
    name = str(int(time.time()))
    line = line.strip('\n')
    r = requests.get(line, headers=headers, stream=True)
    chunk_size = 128
    content_size = int(r.headers['content-length'])
    size = 0
    print("文件大小：" + str(round(float(content_size / 1024 / 1024), 4)) + "[MB]")
    try:
        path = "D:\\testpic\\{}.gif".format(name)
        with open(path, 'wb') as image:
            # r = r.content
            for chunk in r.iter_content(chunk_size=chunk_size):
                image.write(chunk)
                size = len(chunk) + size
                print('\r' + "已经下载：" + int(size / content_size * 100) * "█" +
                      " 【" + str(round(size / 1024 / 1024, 2)) + "MB】" + "【" +
                      str(round(float(size / content_size) * 100, 2)) + "%" +
                      "】",
                      end="")
        end = time.time()
        os.system('cls')
    except Exception:
        Error.append(line)
print(Error)
