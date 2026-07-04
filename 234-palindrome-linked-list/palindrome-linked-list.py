# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        s = f  =head
        while f and f.next:
            s  = s.next
            f  = f.next.next
        prev  = None
        while s:
            n  = s.next
            s.next = prev
            prev = s
            s  = n

        l = head
        r = prev

        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True         