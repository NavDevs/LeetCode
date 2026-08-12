class Solution(object):
    def maxAbsoluteSum(self, nums):
        maxP  = nums[0]
        minP =  nums[0]
        ans  = abs(nums[0]) 

        for i in nums[1:]:

            maxP = max(i , maxP +i)
            minP = min(i , minP +i)

            ans  =  max( ans , abs(maxP),abs(minP))

        return ans 
            
        
        