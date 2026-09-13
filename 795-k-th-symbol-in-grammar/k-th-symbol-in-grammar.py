class Solution(object):
    def kthGrammar(self, n, k):
        cur  =0
        l, r = 1, 2**(n-1)

        for _ in range(n-1):
            m = (l+r)//2
            if k <=m:
                r = m


            else:
                l = m+1
                if cur == 0:
                    cur = 1
                else:
                    cur = 0

              

        return cur 
        