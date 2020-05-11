class dog(object):
    def work(self):
        print('nothing')


class armyDog(dog):
    def work(self):
        print('nothing-first')


class drugDog(dog):
    def work(self):
        print("nothing-second")


class person(object):
    def work_with_dog(self, dog):
        dog.work()


ad = armyDog()
dd = drugDog()
daqiu = person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)
