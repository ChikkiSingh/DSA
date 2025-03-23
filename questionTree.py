
class Node:
    def __init__(self,item=0,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right

class BST:
    def rdelete(self,root,data):
        if root is None:
            return root
        if data > root.item:
            root.right=self.rdelete(root.right,data)
        elif data <root.item:
            root.left=self.rdelete(root.left,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
# sub tree 
            cur=root.right
            while cur.left:
                cur=cur.left
            root.val=cur.item
            root.right=self.rdelete(root.right,root.item)
        return root