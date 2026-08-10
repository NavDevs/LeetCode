class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        freq = {0:1}
        prefix = 0 
        c= 0

        for i in range(len(nums)):
            prefix += nums[i]

            need  = prefix - goal

            if need in freq:
                c +=freq[need]

            freq[prefix] = freq.get(prefix,0) +1
        return c


        
        