class Solution:
    def canConstruct(self, ransomNote, magazine):
        if len(magazine) < len(ransomNote):
            return False 
        c = {}
        for i in magazine:
            c[i] = 1 + c.get(i,0)
        
        for i in ransomNote:
            if i not in c:
                return False
            if c[i] == 0:
                return False
            c[i] -= 1
        return True 
        
        
