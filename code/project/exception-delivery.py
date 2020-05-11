class shortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    def __str__(self):
        return f'你输入的长度为{self.length},长度不能少于{self.min_len}个字符'


def main():
    try:
        content = input("请输入密码:")
        if (len(content) < 3):
            raise shortInputError(len(content), 3)
    except Exception as result:
        print(result)
    else:
        print('no error')


main()
