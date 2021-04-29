

import random
from heapq import heappop, heappush

def createRandomArr(limit,size):
    return  [random.randrange(1, limit, 1) for i in range(size)] 

def Swap(arr,i,j):
    t = arr[i]
    arr[i]=arr[j]
    arr[j]=t
    return arr

def BubbleSort(arr):
    ret=arr
    l = len(arr)
    swap = False
    while True:
        swap = False
        for i in range(1,l):
            if ret[i-1]>ret[i]:
                ret = Swap(ret,i-1,i)
                swap=True
        if not swap :
            break
    return ret

def HeapSort(arr):
    ret =[]
    for item in arr:
        heappush(ret,item)
    return [heappop(ret) for i in range(len(ret))]


def InsterionSort(arr):
    for i in range(len(arr)):
        v = arr[i]
        j=i
        while j>=1 and arr[j-1]>v:
            arr[j]=arr[j-1]
            j-=1
            
        arr[j]=v
    return arr


def mergeArr(larr,rarr):
    merge=[]
    l=r=m=0
    while(l<len(larr) or r<len(rarr)):
        if r>len(rarr):
            merge.append(larr[l])
            l+=1
        elif l>len(larr):
            merge.append(rarr[r])
            r+=1
        elif larr[l]>rarr[r]:
            merge.append(rarr[r])
            r+=1
        else:
            merge.append(larr[l])
            l+=1
    return merge

def MergeSort(arr):
    if len(arr)<=1:
        return arr
    mid =int(len(arr)/2)
    larr=MergeSort(arr[0:mid])
    rarr=MergeSort(arr[mid:])
    return mergeArr(larr,rarr)

def Partition(arr ,lo,hi):
    pivot = arr[hi]
    i =lo
    for j in range(lo,hi):
        if arr[j] <pivot :
            Swap(arr,i,j)
            i+=1
    Swap(arr,i,hi)
    return i 


def RunTestSort(name,func):
    t =createRandomArr(1000,10)
    print ("arr before {} sort ={}".format(name,t))
    print ("{}Sort after {}".format(name,func(t)))


if __name__=="__main__":
    
    RunTestSort("Bubble",BubbleSort)
    RunTestSort("heap",HeapSort)
    RunTestSort("Insert",InsterionSort)
    RunTestSort("merge",MergeSort)