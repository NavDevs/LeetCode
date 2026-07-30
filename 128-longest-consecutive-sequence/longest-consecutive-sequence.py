class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)

        longest = 0 

        for num  in numSet:

            if num - 1 not in numSet:
                current  = num
                lenght  = 1
                
                while current + 1 in numSet:
                    current = current + 1
                    lenght +=1
                
                longest = max(longest,lenght)
        return longest
       
        
        