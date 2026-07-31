class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])

        def dfs(i, j):
            if i<0 or j<0 or i>=r or j>=c or grid[i][j]==0:
                return 1

            if grid[i][j]==-1:
                return 0
            grid[i][j]=-1
            return dfs(i+1, j)+ dfs(i-1, j)+dfs(i, j+1)+dfs(i, j-1)
        
        p=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    p+=dfs(i,j)


        return p


        