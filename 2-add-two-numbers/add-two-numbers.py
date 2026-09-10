# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        tail = dummy
        carry = 0
        
        while l1 or l2 or carry:
            s= carry

            if l1:
                s+=l1.val
                l1= l1.next
            
            if l2:
                s+=l2.val
                l2= l2.next

            carry = s // 10
            digit = s % 10

            tail.next = ListNode(digit)
            tail = tail.next
        
        return dummy.next 
