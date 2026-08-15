class Solution(object):
    def predictPartyVictory(self, senate):
        senate  = list(senate)
        R,D = deque(),deque()

        for i,c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)

        while R and D:

            r  = R.popleft()
            d = D.popleft()

            if r < d:
                R.append(len(senate) +d)
            else:
                D.append(len(senate) +r)
        
        return "Radiant" if R else "Dire"







        
        
        