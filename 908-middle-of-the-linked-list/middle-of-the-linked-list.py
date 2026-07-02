# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        cur  = head 
        count  =0
        while cur:
            count+=1
            cur = cur.next
        m =  count//2
        cur =  head

        for i in range(m):
            cur = cur.next
        
        return cur
        