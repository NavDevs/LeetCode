class Solution(object):
    def checkSubarraySum(self, nums, k):
        f  = { 0:-1}
        p = 0 

        for i in range(len(nums)):
            p += nums[i]

            need = p % k

            if need in f : 
                if i - f[need] >= 2:
                    return True
            else:
                f[need] = i 
        return False
                




        
        