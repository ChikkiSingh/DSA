# define a class Node to describe a node of singly linked List;
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
        
# define a class SLL  to implement singly linked list __init__() method to create and initials start reference variable;
class SLL:
    def __init__(self,start=None):
        self.start=start

# define a method is_empty() to check if the inked list is empty in sll class.
    def is_empty(self):
        return self.start==None

# class in sll ,define a method insert_at_start() to insert on element at the starting of the list.

    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
        
# class in sll,define a method insert_at_last() to insert on element at the end of the list.
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
                temp.next=n
            else:
                self.start=n
                
                
# class sll , define a method search() to  fine the node with specified  element  val;
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp= temp.next
        return None
    
#  class sll define a method insert_after() to insert a new node after  given node of the list;
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
 # class sll define  a method to print all the element of the list   
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end='') 
            temp=temp.next
  
# delete first node in sll class ;
    def delete_first(self):
        if self.start is not None:
            self.start= self.start.next
            
# delete last node in sll class
    def delete_last(self):
        if self.start is not None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next 
            temp.next=None
            
# delete node in after specified node in sll class;
    def delete_after(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp .item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next 
                        break
                    temp=temp.next
                
# class implement iterator  for sll to access all of the list in a sequence;
    # def __iter__(self):
    #     return SLLIterator(self.start)
        
class SLLIterator:
    
    def __init__(self,start) :
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopAsyncIteration
        data=self.current.item 
        self.current=self.current.next 
        return data
myClass=SLL()
myClass.insert_at_start(10)
myClass.insert_at_start(20)
myClass.insert_at_last(100)
myClass.print_list()
print()
#myClass.search(10)
            
#myClass.delete_after(100)
#print()
 
# for x in myClass:
#     print(x,end='')
# print()
 
 
    