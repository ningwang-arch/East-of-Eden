import os
import student


class studentManage(object):
    def __init__(self):
        # 存储数据所用列表
        self.student_list = []

    # 一 . 程序入口函数, 启动后执行的函数
    def run(self):
        # 1. 加载信息
        self.load_Student()
        while (True):
            # 显示功能菜单
            self.showMenu()
            # 用户输入功能序号
            menu_num = int(input('输入功能序号:'))
            # 根据用户输入执行不同功能
            if (menu_num == 1):
                # 添加
                self.add_Student()
            elif (menu_num == 2):
                # 删除
                self.del_Student()
            elif (menu_num == 3):
                # 修改
                self.modify_Student()
            elif (menu_num == 4):
                # 查询
                self.search_Student()
            elif (menu_num == 5):
                # 显示所有
                self.show_Student()
            elif (menu_num == 6):
                # 保存
                self.save_Student()
            elif (menu_num == 0):
                # 退出
                print('是否保存所有修改后退出(y/n)?')
                if (input() == 'y' or input() == 'Y'):
                    self.save_Student()
                break
            else:
                print('无效输入')
            os.system('pause')
            os.system('cls')

    # 二 系统功能函数
    # 显示功能菜单
    @staticmethod
    def showMenu():
        print('请选择如下功能:')
        print('1.添加信息')
        print('2.删除信息')
        print('3.修改信息')
        print('4.查询信息')
        print('5.显示所有信息')
        print('6.保存信息')
        print('0.退出系统')

    # 添加
    def add_Student(self):
        # print('添加信息')
        # 输入姓名 性别 手机号
        name = input('请输入姓名:')
        gender = input('请输入性别:')
        tel = input('请输入手机号:')
        # 创建学生对象
        studentInfo = student.student(name, gender, tel)
        # 将该对象添加至列表
        for i in self.student_list:
            if (i.name == name):
                print('已有此人,无法添加')
                break
        else:
            self.student_list.append(studentInfo)
            print('添加成功')
        # print(self.student_list)
        # print(studentInfo)

    # 删除
    def del_Student(self):
        # print('删除信息')
        # 输入删除目标姓名
        del_name = input('请输入要删除的姓名:')
        # 遍历列表,存在则删除,不存在提示
        for i in self.student_list:
            if (i.name == del_name):
                # 删除该对象
                self.student_list.remove(i)
                print('删除成功')
                break
        else:
            # 正常结束提示不存在
            print('查无此人')
        # print(self.student_list)

    # 修改
    def modify_Student(self):
        # print('修改信息')
        # 输入修改的姓名
        modify_name = input('请输入要修改的姓名:')
        # 遍历 存在则修改 不存在则提示
        for i in self.student_list:
            if (i.name == modify_name):
                i.name = input('请输入修改后的姓名:')
                i.gender = input('请输入修改后的性别:')
                i.tel = input('请输入修改后的手机号:')
                print('修改成功')
                print(f'姓名:{i.name},性别:{i.gender},电话号码:{i.tel}')
                break
        else:
            print('查无此人')

    # 查询
    def search_Student(self):
        # print('查找信息')
        # 输入查询目标姓名
        search_name = input('请输入查询目标姓名:')
        # 遍历 存在则输出 不存在则提示
        for i in self.student_list:
            if (i.name == search_name):
                print(f'姓名:{i.name},性别:{i.gender},电话号码:{i.tel}')
                break
        else:
            print('查无此人')

    # 显示所有信息
    def show_Student(self):
        print('显示所有信息')
        print(f'姓名\t性别\t电话号码')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    # 保存
    def save_Student(self):
        # print('保存所有信息')
        # 打开文件
        f = open('student.data', mode='w')
        # 写入数据
        # 对象装换为字典数据
        new_list = [i.__dict__ for i in self.student_list]
        # 文件以字符串写入
        f.write(str(new_list))
        # 关闭文件
        f.close()

    # 加载信息
    def load_Student(self):
        # print('加载信息')
        # 尝试以'r'模式打开,若有异常,以'w'打开
        try:
            f = open('student.data', mode='r')
        except Exception:
            f = open('student.data', mode='w')
        else:
            data = f.read()
            new_list = eval(data)
            self.student_list = [
                student.student(i['name'], i['gender'], i['tel'])
                for i in new_list
            ]
        finally:
            f.close()
