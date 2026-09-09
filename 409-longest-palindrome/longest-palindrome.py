class Solution(object):
    def longestPalindrome(self, s):
        l = 0
        has_odd = False
        freq = Counter(s)

        for i in freq.values():
            if i % 2  == 0:
                l += i
            else:
                l += i - 1
                has_odd = True

        if has_odd:
            l +=1
        
        return l 
        