class Solution(object):
    def maximumSubarraySum(self, nums, k):

        left = 0
        window_sum = 0
        max_sum = 0

        count = {}

        for right in range(len(nums)):

            # Add right element
            window_sum += nums[right]

            if nums[right] in count:
                count[nums[right]] += 1
            else:
                count[nums[right]] = 1

            # Keep window size exactly k
            if right - left + 1 > k:

                left_element = nums[left]

                window_sum -= left_element
                count[left_element] -= 1

                if count[left_element] == 0:
                    del count[left_element]

                left += 1

            # Check the window
            if right - left + 1 == k:

                # All k elements are distinct
                if len(count) == k:
                    max_sum = max(max_sum, window_sum)

        return max_sum