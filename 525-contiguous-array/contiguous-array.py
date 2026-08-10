class Solution(object):
    def findMaxLength(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        s = 0 
        max_len  = 0 
        f  = {0:-1}

        for i in range(len(nums)):
            s +=nums[i]

            if s in f:
                l = f[s]
                max_len= max(max_len, i - l)

            else:
                f[s] = i
        return max_len 



        
        