class master(object):
    def __init__(self):
        self.kongfu = '[nothing-first]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作')


class school(object):
    def __init__(self):
        self.kongfu = '[nothing-second]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作')

        # super().__init__()
        # super().make_cake()


class prentice(school, master):
    def __init__(self):
        self.kongfu = '[nothing-third]'
        self.__money = 1000000

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

    def __info_print(self):
        pass

    def make_cake(self):  # nothing-third
        self.__init__()
        print(f'运用{self.kongfu}制作')

    def make_master_cake(self):  # nothing-first
        master.__init__(self)
        master.make_cake(self)

    def make_school_cake(self):  # nothing-second
        school.__init__(self)
        school.make_cake(self)

    def make_old_cake(self):
        # 方法一
        """
        master.__init__(self)
        master.make_cake(self)
        school.__init__(self)
        school.make_cake(self)
        """
        super().__init__()
        super().make_cake()


class tusun(prentice):
    pass


daqiu = prentice()
# daqiu.make_old_cake()
# daqiu.make_cake()
# daqiu.make_master_cake()
# daqiu.make_school_cake()
# daqiu.make_cake()
xiaoqiu = tusun()
print(xiaoqiu.get_money())
xiaoqiu.set_money(1000)
print(xiaoqiu.get_money())
# xiaoqiu.__info_print()
# xiaoqiu.make_cake()
# xiaoqiu.make_master_cake()
# xiaoqiu.make_school_cake()
