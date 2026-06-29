
class Solution(object):
    def minEatingSpeed(self, piles, h):
        l = 1 
        r =  max (piles)

        while l <= r :
            m = (l +r) // 2
            hour  =  sum((p + m - 1)//m for p  in piles)
            
            if hour <= h:
                r = m -1
            else:
                l = m +1
        return  l

        