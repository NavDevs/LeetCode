class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        c ={}
        for i in s:
            c[i]=1+c.get(i,0)
        for i in t:
            if i not in c:
                return False
            c[i] -=1 
            if c[i] < 0:
                return False
        return True
                
       

        

        
 