class Solution(object):
    def groupAnagrams(self, strs):
        anagram  ={}

        for i in strs:
            sorted_words = "".join(sorted(i))

            if sorted_words in anagram:
                anagram[sorted_words].append(i)
            else:
                anagram[sorted_words]  = [i]

        return list(anagram.values())      
        

            
        