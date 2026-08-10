class Solution(object):
    def minStartValue(self, nums):
        s = 0
        m = 1

        for i in range(len(nums)):
            s += nums[i]
            m = min(m,s)
        if m > 0 :
            return m 
        else:
            return (m*-1) + 1 
                 
        