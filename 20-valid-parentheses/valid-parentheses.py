class Solution(object):
    def isValid(self, s):
        m = {
            ")":"(","}":"{","]":"["
        }
        st=[]
        for i in s:
            if i in "({[":
                st.append(i)
            else:
                if not st or  st.pop() != m[i]:
                    return False 
              
        return len(st)==0
        
                                 