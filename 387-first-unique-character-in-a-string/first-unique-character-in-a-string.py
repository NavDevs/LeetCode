class Solution(object):
    def firstUniqChar(self, s):
        c = Counter (s)

        for i in range(len(s)):
            if c[s[i]] == 1:
                return i

        return -1 
       
        
        

        
        