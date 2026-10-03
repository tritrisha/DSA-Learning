class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        def dfs(i, j, c, ori):
            if i<0 or j<0 or i>=row or j>=col or image[i][j]!=ori or image[i][j]==c:
                return

            image[i][j]=c
            dfs(i+1, j, c, ori)
            dfs(i-1, j, c, ori)
            dfs(i, j+1, c, ori)
            dfs(i, j-1, c, ori)
            return
            



        row=len(image)
        col=len(image[0])
        orig=image[sr][sc]
        dfs(sr,sc,color, orig)
        return image
        