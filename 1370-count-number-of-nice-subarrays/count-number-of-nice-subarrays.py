class Solution(object):
    def numberOfSubarrays(self, nums, k):
        f  = {0:1}
        c = 0
        prefix  = 0
        for i in range(len(nums)):

            if  nums[i] % 2 ==1:
                prefix += 1

            need  = prefix - k
            
            if need in f:
                c += f[need]

            f[prefix] = f.get(prefix,0) +1
        return c 