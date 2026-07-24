class Solution(object):
    def singleNumber(self, nums):
        s ={}
        for i in nums:
            s[i]  = s.get(i,0)+1
        for i  in s:
            if s[i] == 1:
                return i
            
            
        