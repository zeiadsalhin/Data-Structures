class stack:
    def __init__(self):
        self.s = []

    def push(self, value):
        self.s.append(value)
        value=[1]
    def pop(self):
        if self.isEmpty():
            print("Error")
        else:
         self.s.pop()

    def isEmpty(self):
        if len(self.s) == 0:
            return True
        else:
            return False

    def top(self):
        if self.isEmpty():
            print("Error")
        else:
         return self.s[-1]

stack= stack()
x=input("enter")
print(stack,x)