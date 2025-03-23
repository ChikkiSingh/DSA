import dataclasses
from tables import Node


class object:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
    def __init__(self,start,item):
        self.start=start
        
    def is_empty(self):
        return self.start
    def INSERT_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def INSERT_at_last(self.data):
        n=Node(data)
        if not self.is_empty():
        
        
            