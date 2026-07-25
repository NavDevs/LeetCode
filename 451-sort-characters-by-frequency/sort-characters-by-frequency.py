class Solution(object):
    def frequencySort(self, s):

        ans =""
        freq  = {}
        for i in s:
            freq[i]  = 1 + freq.get(i,0)

        for i in sorted(freq, key = freq.get, reverse = True ):
            ans += i *freq[i]

        return ans 
        
        