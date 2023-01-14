class node :
    def init(self,data):
        self.data=data
        self.left=None
        self.right=None
def size (node):
    if node is None:
        return 0
    else:
        return(size(node.left)+1+size(node.right))
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
print ("size of the tree is %d" %(size(root)))