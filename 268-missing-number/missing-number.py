class Solution(object):
    def missingNumber(self, nums):
        s = {}
        for i in range(len(nums)):
            s[nums[i]] = i
        for i in range(len(nums)+1):
            if i not in s:
                return i 
        
       
        