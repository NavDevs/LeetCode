class Solution(object):
    def maxProfit(self, prices):
        m = prices[0]
        ma  =0 

        for i in range(1,len(prices)):
            m = min(m, prices[i])
            ma = max(ma, prices[i] - m)
        
        return ma 
        
        


                 

        