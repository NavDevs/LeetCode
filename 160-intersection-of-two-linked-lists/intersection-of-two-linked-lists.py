# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        p1= headA
        p2  =headB
        has = set()
        
        while p1:
            has.add(p1)
            p1 = p1.next

        while p2:
            if p2 in has:
                return p2
            p2 = p2.next

        return None 

        
            




        
            
        