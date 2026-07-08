class Solution(object):
    def isValid(self, s):
        m = {
            ")":"(","}":"{","]":"["
        }
        stm  =[]
        for i in s:
            if i in "({[":
                stm.append(i)
            elif not stm or stm.pop() != m[i]:
                return False
            
        return len(stm) == 0
            
        
                                 