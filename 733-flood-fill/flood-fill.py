class Solution(object):
    def floodFill(self, image, sr, sc, color):
        rows = len(image)
        cols = len(image[0])

        OG = image[sr][sc]

        if OG == color:
            return image

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if image[r][c] != OG:
                return

            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)

        return image