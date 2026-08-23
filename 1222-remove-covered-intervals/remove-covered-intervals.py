class Solution(object):
    def removeCoveredIntervals(self, intervals):
        res  =len(intervals)
        intervals.sort( key = lambda x : (x[0],-x[1]))

        prev  = intervals[0]

        for i in range(1,len(intervals)):

            cur  =  intervals[i]

            if cur[1] <= prev[1]:
                res  -=1
            else:    
                prev  = cur 
        return res 
        