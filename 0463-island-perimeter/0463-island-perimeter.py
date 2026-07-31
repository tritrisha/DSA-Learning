class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])

        # def dfs(i, j):
        #     if i<0 or j>0 or i>=r or j>=c:
        #         return 1

        #     return dfs(i+1, j)+ dfs(i-1, j)+ dfs(i, j+1)+ dfs(i, j-1)
        
        p=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    if i-1<0:
                        p+=1
                    else:
                        if grid[i-1][j]==0:
                            p+=1

                    if j-1<0:   
                        p+=1
                    else:
                        if grid[i][j-1]==0:
                                p+=1

                    if i+1>=r:
                        p+=1

                    else:
                        if grid[i+1][j]==0: 
                            p+=1

                    if j+1>=c:
                        p+=1

                    else:
                        if grid[i][j+1]==0:
                            p+=1


        return p


        


        