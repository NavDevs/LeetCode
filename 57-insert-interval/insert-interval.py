class Solution:
    def insert(self, intervals, new):
        res  =[]

        for i in range(len(intervals)):

            if intervals[i][1] < new[0]:
                res.append(intervals[i])

            elif intervals[i][0] > new[1]:
                res.append(new)
                new = intervals[i]

            else:

                new[0] = min(new[0], intervals[i][0])
                new[1] = max(new[1],intervals[i][1])

        res.append(new)
        
        return res