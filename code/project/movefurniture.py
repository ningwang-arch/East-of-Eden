class furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area


class home():
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture = []

    def add_furniture(self, item):
        if (self.free_area >= item.area):
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print("无法容纳")

    def __str__(self):
        return f'房子位于{self.address},占地面积{self.area},剩余面积{self.free_area},家具有{self.furniture}'


bed = furniture('bed', 6)
sofa = furniture('sofa', 10)

home1 = home('nothing', 1000)
home1.add_furniture(bed)
print(home1)
home1.add_furniture(sofa)
print(home1)
temp = furniture('test', 1000)
home1.add_furniture(temp)
print(home1)
