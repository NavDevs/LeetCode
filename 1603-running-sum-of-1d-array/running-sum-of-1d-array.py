class Solution(object):
    def runningSum(self, nums):
        p = [0]

        for i in nums:
            p.append(i + p[-1])

        return p[1:] 
        