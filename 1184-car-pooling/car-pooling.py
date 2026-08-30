class Solution(object):
    def carPooling(self, trips, capacity):
        p = 0 

        for km in range(1001):

            for num , st ,ed in trips:
                if ed == km:
                    p -= num

            for num , st, ed in trips:
                if st ==  km:
                    p +=num 

            if p  > capacity:
                return False
        
        return True 

        