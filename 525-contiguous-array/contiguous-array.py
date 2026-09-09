class Solution(object):
    def findMaxLength(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        s = 0
        f = {0:-1}
        maxlen = 0 

        for i in range(len(nums)):
            s += nums[i]

            if s in f:
                l = f[s]
                maxlen = max(maxlen, i - l)
            else:
                f[s] = i
        
        return maxlen         


        
        