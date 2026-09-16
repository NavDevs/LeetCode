class Solution(object):
    def canJump(self, nums):
        n = len(nums)
        target = n-1 
        for i in range(n-1,-1,-1):
            max_jump = nums[i]
            if i + nums[i] >= target:
                target  = i

        return target  ==  0



        
        