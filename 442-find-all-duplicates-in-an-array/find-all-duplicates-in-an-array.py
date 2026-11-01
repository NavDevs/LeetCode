class Solution(object):
    def findDuplicates(self, nums):
        seen = set()
        ans = []
        for i in nums:
            if i in seen:
                ans.append(i)
            else:
                seen.add(i)
        return ans
        
        