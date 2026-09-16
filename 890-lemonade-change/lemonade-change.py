class Solution(object):
    def lemonadeChange(self, bills):
        f , t = 0 , 0 

        for b in bills:
            if b == 5:
                f +=1
            if b == 10:
                t +=1

            change = b - 5
            if change == 5:
                if f > 0:
                    f -=1
                else:
                    return False

            elif change == 15:
                if f  and t :
                    f , t  = f -1  , t  - 1
                elif f >= 3 :
                    f  -= 3
                else:
                    return False

        return True  

        