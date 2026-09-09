class Solution(object):
    def waysToSplitArray(self, nums):
        c = 0
        total = sum(nums)
        left  =0 

        for i in range(len(nums)-1):
            left += nums[i]
            right = total - left 

            if left >= right:
                c +=1
        return c         
        