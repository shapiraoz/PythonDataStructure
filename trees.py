import random
import sys
class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    
    def __str__(self):
        return " {} ".format(self.data)


class LinkNode(Node):
    def __init__(self, data,left=None,right=None,next=None):
        super().__init__(data,left,right)
        self.next=next

class HdNode(Node):
    def __init__(self, data, left=None, right=None):
        super().__init__(data, left=left, right=right)
        self.hd=sys.maxsize
    


class BinaryTree:
    def __init__(self):
        self.root=None

   

    
    def _height(self,node):
        if node is None:
            return 0

        lh =self._height(node.left)
        rh =self._height(node.right)
        if lh>rh :
            return lh+1
        else:
            return rh+1

    def height (self):
        return self._height(self.root) 

    def _sumNode(self,node):
        if node is None :
            return 0
        return self._sumNode(node.left)+node.data+self._sumNode(node.right)
        

    def _isSumTree(self, node):
        
        if node is None or node.left==None and node.right==None:
            return True
        
        sl =  self._sumNode(node.left)
        sr = self._sumNode(node.right)
        return  node.data == sl+sr and  self._isSumTree(node.left) and self._isSumTree(node.right)

  

    def _printLevelTree(self,node,level):
        if level==0 or node is None:
            return
        if level ==1 :
            print (node.data)
        elif level>1:
            self._printLevelTree(node.left,level-1)
            self._printLevelTree(node.right,level-1)

    def IsSumTree(self):
        return self._isSumTree(self.root)  


    def isBstUntil(self ,node, min,max):

        if node is None:
             return True
        if node.data <min or node.data>max :
            return False
        
        return self.isBstUntil(node.left,min,node.data-1) and self.isBstUntil(node.right,node.data+1,max)


    def IsBST(self):
        return self.isBstUntil(self.root,-sys.maxsize-1,sys.maxsize)

    def levelTreePrint(self):
        print("level order print")
        h=self.height()
        for i in range(h+1):
            self._printLevelTree(self.root,i) 


    def _printPreorderSubTree(self , node):
        if node is None:
            return
        print(node)
        self._printPreorderSubTree(node.left)
        self._printPreorderSubTree(node.right)

    def printPreorderTree(self):
        self._printPreorderSubTree(self.root)

class BinarySearchTree(BinaryTree):
      
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
        curr=node
        if curr==None or data==curr.data:
            return curr
        if data<node.data:
            return self._find(node.left,data)
        else :
            return self._find(node.right,data)
        
    def _findMin(self,node):
        current = node
        while(current.left):
            current=current.left
        return current

    def _findMax(self,node):
        while(node.right):
                node=node.right
        return node


    def _remove(self,node,data):
        
        if node is None:
            return node

        if  data<node.data:
            node.left = self._remove(node.left,data)
        elif node.data<data:            
            node.right = self._remove(node.right,data)
        else : #need to take it out
            if node.left is None:
                temp=node.right
                node=None
                return temp
            elif node.right is None:
                temp=node.left
                node=None
                return temp
            temp =self._findMin(node.right)
            node.data=temp.data
            node.right=self._remove(node.right,temp.data)
        return node  
   
        

   




########################## public section #############################################
    
   

    
    def buildHdData(self,data,hd,level):
        
        root =self.root
        if root is None :
            return
    
        if hd in data:
            if level>data[hd][1]:
                data[hd]=[root.data,level]
            else:
                data[hd]=[root.data,level]
              
        
        buildHdData(root.left,data,hd-1,level+1)
        buildHdData(root.left,data,hd+1,level+1)
        
    
    
    

    def printBottomView(self):
        root = self.root
        if root is None:
            return 
        d={}
        buildHdData(root,d,0,0)
        #return [ v[0]  for k,v in d.iteritems()]
        for k,v in d.items():
            print (v[0])
        

    def findMin(self):
        return self._findMin(self.root).data

    def findMax(self):
        return self._findMax(self.root)

    def find(self,data):
        return self._find(self.root,data)!=None
        
    def add(self,data):
        self.root=self._add2Tree(self.root,data)


    def remove(self,data):
        self._remove(self.root,data)



def basicTests(bt):
    
    items =[8,3,10,1,6,14,4,7,13]
    for i in items:
        bt.add(i)
    bt.printPreorderTree()
    
    bt.levelTreePrint()
    for i in items:
        print("find {}={}".format(i,bt.find(i)))
    print("find 55={}".format(bt.find(55)))
    item2 = [50,30,20,40,70,60,80]
    bt2  = BinarySearchTree()
    for j in item2:
        bt2.add(j)
    bt2.printPreorderTree()
    bt2.remove(50)
    print("after delete")
    bt2.printPreorderTree()

def stressTest(bt,limit,nums):
    items = [random.randrange(1, limit, 1) for i in range(nums)]  
    for i in items:
        bt.add(i)
    for i in items:
        if not bt.find(i): # test add & find
            print ("failed the item{} should be exist!!!")
            return False
    return True


if __name__=="__main__":
    bt=BinarySearchTree()
    basicTests(bt)
    bt_s= BinaryTree()
    bt_s.root = Node(26)
    bt_s.root.left= Node(10)
    bt_s.root.right = Node(3)
    bt_s.root.left.left = Node(4)
    bt_s.root.left.right = Node(6)
    bt_s.root.right.right = Node(3)
    print("bt_s tree :")
    bt_s.printPreorderTree()
    print ("bt_s IsSumTree={}!!".format(bt_s.IsSumTree()))
    print ("bt_s IsBST={}!!".format(bt_s.IsBST()))
    print ("bt IsBST={}!!".format(bt.IsBST()))

    #if stressTest(bt,100000000,500000):
    #    print ("stress pass!")
