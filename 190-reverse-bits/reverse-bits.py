class Solution(object):
    def reverseBits(self, n):
        res = 0

        for i in range(32):
            res = res * 2 + (n%2)
            n  = n// 2 

        return res 