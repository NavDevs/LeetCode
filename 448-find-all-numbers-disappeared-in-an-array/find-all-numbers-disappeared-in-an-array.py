class Solution(object):
    def findDisappearedNumbers(self, nums):
        s= {}
        ans = []
        for i in range(len(nums)):
            s[nums[i]]= i
        
        for i in range(1,len(nums)+1):
            if i not in s:
                ans.append(i)
        return list(ans)

        



        