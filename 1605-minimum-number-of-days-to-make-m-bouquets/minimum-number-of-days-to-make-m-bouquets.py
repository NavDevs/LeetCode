class Solution(object):
    def minDays(self, bloomDay, m, k):
        n =len(bloomDay)
        if m * k > n:
            return -1  
        l = min(bloomDay)
        r = max(bloomDay)
        
        res = r
        def possible(bloomDay, m, k,days):
            b = 0 
            f = 0 

            for i in bloomDay:
                if i <= days:
                    f +=1
                    if f  == k:
                        b+=1
                        f= 0
                else:
                    f = 0
            return  b >= m
        while l <= r:

            days = (l +r) // 2

            if possible(bloomDay, m, k,days):
            
                r = days -1
            else:
                l = days +1
            
        return l
            
