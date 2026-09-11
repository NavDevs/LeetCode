class Solution(object):
    def removeKdigits(self, num, k):
        st = []

        for i in num:
            while st and k > 0 and st[-1] > i:
                st.pop()
                k -= 1
            st.append(i)

        while k > 0:
            st.pop()
            k -= 1

        ans = ''.join(st).lstrip('0')

        if ans =='':
            return '0'

        return ans 


        