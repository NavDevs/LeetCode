class Solution(object):
    def maxVowels(self, s, k):
        su = 0 
        
        
        for i in range(k):
            if s[i] in "aeiou":
                su +=1
            
        ans = su

        st = 0 
        ed  = k 
        
        while ed < len(s):
            if s[st] in "aeiou":
                su -=1
            st +=1

            if s[ed] in "aeiou":
                su+=1
            ed+=1

            ans = max (ans, su)
        
        return ans 
        

        
        
        