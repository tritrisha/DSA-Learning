class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])

        def dfs(i, j):
            if i<0 or j<0 or i>=r or j>=c:
                return 

            if grid[i][j]==1:
                grid[i][j]=0
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j-1)
                dfs(i, j+1)

            return 

        for j in range(c):
            if grid[0][j]==1:
                dfs(0, j)

            if grid[r-1][j]==1:
                dfs(r-1, j)

        

        for i in range(r):
            if grid[i][0]==1:
                dfs(i, 0)

            if grid[i][c-1]==1:
                dfs(i, c-1)

        cou=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    cou+=1
                    

        return cou

        
        