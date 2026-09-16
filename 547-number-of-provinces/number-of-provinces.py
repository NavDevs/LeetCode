class Solution(object):
    def findCircleNum(self, isConnected):
        n =  len(isConnected)

        v =[False]* n

        def dfs(node):
            v[node] =True
            for i in range(n):
                if not v[i] and isConnected[node][i] == 1:
                    dfs(i)
                    
        c = 0

        for i in range(n):
            if not v[i]:
                c +=1
                dfs(i)

        return c


        