class Solution(object):
    def maxAscendingSum(self, nums):
        maxs= cur  = nums[0]

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                cur +=nums[i]
            else:
                cur  = nums[i]
            maxs  = max(maxs,cur)
        return maxs     

