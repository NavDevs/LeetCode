class Solution(object):
    def findWords(self, words):
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        w = []

        for i in words:
            w.append(i.lower())
        ans = []


        for i in range(len(w)):
            if all( j in row1 for j in w[i]):
                ans.append(words[i])
                
            elif all( j in row2 for j in w[i]):
                ans.append(words[i])

            elif all( j in row3 for j in w[i]):
                ans.append(words[i])

        return list(ans)            
        
        