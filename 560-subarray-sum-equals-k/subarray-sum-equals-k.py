class Solution(object):
    def subarraySum(self, nums, k):
        count  = 0
        freq = {0:1}

        prefix = 0

        for i in range(len(nums)):

            prefix += nums[i]

            need  = prefix - k

            if need in freq:
                count += freq[need]

            freq[prefix] = freq.get(prefix, 0) + 1

        return count 