class Solution(object):
    def largestAltitude(self, gain):
        prefix  = [0]

        for i in gain:
            prefix.append(prefix[-1] + i)

        return max(prefix)        
        