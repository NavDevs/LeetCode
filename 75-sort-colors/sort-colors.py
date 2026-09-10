class Solution(object):
    def sortColors(self, nums):
        l = 0 
        m = 0 
        r = len(nums)-1

        while m <= r:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                m+=1
                l+=1
            elif nums[m] ==1:
                m+=1
            else:
                nums[r], nums[m] = nums[m],nums[r]
                r-=1
        return nums

        
             


            

                

        
            

               