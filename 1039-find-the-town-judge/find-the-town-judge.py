class Solution(object):
    def findJudge(self, n, trust):
        i = [0] * (n+1)
        o = [0] * (n+1)

        for a , b in trust:
            o[a] +=1
            i[b] +=1
        
        for j in range(1,n+1):
            if  i[j] == n-1 and  o[j] == 0:
                return j

        return -1

        
        