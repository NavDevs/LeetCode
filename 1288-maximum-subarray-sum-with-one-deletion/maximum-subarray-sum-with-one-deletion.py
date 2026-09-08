class Solution(object):
    def maximumSum(self, arr):
        curNodel = ans = arr[0]
        curOneDel  = float("-inf")

        for i in arr[1:]:
            prev = curNodel

            curNodel = max(i,curNodel+i)
            curOneDel = max(prev,curOneDel+i)

            ans  = max(ans,curNodel,curOneDel)

        return ans 
        