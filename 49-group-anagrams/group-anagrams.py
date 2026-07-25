class Solution(object):
    def groupAnagrams(self, strs):
        a ={}

        for i in strs:
            sot = "".join(sorted(i)) 

            if sot in a:
                a[sot].append(i)

            else:
                a[sot] = [i]

        return list(a.values())       
        

            
        