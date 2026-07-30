class Solution(object):
    def groupAnagrams(self, strs):
        m = {}

        for i in strs:
            sorted_word  =  "".join(sorted(i))
            if  sorted_word in m:
                m[sorted_word].append(i)
            else:
                m[sorted_word] = [i]
        
        return list(m.values())
        