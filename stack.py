#define a class stack to implement stack data structure using list def __init__()method to create empty list object
class stack:
    def __init__(self):
        self.item=[]
# define a method is_empty() to check if the stack is empty in stack class
    def is_empty(self):
        return len(self.item)==0
    # in stack class define push()method to add the data onto the stack
    def push(self,data):
        self.item.append(data)
    #in stack class define pop( method) to remove top element from the stack
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("stack is empty")
    # in stack class define peek() method to return top element from the stack
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("stack is empty") 
    # in stack class  define size() method to return the size of the stack
    def size(self):
        return len(self.item)     
    
s1=stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("first element",s1.peek())
print("remove first element",s1.pop())
print("first element",s1.peek())
        