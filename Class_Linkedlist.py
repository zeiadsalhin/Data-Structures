class node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextdataval = None


class slinkedlist:
    def __init__(self):
        self.headval = None

    def listprint(self, null=None):
        printable = self.headval
        while printable is not null:
            print(printable.dataval)
            printable = printable.nextdataval

    def atbegining(self, newdata):
        NewNode = node(newdata)
        NewNode.nextval= self.headval
        self.headval = NewNode



list1 = slinkedlist()

list1.headval = node(input("enter last item"))
z=node("mon")
t = node("Tue")
w = node("Wed")
list1.nextdataval = z
list1.nextdataval = t
list1.nextdataval = w
list1.headval.nextdataval= z
z.nextdataval= t
t.nextdataval=w

list1.listprint()
