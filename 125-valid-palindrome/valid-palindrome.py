class Solution(object):
    def isPalindrome(self, s):
        newStr =""
        for i in s:
            if i.isalnum():
                newStr += i.lower()
        l = 0
        r  = len(newStr)-1
        while l<=r:
            if newStr[l] != newStr[r]:
                return False
            l +=1
            r-=1
        return True 

