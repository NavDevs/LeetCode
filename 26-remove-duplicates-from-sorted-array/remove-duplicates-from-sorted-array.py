class Solution(object):
    def removeDuplicates(self, nums):
        ans = sorted(set(nums))

        for i in range(len(ans)):
            nums[i] = ans[i]

        return len(ans)