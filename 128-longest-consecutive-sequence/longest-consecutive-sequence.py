class Solution(object):
    def longestConsecutive(self, nums):
        s = set(nums)
        l = 0
        for i in s:
            if i-1 not in s:
                le = 1
                while i+le in s:
                    le +=1
                l = max(l,le)
        return l 




