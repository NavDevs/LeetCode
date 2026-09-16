class Solution(object):
    def findJudge(self, n, trust):
        indegree = [0] * (n+1)
        outdegree = [0] * (n+1)

        for a , b in trust:
            indegree[a] +=1
            outdegree[b] +=1

        for i in range(1,n+1):

            if indegree[i] == 0 and outdegree[i] == n - 1:
                return i

        return -1             
       
        