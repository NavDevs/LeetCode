class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        l = 0
        maxlen =0

        for r in range(len(s)):
            if s[r] in seen:
                l = max(l,seen[s[r]]+1)

            seen[s[r]] = r
            maxlen = max(maxlen,r-l+1)

        return maxlen 



        

        
        
        