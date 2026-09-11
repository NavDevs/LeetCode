# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head:
            return 
        a = []
        cur = head

        while cur:
            a.append(cur.val)
            cur = cur.next

        ans  = self.sort(a) 
        h = ListNode(ans[0])
        cur  =h
        for i in range(1,len(ans)):
            cur.next  = ListNode(ans[i])
            cur  = cur.next 

        return h
    def sort(self,a):
        if len(a) <= 1:
            return a
        mid  =len(a)//2
        l = self.sort(a[:mid])
        r = self.sort(a[mid:])

        return self.merge(l,r)

    def merge(self,l,r):
        res =[]
        i = 0
        j = 0
        while i < len(l) and j  < len(r):
            if l[i] < r[j]:
                res.append(l[i])
                i +=1
            else:
                res.append(r[j])
                j+=1
            
        res.extend(l[i:])
        res.extend(r[j:])

        return res
        