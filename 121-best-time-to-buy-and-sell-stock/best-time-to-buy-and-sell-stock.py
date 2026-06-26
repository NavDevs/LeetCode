class Solution(object):
    def maxProfit(self, prices):
        l=0
        r = 1
        ans = 0
        while r < len(prices):
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]
                ans = max(ans,profit)
            else:
                l=r
            r+=1
        return ans            

        