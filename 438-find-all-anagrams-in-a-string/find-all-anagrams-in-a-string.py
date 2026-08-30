class Solution(object):
    def findAnagrams(self, s, p):
        ans = []
        
        if len(p) > len(s):
            return ans

        p_count = [0] * 26
        s_count = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        for i in range(len(p)):
            s_count[ord(s[i]) - ord('a')] += 1

        if s_count == p_count:
            ans.append(0)

        for i in range(len(p), len(s)):

            # Add new character
            s_count[ord(s[i]) - ord('a')] += 1

            # Remove old character
            s_count[ord(s[i - len(p)]) - ord('a')] -= 1

            if s_count == p_count:
                ans.append(i - len(p) + 1)

        return ans