class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        happy  = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                happy += customers[i]

        l = 0 
        ans =0
        extra = 0

        for r in range(len(customers)):

            if grumpy[r] == 1:
                extra += customers[r]

            if r - l +1 == minutes:
                ans  = max(extra,ans)

                if grumpy[l] == 1:
                    extra -= customers[l]

                l +=1
        return ans + happy   

        