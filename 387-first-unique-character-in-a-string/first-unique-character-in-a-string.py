class Solution(object):
    def firstUniqChar(self, s):
        m= {}

        for i in s:
            m[i] = 1 + m.get(i,0)

        for i in range(len(s)):
            if m[s[i]] == 1:
                return i
        return -1

        