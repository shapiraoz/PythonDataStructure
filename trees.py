class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def __str__(self):
        return " {} ".format(self.data)


class BinaryTree:
    def __init__(self):
        self.root=None

    def _printSubTree(self , node):
        if node is None:
            return
        print(node)
        self._printSubTree(node.left)
        self._printSubTree(node.right)

    def printTree(self):
        self._printSubTree(self.root)
            
        

    def _add2Tree(self,node,data):
        if node is None:
            return Node(data)
            
        if node.data == data:
            return node
        if node.data<data:
            node.right=self._add2Tree(node.right,data) 
        else :
            node.left=self._add2Tree(node.left,data)
        return node

    def _find(self,node,data):
        if node is None:
            return None
        if node.data==data:
            return node
        return self._find(node.left,data) or self._find(node.right,data)

    def find(self,data):
        return self._find(self.root,data)!=None
        
    def add(self,data):
        self.root=self._add2Tree(self.root,data)

    #def remove(self,data):

if __name__=="__main__":
    bt=BinaryTree()
    items =[8,3,10,1,6,14,4,7,13]
    for i in items:
        bt.add(i)
    bt.printTree()
    for i in items:
        print("find {}={}".format(i,bt.find(i)))
    print("find 55={}".format(bt.find(55)))