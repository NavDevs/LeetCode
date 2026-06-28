class Solution(object):
    def dailyTemperatures(self, temperatures):
        st =[]
        res = [0]*len(temperatures)
       
        for i in range(len(temperatures)):
            while st and (temperatures[i] > temperatures[st[-1]]):
                prev = st.pop()
                res[prev]= i - prev
            st.append(i)
        return res
