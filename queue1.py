class Queue(object) :
    def __init__(self):
          self.S1=[]
          self.S2=[]
   def enqueue(self.element):
          self.S1.append(element)
   def dequeue(self):
       if not self.S2:
           while self.S1:
                self.S2.append(self.S1.pop())
      Return self.S2.pop()
q = Queue
for I in xrange(5):
     q.enqueue(i)
for i in xrange(5):
      print q.dequeue()