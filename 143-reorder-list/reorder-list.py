class Solution(object):
    def reorderList(self, head):
        if not head:
            return 
        a  = []
        c = head

        while c:
            a.append(c)
            c  =c.next 
        
        i = 0
        j = len(a)-1

        while i < j:
            a[i].next = a[j]
            i +=1

            if i ==j:
                break

            a[j].next = a[i]
            j-=1
        a[i].next = None

        