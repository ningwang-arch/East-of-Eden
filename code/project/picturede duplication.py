import os
import hashlib
filePath = 'D:\\testpic'
img_names_list = os.listdir(filePath)
hash_dict = {}
for img in img_names_list:
    file = open('D:\\testpic\\{}'.format(img), 'rb')
    file = file.read()
    ret = hashlib.md5(file).hexdigest()
    hash_dict[img] = ret

values = set()
imgs_del = []
for key in hash_dict.keys():
    val = hash_dict[key]
    if val in values:
        imgs_del.append(key)
    else:
        values.add(val)

for img_del in imgs_del:
    os.remove('D:\\testpic\\{}'.format(img_del))
