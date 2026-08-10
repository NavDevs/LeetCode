class Solution(object):
    def subarraysDivByK(self, nums, k):
        freq  = {0:1}
        p = 0
        c= 0

        for i in range(len(nums)):
            p  += nums[i]

            need  = p % k

            if  need in freq:
                c += freq[need]
            
            freq[need] = freq.get(need,0)+1
        return c  

        