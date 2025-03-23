#tree data structure  define the class ;
class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
# define the bst class  and root node
class BST:
    def __init__(self):
        self.root=None
# insert the data in bst tree;
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.item:
             root.left=self.rinsert(root.left,data)
        elif data >root.item:
              root.right=self.rinsert(root.right,data)
        return root    
# search method 
    def search(self,data):
        return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        if root is None or root.item==data:
            return root 
        if data< root.item:
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)
    
    
# in_order method 
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,data):
        if root:
            self.rinorder(root.left,data)
            result.append(root.item)
            self.rinorder(root.right,data)

# pre_order method 
    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,data):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,data)
            self.rpreorder(root.right,data)
# post_order 
    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,data):
        if root:
            self.rpostorder(root.left,data)
            self.rpostorder(root.right,data)
            result.append(root.item)
            
    # FINED minimum  values  in item node.
    
    def min_values(self,temp):
        current=temp
        while current.left is not None:
            current=current.left
        return current.item
    # fined max values 
    def max_values(self,temp):
        current=temp
        while current.right is not None:
            current=current.right
        return current.item
        
    
    
    
    