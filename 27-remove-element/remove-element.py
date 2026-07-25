class Solution(object):
    def removeElement(self, nums, val):
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] , nums[r] = nums[r] , nums[l]
                l+=1

        return l 

                       
        
