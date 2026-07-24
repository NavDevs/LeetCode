class Solution(object):
    def topKFrequent(self, nums, k):
        c = {}

        for i in nums:
            c[i] = c.get(i, 0) + 1

        # Sort the dictionary by frequency (highest first)
        ans = sorted(c, key=c.get, reverse=True)

        return ans[:k]