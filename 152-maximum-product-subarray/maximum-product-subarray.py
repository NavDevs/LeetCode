class Solution(object):
    def maxProduct(self, nums):
        curMax = curMin = ans = nums[0]

        for i in nums[1:]:
            if i < 0:
                curMax, curMin = curMin, curMax

            curMax = max(i, curMax * i)
            curMin = min(i, curMin * i)

            ans = max(ans, curMax)

        return ans