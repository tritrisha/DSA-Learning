class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        c=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    c+=1

                if grid[i][j]==1:
                    start=[i, j]


        def up(i, j, c):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]==-1 or grid[i][j]==-2:
                return 

            if grid[i][j]==2:
                if c==0:
                    allp[0]+=1
                return 


            if grid[i][j]==0:
                c-=1
            grid[i][j]=-2
            up(i+1, j, c)
            up(i-1, j, c)
            up(i, j+1, c)
            up(i, j-1, c)
            grid[i][j]=0
            

        allp=[0]
        up(start[0], start[1],c)
        return allp[0]