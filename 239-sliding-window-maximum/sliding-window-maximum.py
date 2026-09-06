from collections import deque

class Solution(object):

    def maxSlidingWindow(self, nums, k):

        dq = deque()
        ans = []

        for r in range(len(nums)):

            while dq and dq[0] <= r - k:
                dq.popleft()

            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()

            dq.append(r)

            if r >= k - 1:
                ans.append(nums[dq[0]])

        return ans