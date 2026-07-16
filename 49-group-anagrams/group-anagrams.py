class Solution(object):
    def groupAnagrams(self, strs):
        a ={}
        for i in strs:
            sorted_word = "".join(sorted(i))
            if sorted_word in a:
                a[sorted_word].append(i)
            else:
                a[sorted_word] = [i]
        return list(a.values())

            
        