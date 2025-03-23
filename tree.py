# define a class Node with instance variable left,item and right, the variable left and right are use to refer left child the item variable is used to hold data item.....
class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right
# define a class BST to implement binary search tree data structure. make __init__() method to create to root instance variable to hold the ref of root node
class BST:
    def __init__(self):
        self.root=None
## in class BST define insert method to store new data item in the binary search tree.
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data <root.item:
            root.left=self.rinsert(root.left,data)
        elif data> root.item:
            root.right=self.rinsert(root.right,data)
            return root
## in class BST,define a search method to find to a given item in the binary search tree and returns in the node ref in return none if search failed
    def search(self,data):
        return self.rsearch(self.root.data)
    def rsearch(self,root,data):
        if root is None or root.item==data:
            return root  
        if data <root.item:
            self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)
        
#  in class define a method to implement in_order traversal 
    def inorder(self):
        result=[]
        self.rinorder(self,root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
# in class define a method to implement pre_order traversal 
    def preorder(self):
        result=[]
        self.rinorder(self,root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
            
######### in class define a method to implement post_order traversal   
    def postorder(self):
        result=[]
        self.rinorder(self,root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)
            result.append(root.item)
            
            