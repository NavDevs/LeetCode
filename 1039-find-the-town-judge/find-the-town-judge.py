class Solution(object):
    def findJudge(self, n, trust):
        ind = [0]*(n+1)
        o = [0]*(n+1)

        for a,b in trust:
            ind[a]+=1
            o[b]+=1

        for i in range(1,n+1):
            if ind[i] == 0 and  o[i] == n -1 :
                return i 

        return -1 
        
       
        