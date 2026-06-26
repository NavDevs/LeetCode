class Solution(object):
    def maxSubArray(self, nums):
        c = 0
        best = nums[0]
        for i in range(len(nums)):
            c+=nums[i]
            best = max(c,best)
            if c < 0:
                c = 0
        return best
       
        
       
        