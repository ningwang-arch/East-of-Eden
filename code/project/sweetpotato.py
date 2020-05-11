class sweetPotato():
    def __init__(self):
        self.cook_time = 0
        self.cook_status = 'raw'
        self.condiments = []

    def cook(self, time):
        self.cook_time += time
        if (0 <= self.cook_time < 3):
            self.cook_status = 'raw'
        elif (3 <= self.cook_time < 5):
            self.cook_status = 'half-baked'
        elif (5 <= self.cook_time < 8):
            self.cook_status = 'cooked'
        else:
            self.cook_status = 'bake'

    def add_condiments(self, condiments):
        self.condiments.append(condiments)

    def __str__(self):
        return f"被烤过的时间为{self.cook_time},状态是{self.cook_status},调料有{self.condiments}"


digual = sweetPotato()
print(digual)

digual.cook(2)
digual.add_condiments('皮卡丘')
print(digual)

digual.cook(2)
digual.add_condiments('nothing')
print(digual)
