class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class slinkedlist:
    def __init__(self):
        self.head = None

    def atbegining(self, data_in):
        NewNode = node(data_in)
        NewNode.next = self.head
        self.head = NewNode

    def removeNode(self, removekey):
        headval = self.head
        if headval is not None:
            if headval.data == removekey:
                self.head = headval.next
                headval = None
                return
        while headval is not None:
            if headval.data == removekey:
                break
            prev = headval
            headval = headval.next

        if headval == None:
            return
        prev.next = headval.next
        headval = None

    def listprint(self):
        printval = self.head
        while printval:
            print(printval.data)
            printval = printval.next


list1 = slinkedlist()
list1.atbegining(input("enter last item"))
list1.atbegining("Nov")
list1.atbegining("Oct")
list1.atbegining("Sep")

list1.removeNode(input("enter name to remove:"))
list1.listprint()
