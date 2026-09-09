class Solution(object):
    def findDuplicate(self, nums):
        nondup = set()
        dup =[]
        for i in nums:
            if i in nondup:
                dup.append(i)
            else:
                nondup.add(i)
        return dup[0]         