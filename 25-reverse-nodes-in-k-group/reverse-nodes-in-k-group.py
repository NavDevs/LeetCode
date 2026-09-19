# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        cur =  head

        temp =cur

        for _ in range(k):
            if temp is None:
                return head
            temp = temp.next

        prev = None
        cur = head

        for _ in range(k):
            nxt = cur.next
            cur.next =prev
            prev = cur
            cur = nxt

        head.next = self.reverseKGroup(cur,k) 

        return prev
        