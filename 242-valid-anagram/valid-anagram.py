class Solution(object):
    def isAnagram(self, s, t):
        if  len(s)!= len(t):
            return  False
        count ={}

        for i in s:
            count[i]=count.get(i,0)+1
    

        for i in t:
            if i not in count:
                return False
            elif count[i] == 0:
                return False
            else:
                count[i]-=1
        return True

        
 