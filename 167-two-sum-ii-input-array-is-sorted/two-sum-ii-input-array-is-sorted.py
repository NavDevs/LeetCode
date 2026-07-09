class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers)-1

        while l<=r:
            t  = numbers[l]+numbers[r]
            if t  == target:
                return [l+1,r+1]
            elif t < target:
                l +=1
            else:
                r-=1
        