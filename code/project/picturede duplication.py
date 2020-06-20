import os
import hashlib
temp_path = input('请将要去重的文件夹路径复制至此处:')
filePath = temp_path.replace('\\', '\\\\')
item_names_list = os.listdir(filePath)
hash_dict = {}
for item in item_names_list:
    file = open(filePath + '\\{}'.format(item), 'rb')
    file = file.read()
    ret = hashlib.md5(file).hexdigest()
    hash_dict[item] = ret

values = set()
items_del = []
for key in hash_dict.keys():
    val = hash_dict[key]
    if val in values:
        items_del.append(key)
    else:
        values.add(val)

for item_del in items_del:
    os.remove(filePath + '\\{}'.format(item_del))
