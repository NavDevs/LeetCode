class Solution(object):
    def firstUniqChar(self, s):
        m =Counter(s)
        
        for i in range(len(s)):
            if m[s[i]] ==1:
                return i
        return -1

        
        

        
        