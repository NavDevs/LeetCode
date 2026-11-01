class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)

        t = n * (n+1) // 2 

        return t  - sum(nums)

        

        

      
        