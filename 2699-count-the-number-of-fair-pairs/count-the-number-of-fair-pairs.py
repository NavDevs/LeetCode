class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()

        return self.Count(nums,upper) - self.Count(nums,lower-1)

    def Count(self,nums,tar):
        l = 0
        r  = len(nums)-1
        c= 0
        while l <r:
            if nums[l] + nums[r] <= tar:
                c += r -l
                l +=1
            else:
                r -= 1
        return c 
        