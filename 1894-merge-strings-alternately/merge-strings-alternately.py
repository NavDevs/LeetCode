class Solution(object):
    def mergeAlternately(self, word1, word2):
        l = 0
        r  =0 
        new = ""

        while l < len(word1) or r < len(word2):
            if l < len(word1):
                new+= word1[l]
                l+=1
            if r < len(word2):
                new +=word2[r] 
                r+=1
        return new 
        