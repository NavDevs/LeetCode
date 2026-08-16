class Solution(object):
    def leastInterval(self, tasks, n):
        d  ={}

        for i in tasks:
            d[i] = d.get(i,0)+1

        lst = sorted(d.values(),reverse=True)

        max_number = lst[0]
        i = 0
        c = 0
        while i < len(lst) and lst[i] == max_number:
            c +=1
            i+=1

        ret = (max_number -1) * (n+1) + c
        return max(ret,len(tasks))

            

                                      
        