#define the class to implement heap sort data structure withe __init__method to create empty heap...
class Heap:
    def __init__(self):
        self.heap=[]
        
# in class, define a method to create heap  from a given list of element .
def create_heap(self,list):
    for e in list:
        self.insert(e)
        
# define the method insert a given element in the heap at appropriate position.
def insert(self,e):
    index=len(self.heap)
    parent_index=(index-1)//2
    while index > 0 and self.heap[parent_index]<e:
        if index==len(self.heap):
            self.heap.append(self.heap[parent_index])
        else:
            index=parent_index
            parent_index=(index-1)//2
        if index==len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index]=e 
            
            
# define a top method which return the top element of the heap. raise an exception if heap empty.
def top(self):
    if len(self.heap)==0:
        raise Empty_heap_Exception()
    return self.heap[0]
###### define a method  delete which delete the top element and return arise the top  element and return it exception heap is empty.
def delete(self):
    if len(self.heap)==0:
        raise Empty_heap_Exception()
    if len(self.heap)==1:
        return self.heap.pop()
    max_value=self.heap[0]
    temp=self.heap.pop()
    index=0
    left_child_index=2*index*1
    right_child_index=2*index+2
    while left_child_index<len(self.heap):
        if right_child_index<len(self.heap):
            if self.help[left_child_index]>self.help[right_child_index]:
                if self.heap[index]==self.help[right_child_index]>temp:
                    self.heap[index]=self.heap[left_child_index]
                    index=left_child_index
                else:
                    break
            else:
                if self.heap[right_child_index]>temp:
                    self.heap[index]=self.heap[right_child_index]
                    index=right_child_index
                else:
                    break
        else:
            if self.heap[right_child_index]>temp:
                self.heap[index]=self.heap[right_child_index]
            else:
                break
            left_child_index=2*index+1
            right_child_index=2*index+2
            self.heap[index]=temp
            return max_value
    #### define a method heap sort to given list with the heap of heap.
def heap_sort(self,list):
    self.create_heap(list1)
    list2=[]
    try:
        while True:
            
            list2.insert(0,self.delete(1))
    except Empty_heap_Exception:
        pass
    return list2






###########
def Empty_heap_Exception(Exception):
    def __init__(self,msg="empty heap"):
        self.msg=msg
    def __str__(self):
        return self.msg
    
               

list1=[12,43,67,89,34,11,34,99,54]
h=help()
list=h.heap_sort(list1)
print(list1)