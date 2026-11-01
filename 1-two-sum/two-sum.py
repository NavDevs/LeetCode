class Solution(object):
    def twoSum(self, nums, target):
        s  = {}

        for i in range(len(nums)):
            diff  = target - nums[i]

            if diff in s:
                return [i,s[diff]]

            s[nums[i]] = i
        
