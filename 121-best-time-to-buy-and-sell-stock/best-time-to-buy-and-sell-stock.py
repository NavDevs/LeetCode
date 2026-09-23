class Solution(object):
    def maxProfit(self, prices):
        minProfit  = prices[0]
        maxProfit = 0 

        for i in range(1,len(prices)):

            minProfit =  min(minProfit, prices[i])

            maxProfit = max(maxProfit, prices[i] - minProfit)

        return maxProfit 
        
        


                 

        