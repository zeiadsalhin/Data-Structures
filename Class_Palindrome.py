class stack:
    def __init__(self,limit=10):
        self.stk=[]
        self.limit=limit
    def push(self,item):
        if len (self.stk)>=self.limit:
            print("stack overflow")
        else:
            self.stk.append(item)
        print("stack after push", self.stk)

    def pop(self):
        if len (self.stk)<=0:
            print("stack underflow")
        else:
            print("stack after pop", self.stk)
        return self.stk.pop()

def palind(input,length):
    p=False
    s=stack(length)
    for c in input:
       s.push(c)
    for c in input:
        if c==s.pop():
          p=True
        else:
          p=False
    return p

x=input("enter your string for palindrome test\n")
if (palind(x,len(x))):
    print("string is palindrome")
else:
    print("string is not palindrome")