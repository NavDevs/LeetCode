class Solution(object):
    def countStudents(self, students, sandwiches):
        c  =  Counter(students)
        res = len(students)

        for i in sandwiches:
            if c[i] > 0:
                res -=1
                c[i] -=1
            else:
                return res 
            
        return res 
        
        