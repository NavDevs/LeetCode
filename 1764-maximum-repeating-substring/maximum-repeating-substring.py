class Solution(object):
    def maxRepeating(self, sequence, word):
        cnt  = 0
        temp = word

        while temp in sequence:

            cnt +=1
            temp += word


        return cnt 
                
        