##################################################################   

#### o(n) - bad implemention 
class LRUCache(object):

    def __init__(self, capacity):
        self._data={}
        self._capacity = capacity
        self.q=[]       
              

    def get(self, key):
      
        if key not in self._data :
          return -1
        self._move2End(key)
        return self._data[key]
                               
                
    def _add2Data(self,key,value):
        self._data[key]=value
        self.q.append(key)
        #self._data[key] =[value,self.q[-1]]
        

    def _move2End(self,key):
        self.q.append(self.q.pop(self.q.index(key)))  

    def put(self, key, value):

        self._add2Data(key,value)
        self._move2End(key)
        if len(self._data) <= self._capacity:
            return

        # general 
        going_to_pop= self.q[0]        
        del self._data[going_to_pop]
        del self.q[0] 
     
######################################################################################################### 
'''
 linked list as q o(1) implemention 
'''

class Node:
    def __init__(self,key,data,next=None,prev =None):
        self.val =data
        self.key=key
        self.next=next
        self.prev=prev

class LRUCacheLinkedList(object):
    def __init__(self,capacity):
        self._capacity = capacity
        self.head=None
        self.tail=None
        self.data={}


    def _move2End(self,node):
        prev=node.prev
        next=node.next

        if prev is not None:
            prev.next=next
        if node==self.head:
            self.head=node.next
        
        node.prev=self.tail
        self.tail.next=node
        self.tail=self.tail.next


    def get(self, key):
        if key not in self.data:
            return -1
        node =self.data[key]
        ret =node.val
        self._move2End(node)
        return ret

    def put(self, key, value):

        node = self.data[key] if key in self.data else Node(key,value)
        self.data[key] = node
        if self.head == None:
            self.head = node
            self.tail =node
            return
        

        self._move2End(node)
        if len(self.data) <=self._capacity :
            return
        
        temp= self.head
        del self.data[temp.key]
        self.head=temp.next
        del temp
############################################################################################################
'''
    best and simple for python (3 and above) using OredredDic and very common for this task
    https://docs.python.org/3/library/collections.html
'''
from collections import OrderedDict

class LruOrderedDic:
    def __init__(self ,capacity):
        self.capacity=capacity
        self.data= OrderedDict()

    
    def get(self, key):
        if key not in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]


    def put(self, key, value):
        self.data[key]=value
        self.data.move_to_end(key)

        if len(self.data) <= self.capacity:
            return
        
        self.data.popitem(last=False)


#########################  tests  ############################################  
def stressTest():
    cache = LRUCache(10) 
    for i in range (100):
        cache.put(i,i)
        if i>3:
            cache.get(i)
        print (cache._data)

    

def simpleTest(lru):
    
   lru.put(1,1)
   lru.put(2,2)
   assert(lru.get(1)==1)
   lru.put(3,3)
   assert(lru.get(2)==-1)
   lru.put(4,4)
   assert(lru.get(1)==-1)
   assert(lru.get(3)==3)
   assert(lru.get(4)==4)



if __name__ == "__main__":

    import sys
    
    simpleTest(LRUCache(2))
    simpleTest(LRUCacheLinkedList(2))
    
    if sys.version_info.major !=3 :
        print("skipping this test only for python3 ")
    else :
        print("3rd test using OrderedDic")
        simpleTest(LruOrderedDic(2))
   
###########################################################
 
 
    




