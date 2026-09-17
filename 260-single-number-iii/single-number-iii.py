class Solution(object):
    def singleNumber(self, nums):
        ans= []
        m = Counter(nums)

        for i in m:
            if m[i] == 1:
                ans.append(i)

        return ans 
        