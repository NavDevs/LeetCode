class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        res = []
        
        i= 0
        j = 0

        while i < len(firstList) and j < len(secondList):

            s =  max(firstList[i][0],secondList[j][0])
            e  = min(firstList[i][1],secondList[j][1])

            if s <= e :
                res.append([s,e])

            if firstList[i][1] < secondList[j][1]:
                i +=1
            else:
                j +=1

        return res 

        