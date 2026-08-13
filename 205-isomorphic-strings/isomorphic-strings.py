class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        m1  ={}
        m2  ={}

        for i,j in zip(s,t):
            if i in m1 and m1[i] != j:
                return False
            if j in m2 and m2[j] != i:
                return False
            m1[i] = j
            m2[j] = i
        return True 

                      
        
        