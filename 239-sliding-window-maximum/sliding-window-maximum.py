from collections import deque

class Solution(object):

    def maxSlidingWindow(self, nums, k):

        dq = deque()
        ans = []
        l = r = 0

        while r < len(nums):

            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            if l > dq[0]:
                dq.popleft()

            if (r + 1) >= k:
                ans.append(nums[dq[0]])
                l+=1
            r+=1
            

        return ans  