class Solution(object):
    def subsets(self, nums):
        res   = [[]]

        for i in nums:
            new = []
            for j in res:
                new.append(j+[i])
            res.extend(new)
        return res
                
        
        