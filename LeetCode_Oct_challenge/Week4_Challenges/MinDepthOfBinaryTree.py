'''

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.


Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2

'''


# Definition for a binary tree node.
class Node: 
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def minDepth(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        return minDepth(root.right)+1
    if root.right is None:
        return minDepth(root.left)+1 
    return min(minDepth(root.left), minDepth(root.right))+1


# Driver Program 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(minDepth(root))