class Solution(object):
    def subsets(self, nums):
        res   = [[]]

        for i in nums:
            for j in res[:]:

                res.append(j + [i])

        return res
                
        
        