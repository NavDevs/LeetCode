class Solution(object):
    def subarraySum(self, nums, k):
        c = 0
        freq  = {0:1}
        p = 0
        for i in nums:

            p += i 

            n = p - k 
            
            if n in freq:
                c += freq[n]

            freq[p] = freq.get(p,0) + 1
        
        return c 



             