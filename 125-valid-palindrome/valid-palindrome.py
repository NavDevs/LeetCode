class Solution(object):
    def isPalindrome(self, s):
        new  = []

        for i in s:
            if i.isalnum():
                new.append(i.lower())
        
        l = 0
        r=len(new)-1

        while l <= r:

            if new[l] != new[r]:
                return False
            l+=1
            r-=1
        return True 
        
        
        
       

