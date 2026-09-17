class Solution(object):
    def luckyNumbers(self, matrix):
        res  =[]

        for i in range(len(matrix)):
            small = min(matrix[i])

            for j in range(len(matrix[0])):
                if matrix[i][j]==small:
                    big = True

                    for k in range(len(matrix)):

                        if matrix[k][j] > small:
                            big = False
                            break

                    if big:
                        res.append(small)

        return res 
        