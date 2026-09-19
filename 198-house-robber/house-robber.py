class Solution(object):
    def rob(self, nums):
        a = 0
        b = 0

        for i in nums:
            a , b = b, max(b , a + i)

        return b 
        