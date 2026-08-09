class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        q=deque()
        for i in range(r):
            if grid[i][0]==1:
                q.append([i, 0])

            if grid[i][c-1]==1:
                q.append([i, c-1])

        for j in range(c):
            if grid[0][j]==1:
                q.append([0, j])
            
            if grid[r-1][j]==1:
                q.append([r-1, j])

        d=[0,1,0,-1,0]
        while q:
            i, j=q.popleft()
            grid[i][j]=0
            for m in range(4):
                x=i+d[m]
                y=j+d[m+1]

                if x<0 or y<0 or x>=r or y>=c or grid[x][y]==0:
                    continue

                grid[x][y]=0
                q.append([x, y])

        count=0
        for i in range(1, r-1):
            count+=sum(grid[i])
                


        return count



