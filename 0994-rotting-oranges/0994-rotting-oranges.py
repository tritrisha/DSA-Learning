class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        g=grid
        q=deque()
        cou=-1
        efresh=0
        for i in range(r):
            for j in range(c):
                if g[i][j]==2:
                    q.append([i, j, cou])

                if g[i][j]==1:
                    efresh+=1

        if efresh==0:
            return 0

        direc=[(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            i, j, cou=q.popleft()
            cou+=1
            for x, y in direc:
                nx=x+i
                ny=j+y

                if nx<0 or ny<0 or nx>=r or ny>=c or g[nx][ny]!=1:
                    continue

                g[nx][ny]=2
                efresh-=1
                q.append([nx, ny, cou])
            
        return cou if efresh==0 else -1


            

            



            
        

            


        
                

        


        

        