class Solution(object):
    def isValid(self, s):
        st =[]
        Map = {")": "(", "]": "[","}": "{", }
        for i in s:
            if i in "({[":
                st.append(i)
            elif not st or st.pop() != Map[i]: 
                return False
        return len(st)==0
        
                                 