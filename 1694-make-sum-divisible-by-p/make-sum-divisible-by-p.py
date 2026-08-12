class Solution(object):
    def minSubarray(self, nums, p):
        f = {0:-1}
        total =  sum(nums)

        rem  = total % p
        ans  = len(nums)

        if rem  == 0:
            return 0
        
        pre = 0

        for i in range(len(nums)):

            pre = (pre+ nums[i]) % p

            n  = (pre -  rem) % p 

            if n in f:
                ans  = min(ans, i - f[n])
            
            f[pre] = i

        if ans == len(nums):
            return -1
            
        return ans 

        
        