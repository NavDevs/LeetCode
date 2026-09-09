class Solution(object):
    def maxSubarrayLength(self, nums, k):
        l = 0
        maxlen = 0
        c = {}

        for r in range(len(nums)):
            c[nums[r]] = c.get(nums[r], 0) + 1

            while c[nums[r]] > k:
                c[nums[l]] -= 1
                l +=1

            maxlen = max(maxlen, r - l + 1)

        return maxlen 
        