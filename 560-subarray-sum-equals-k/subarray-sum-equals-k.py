class Solution(object):
    def subarraySum(self, nums, k):
        c = 0
        f = { 0 : 1}
        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]

            need = prefix - k
            if need in f :
                c += f[need]

            f[prefix] = f.get(prefix, 0) + 1
        return c  