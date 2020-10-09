"""Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
"""

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
    def __init__(self): 
        self.head = None

    def push(self, new_data):  
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    def printList(self): 
        temp = self.head 
        while(temp): 
            print( temp.data), 
            temp = temp.next
  
    def rotate(self, k): 
        if k == 0:  
            return 
        current = self.head 
        count = 1 
        while(count <k and current is not None): 
            current = current.next
            count += 1
        if current is None: 
            return
        kthNode = current  
        while(current.next is not None): 
            current = current.next
        current.next = self.head 
        self.head = kthNode.next
        kthNode.next = None
  
  
  
 
llist = LinkedList() 
  

for i in range(60, 0, -10): 
    llist.push(i) 
  
print("Given linked list")
llist.printList() 
llist.rotate(4) 
  
print( "\nRotated Linked list")
llist.printList() 