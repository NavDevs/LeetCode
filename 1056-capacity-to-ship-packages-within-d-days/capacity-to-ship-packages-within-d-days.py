class Solution(object):
    def shipWithinDays(self, weights, days):
        l= max(weights)
        r  =  sum(weights)
        res = r

        def canShip(cap):
            ship = 1
            curCap= cap
            for w in weights:
                if curCap - w < 0:
                    ship+=1
                    curCap = cap
                curCap -= w
            return ship <= days

        while l <=r:
            cap = (l +r) //2

            if canShip(cap):
                res= min(res,cap)
                r = cap-1
            else:
                l = cap +1

        return res

        
        