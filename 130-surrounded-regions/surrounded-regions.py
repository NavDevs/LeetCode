class Solution(object):
    def solve(self, board):
        if not board:
            return 

    
        row = len(board)
        col = len(board[0])

        if not board:
            return 0

        def dfs(r,c):

            if r < 0 or r >= row or c < 0 or c >= col:
                return 

            if board[r][c] != 'O':
                return 

            board[r][c] = '#'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r ,c + 1)
            dfs(r , c -1)

        for r in range(row):
            dfs(r,0)
            dfs(r,col-1)
        
        for c in range(col):
            dfs(0,c)
            dfs(row-1,c)

        for r in range(row):
            for c in range(col):

                if board[r][c] == 'O':
                    board[r][c] = 'X'

                elif board[r][c] == '#':
                    board[r][c] = 'O'


                

            
        