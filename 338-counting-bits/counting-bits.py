class Solution(object):
    def countBits(self, n):
        ans  = []

        for i in range(n+1):
            c = 0
            while i:
                i = i & (i-1)
                c +=1
            ans.append(c)

        return ans 
        