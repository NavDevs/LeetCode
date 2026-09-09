class Solution(object):
    def minSubarray(self, nums, p):
        freq  = {0:-1}
        total = sum(nums)
        rem  = total % p
        if rem  == 0:
            return 0
        ans  =len(nums)
        prefix =0
        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % p
            need = (prefix - rem) % p

            if need in freq:
                ans  = min(ans, i- freq[need])
            
            freq[prefix] = i
        
        if ans  == len(nums):
            return  -1
        
        return ans 
        