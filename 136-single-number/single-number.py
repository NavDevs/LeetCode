class Solution(object):
    def singleNumber(self, nums):
        s =Counter(nums)
        for i  in s:
            if s[i] == 1:
                return i
            
            
        