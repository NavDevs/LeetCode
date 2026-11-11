class Solution(object):
    def compress(self, chars):
        i = 0 
        insert = 0

        while i < len(chars):

            grp = 1

            while (grp + i) < len(chars) and chars[grp + i ] == chars[i]:
                grp +=1

            chars[insert] = chars[i]
            insert += 1

            if grp > 1:

                s = str(grp)
                chars[insert:insert+len(s)] = list(s)
                insert += len(s) 

            i += grp

        return insert 


            
       