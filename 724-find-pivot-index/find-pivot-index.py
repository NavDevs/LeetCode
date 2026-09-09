class Solution(object):
    def pivotIndex(self, nums):
        r =sum(nums)

        l  = 0

        for i in range(len(nums)):
            val = nums[i] 
            r -= val
            if l == r:
                return i
            else:
                l += val
        
        return -1
        