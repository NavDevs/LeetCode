class Solution(object):
    def totalFruit(self, fruits):
        maxlen = 0
        l = 0
        c= {} 

        for r in range(len(fruits)):
            c[fruits[r]] = c.get(fruits[r],0)+1

            while len(c) > 2:
                c[fruits[l]] -= 1
                if c[fruits[l]] == 0:
                    del c[fruits[l]]
                l+=1

            maxlen = max(maxlen,r-l+1)

        return maxlen 

            

        