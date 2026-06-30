class Solution(object):
    def countPrimes(self, n):
        if n <=2:
            return 0
        isp = [True]*n
        isp[0]=isp[1]=False

        for i in range(2, int(n**0.5)+1):
            if isp[i]:
                for j in range(i*i,n,i):
                    isp[j]=False
        
        return sum(isp)