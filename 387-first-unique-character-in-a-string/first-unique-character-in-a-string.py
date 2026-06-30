class Solution(object):
    def firstUniqChar(self, s):
        m = {}
        for i in s :
            m[i] =  m.get(i,0)+1
        for i,j in enumerate(s):
            if m[j] ==1:
                return i
        return -1

        
        