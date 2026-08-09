class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r=len(grid)
        c=len(grid[0])
        q=deque()
        vis=[[False]*c for _ in range(r)]

        di=[0,1,0,-1,0]
        def bfs():
            while q:
                i, j=q.popleft()
                vis[i][j]=True
                for k in range(4):
                    x=i+di[k]
                    y=j+di[k+1]
                    if x<0 or y<0 or x>=r or y>=c or vis[x][y]:
                        continue

                    if grid[x][y]=="1":
                        vis[x][y]=True
                        q.append([x,y])

            return 1


        count=0
        for ri in range(r):
            for cj in range(c):
                if grid[ri][cj]=="1" and not vis[ri][cj]:
                    print(grid[ri][cj])
                    q.append([ri, cj])
                    count+=bfs()


        return count




        


        


                


                    
            
        