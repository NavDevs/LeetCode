class Solution(object):
    def twoSum(self, nums, target):
        s={}
        n =len(nums)
        for i  in range(0,n):
            d = target - nums[i]
            if d in s:
                return [s[d],i]
        
            s[nums[i]]=i
