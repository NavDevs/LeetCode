class Solution(object):
    def findDisappearedNumbers(self, nums):
        res  =[]
        for i in range(len(nums)):
            ind = abs(nums[i]) - 1
            if nums[ind] < 0:
                continue
            else:
                nums[ind] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        
        return res



        