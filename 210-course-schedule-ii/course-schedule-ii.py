class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        graph = [[] for  _ in range(numCourses)]

        for c, pre in prerequisites:
            graph[pre].append(c)
            indegree[c] +=1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        res = []

        while q:

            node = q.popleft()
            res.append(node)

            for i in graph[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        return res if len(res) == numCourses else []


        