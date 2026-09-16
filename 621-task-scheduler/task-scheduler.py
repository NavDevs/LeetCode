from collections import Counter
class Solution(object):
    def leastInterval(self, tasks, n):
        d = Counter(tasks)
         
        lst = sorted(d.values(),reverse = True)

        max_num = lst[0]
        i = 1
        c = 1

        while i < len(lst) and lst[i] == max_num:
            i += 1
            c +=1

        ret= (max_num-1)*(n+1) + c

        return max(ret,len(tasks))

            

                                      
        