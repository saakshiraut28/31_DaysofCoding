""" Insert Into Binary Search Tree

 You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

 Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 Example
Input: root = [4,2,7,1,3], val = 5
 Output: [4,2,7,1,3,5] """

class newNode(): 
 
    def __init__(self, data): 
        self.key = data
        self.left = None
        self.right = None
         

def inorder(temp):
 
    if (not temp):
        return
 
    inorder(temp.left) 
    print(temp.key,end = " ")
    inorder(temp.right) 
 
 

def insert(temp,key):
 
    if not temp:
        root = newNode(key)
        return
    q = [] 
    q.append(temp) 


    while (len(q)): 
        temp = q[0] 
        q.pop(0) 
 
        if (not temp.left):
            temp.left = newNode(key) 
            break
        else:
            q.append(temp.left) 
 
        if (not temp.right):
            temp.right = newNode(key) 
            break
        else:
            q.append(temp.right) 
     

if __name__ == '__main__':
    root = newNode(10) 
    root.left = newNode(11) 
    root.left.left = newNode(7) 
    root.right = newNode(9) 
    root.right.left = newNode(15) 
    root.right.right = newNode(8) 
 
    print("Inorder traversal before insertion:", end = " ")
    inorder(root) 
 
    key = 12
    insert(root, key) 
 
    print() 
    print("Inorder traversal after insertion:", end = " ")
    inorder(root)