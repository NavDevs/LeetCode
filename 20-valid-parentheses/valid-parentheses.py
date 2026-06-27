class Solution(object):
    def isValid(self, s):
        st =[]
        Map = {")": "(", "]": "[","}": "{", }
        for i in s:
            if i in Map:
                if st and st[-1]==Map[i]:
                    st.pop()
                else:
                    return False
            else:
                st.append(i)
        return len(st)==0
        
                                 