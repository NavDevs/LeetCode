class Solution(object):
    def canVisitAllRooms(self, rooms):
        v = [False] * len(rooms)

        def dfs(start):
            v[start] = True

            for i in rooms[start]:
                if not v[i]:
                    dfs(i)

        dfs(0)        

        return all(v)
        