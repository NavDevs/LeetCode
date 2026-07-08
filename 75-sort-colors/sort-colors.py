class Solution(object):
    def sortColors(self, nums):
        low = 0
        mid= 0
        r  = len(nums)-1
        while mid <=r:
            if nums[mid] ==0:
                nums[mid], nums[low] =nums[low], nums[mid]
                mid +=1
                low+=1
            elif nums[mid]==1:
                mid  +=1
            else:
                nums[mid], nums[r] =nums[r], nums[mid]
                r -=1
        return nums
            

                

        
            

               