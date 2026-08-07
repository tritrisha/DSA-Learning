class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        g=copy.deepcopy(grid)
        q=deque()
        cou=0
        for i in range(r):
            for j in range(c):
                if g[i][j]==2:
                    q.append([i, j, cou])

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
                q.append([nx, ny, cou])

        for i in range(r):
            if 1 in g[i]:
                return -1

        if cou==0:
            return 0
        return cou-1


            

            



            
        

            


        
                

        


        

        