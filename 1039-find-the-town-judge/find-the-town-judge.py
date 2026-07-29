class Solution(object):
    def findJudge(self, n, trust):
        ind = [0] * (n+1)
        oud = [0] *(n+1)
        for a,b in trust:
            oud[a]+=1
            ind[b]+=1

        for i in range(1,n+1):
            if ind[i] == n-1 and oud[i] == 0:
                return i
            
        return -1

        
        