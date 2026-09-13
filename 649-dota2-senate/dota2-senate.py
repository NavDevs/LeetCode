class Solution(object):
    def predictPartyVictory(self, senate):
        senate = list(senate)
        n = len(senate)
        R , D  = deque(),deque()

        for i,c in enumerate(senate):

            if c == "R":
                R.append(i)
            else:
                D.append(i)

        while R and D:
            r = R.popleft()
            d = D.popleft()

            if r < d:
                R.append(n+d)
            else:
                D.append(r+n)

        return "Radiant" if R else "Dire"








        
        
        