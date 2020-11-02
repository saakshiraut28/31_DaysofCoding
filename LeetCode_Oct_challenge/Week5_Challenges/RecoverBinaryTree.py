'''
You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

 

Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
'''
class Node: 
      
    def __init__(self, data):
         
        self.key = data 
        self.left = None
        self.right = None
 


def correctBstUtil(root, first, middle,
                   last, prev):
                        
    if(root):
         
        correctBstUtil(root.left, first,
                       middle, last, prev)
                        
        if(prev[0] and root.key < prev[0].key):
            if(not first[0]):
                first[0] = prev[0]
                middle[0] = root
            else:
                last[0] = root
        prev[0] = root

        correctBstUtil(root.right, first, 
                       middle, last, prev)
     

def correctBst(root):

    first = [None]
    middle = [None]
    last = [None]
    prev = [None]

    correctBstUtil(root, first, middle,
                   last, prev)
 

    if(first[0] and last[0]):
         

        first[0].key, last[0].key = (last[0].key, 
                                    first[0].key)
 
    elif(first[0] and middle[0]):

        first[0].key, middle[0].key = (middle[0].key,
                                        first[0].key)

def PrintInorder(root):
     
    if(root):
        PrintInorder(root.left)
        print(root.key, end = " ")
        PrintInorder(root.right)
         
    else:
        return

root = Node(6) 
root.left = Node(10) 
root.right = Node(2) 
root.left.left = Node(1) 
root.left.right = Node(3) 
root.right.left = Node(7) 
root.right.right = Node(12) 
 

print("inorder traversal of noraml tree")
PrintInorder(root)
print("")

correctBst(root)

print("")
print("inorder for corrected BST")
 
PrintInorder(root)
 