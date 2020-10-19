'''
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
   # returns the sorted list
    def sortList(self, head: ListNode) -> ListNode:
        # if head is not present returns none or the head
        if head is None or head.next is None:
            return head
        # to get mid element
        mid = self.middleEle(head) #Calls to middleEle fuction
        midlink = mid.next
        
        mid.next = None
                
        left=self.sortList(head)
        right=self.sortList(midlink)

        sort_list = self.sortedList(left,right)

        return sort_list 


    def sortedList(self,l,r): #sorts the left side and rightside of mid
        res = None
        
        if l==None: return r
        if r==None: return l
        
        if l.val<=r.val:
            res=l
            res.next=self.sortedList(l.next, r)
        else:
            res=r
            res.next=self.sortedList(l, r.next)
        return res
        
    def middleEle(self, head): # return mid
        if head is None:
            return head
        # data is value of first int and d_next is value of next integer
        data = head
        d_next = head
        
        while(d_next.next!=None and d_next.next.next!=None):
            data = data.next
            d_next = d_next.next.next
        
        return data


input = [4]
obj = Solution()
result = obj.sortList(input)
print(result)