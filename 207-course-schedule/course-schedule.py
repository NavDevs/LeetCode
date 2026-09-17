class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        indegree= [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for c , pre in prerequisites:
            graph[pre].append(c)
            indegree[c] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        count  = 0

        while q:

            node = q.popleft()
            count+=1

            for i in graph[node]:
                indegree[i] -= 1

                if indegree[i] == 0:
                    q.append(i)

        return count == numCourses



             
        
        