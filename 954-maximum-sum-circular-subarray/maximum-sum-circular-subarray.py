class Solution(object):
    def maxSubarraySumCircular(self, nums):

        maxP = minP = minS =maxS = nums[0]

        ans = 0
        total =  sum(nums)

        for i in nums[1:]:

            maxP = max(i, maxP+i)
            minP = min(i, minP + i)

            maxS = max(maxS,maxP)
            minS = min(minS,minP)
        
        if maxS < 0 :
            return maxS

        return max( maxS, total - minS )

       
        
        