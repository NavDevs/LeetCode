# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy  = ListNode(0,head)
        LeftPrev  = dummy
        cur = head

        for i in range(left-1):
            LeftPrev  = cur
            cur = cur.next
        prev  =None
        for i in range(right-left+1):
            NextNode = cur.next 
            cur.next  = prev
            prev  = cur 
            cur = NextNode
        LeftPrev.next.next = cur
        LeftPrev.next = prev
        return dummy.next
        
        