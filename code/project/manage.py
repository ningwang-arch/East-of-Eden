import os


# 打印功能选项
def info_print():
    print('-' * 20)
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员')
    print('4.查询学员')
    print('5.显示所有学员')
    print('0.退出系统')
    print('-' * 20)


info = []


# 添加功能
def add_info():
    new_id = input("请输入学号:")
    new_name = input('请输入姓名:')
    new_tel = input('请输入电话号码:')
    global info
    for i in info:
        if i['name'] == new_name:
            print('用户已存在,添加失败')
            return

    info_dict = {}

    info_dict['id'] = new_id
    info_dict['name'] = new_name
    info_dict['tel'] = new_tel

    info.append(info_dict)
    print('添加成功!')
    # print(info)


# 删除功能
def del_info():
    del_name = input('请输入要删除名字:')
    global info
    for i in info:
        if (i['name'] == del_name):
            info.remove(i)
            print('删除成功')
    else:
        print("查无此人,无法删除")


# 修改功能
def modify_info():
    modify_name = input('请输入要修改的成员姓名:')

    global info

    for i in info:
        if (i['name'] == modify_name):
            i['tel'] = input('请输入修改后的电话号码:')
            print('修改成功')
            break
    else:
        print("查无此人,修改失败!")


# 查询功能
def search_info():
    search_name = input('请输入要查询的成员姓名:')
    global info
    for i in info:
        if (i['name'] == search_name):
            print('查询信息如下:')
            print(f"学号: {i['id']}\n姓名: {i['name']}\n电话号码: {i['tel']}")
            break
    else:
        print('查无此人')


# 显示所有成员
def print_all():
    print('学号\t姓名\t电话号码')
    global info
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['tel']}")


# 主函数
while (True):
    info_print()
    user_num = int(input('请输入功能序号:'))
    print()

    if user_num == 1:
        print("添加")
        add_info()
        # print(info)
    elif user_num == 2:
        print('删除')
        del_info()
        # print(info)
    elif user_num == 3:
        print('修改')
        modify_info()
        # print(info)
    elif user_num == 4:
        # print('查询')
        search_info()
    elif user_num == 5:
        # print('显示所有')
        print_all()
    elif user_num == 0:
        # print("退出")
        break
    os.system('pause')
    os.system("cls")
