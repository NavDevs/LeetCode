class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        s = 0
        ans = 0
        for i in range(k):
            s +=arr[i]
        if s >= threshold * k:
            ans +=1
        st= 0
        ed = k
        maxs =float("-inf")
        

        while ed < len(arr):

            s -= arr[st]
            st+=1

            s +=arr[ed]
            ed+=1
            

            if s >= threshold * k:
                ans  += 1

        return ans 

        