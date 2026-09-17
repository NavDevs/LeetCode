class Solution(object):
    def findComplement(self, num):
        bits = bin(num)[2:]
        complement = ""

        for i in bits:
            if i == "0":
                complement += '1'
            else:
                complement += '0'
        return int(complement,2)
            
        