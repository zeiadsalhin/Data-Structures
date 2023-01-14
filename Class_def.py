class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eating(self):
        print(self.name, "is eating")


ob1 = person("Amr", 18)
print(ob1.name)
print(ob1.age)
ob1.eating()


class car:
    def __init__(self, color, type):
        self.color = color
        self.type = type

    def running(self):
        print(self.color, "car is running")


car1 = car("Blue", "bmw")
print(car1.color)
print(car1.type)
car1.running()
