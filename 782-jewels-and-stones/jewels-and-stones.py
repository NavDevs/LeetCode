class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        c = 0
        jewels_set = set(jewels)

        for stone in stones:
            if stone in jewels:
                c+=1

        return c 
        