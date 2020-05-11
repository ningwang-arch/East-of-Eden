old_name = input('Please enter the name of the file you want to backup:')
# print(old_name)
# print(type(old_name))
index = old_name.rfind('.')
# print(index)
if (index > 0):
    postfix = old_name[index:]
# print(old_name[:index])
new_name = old_name[:index] + '[backup]' + postfix
# print(new_name)

old_f = open(old_name, 'rb')
new_f = open(new_name, 'wb')

while (True):
    con = old_f.read(1024)
    if (len(con) == 0):
        break
    new_f.write(con)

old_f.close()
new_f.close()
