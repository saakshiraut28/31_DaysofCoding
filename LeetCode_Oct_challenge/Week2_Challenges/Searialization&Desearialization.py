'''
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Example 1:

Input: root = [2,1,3]
Output: [2,1,3]
'''

import collections 


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        queue: Deque[TreeNode] = collections.deque()

        queue.append(root)

        data = ""
        while queue:
            popped = queue.popleft()
            if popped:
                data += str(popped.val) + ","
                queue.append(popped.left)
                queue.append(popped.right)
            else:
                data += "n,"

        return data

    def deserialize(self, data: str) -> TreeNode:
        vals = data.split(",")

        if vals[0] == "n":
            return None

        root = TreeNode(int(vals[0]))
        vals.pop(0)

        queue: Deque[TreeNode] = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()

            if not vals[0] == "n":
                node.left = TreeNode(int(vals[0]))
                queue.append(node.left)

            vals.pop(0)

            if not vals[0] == "n":
                node.right = TreeNode(int(vals[0]))
                queue.append(node.right)

            vals.pop(0)

        return root
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = [1,3,2]
tree = ser.serialize(root)
ans = deser.deserialize(tree)
print(ans)