class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        ms = Counter(s)
        
        for i in t:
            if ms[i] == 0:
                return False
            if ms[i] < 0:
                return False
            ms[i] -=1

        return True 
            
        


        
       

        

        
 