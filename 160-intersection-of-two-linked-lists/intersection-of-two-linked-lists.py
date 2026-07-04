# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        Hash = set()
        p1 =  headA
        p2 =headB

        while p1:
            Hash.add(p1)
            p1 = p1.next 
        
        while p2:
            if p2  in Hash:
                return p2
            else:
                p2 = p2.next 
        return None
            
        