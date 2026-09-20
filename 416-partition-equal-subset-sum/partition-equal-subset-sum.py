class Solution(object):
    def canPartition(self, nums):
        total  = sum(nums)

        target =  total // 2

        if total % 2 != 0:
            return False

        dp = [False] * (target+1)
        dp[0] =  True
        for num in nums:
            for i in range(target,num-1,-1):

                dp[i] = dp[i] or dp[i-num]

        return dp[target]
         
        