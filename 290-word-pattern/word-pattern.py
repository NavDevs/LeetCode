class Solution(object):
    def wordPattern(self, pattern, s):
        words  = s.split(" ")
        if len(words) != len(pattern):
            return False 
        
        
        m1  ={}
        m2 ={}

        for i,j in zip(pattern,words):
            if i in m1 and m1[i] !=j:
                return False
            if j in m2 and m2[j] !=i:
                return False 
            m1[i] = j
            m2[j] = i
        return True 

        
        