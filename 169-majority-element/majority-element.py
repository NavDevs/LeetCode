class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ma =Counter(nums)
        
        for i in ma:
            if ma[i] > len(nums)/2:
                return i