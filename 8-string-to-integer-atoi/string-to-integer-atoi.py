class Solution(object):
    def myAtoi(self, s):
        i =0
        si =1
        s = s.lstrip()
        if not s :
            return 0

        if s[i] == "-":
            si = -1
            i+=1
        elif s[i] == "+":
            i +=1


        num =0

        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i +=1

        num =  num * si

        if num < -2147483648:
            return -2147483648

        if num > 2147483647:
            return 2147483647

        return num

        

        