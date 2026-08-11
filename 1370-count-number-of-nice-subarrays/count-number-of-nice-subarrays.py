class Solution(object):
    def numberOfSubarrays(self, nums, k):
        freq = {0: 1}
        prefix = 0
        count = 0

        for i in range(len(nums)):

            if nums[i] % 2 == 1:
                prefix += 1

            need = prefix - k

            if need in freq:
                count += freq[need]

            freq[prefix] = freq.get(prefix, 0) + 1

        return count