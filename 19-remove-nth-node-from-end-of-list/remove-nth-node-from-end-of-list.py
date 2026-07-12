# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        cur = head
        total = 0
        while cur:
            total += 1
            cur = cur.next
        cur  =dummy 
        move  = total - n
        for  _ in range(move):
            cur  =cur.next
        cur.next = cur.next.next 
        return dummy.next 
