class Solution(object):
    def possible(self,diff,price,k):
        c= 1
        l = price[0]
        for i in range(1,len(price)):
            if price[i] - l >= diff:
                c+=1
                l = price[i]
        return c >= k
    
    def maximumTastiness(self, price, k):
        price.sort()
        l = 0
        r= price[-1]-price[0]

        while l <= r:
            diff = (l+r) //2
            if self.possible(diff, price, k):
                l = diff + 1
            else:
                r = diff - 1
        return r

        
        