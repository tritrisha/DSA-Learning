class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        r=len(isWater)
        c=len(isWater[0])
        vis=[[-1]*c for _ in range(r)]
        q=deque()

        for i in range(r):
            for j in range(c):
                if isWater[i][j]==1:
                    q.append([i, j])
                    vis[i][j]=0


        dis=[(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            i, j=q.popleft()

            for x, y in dis:
                nx=x+i
                ny=y+j
                if nx<0 or ny<0 or nx>=r or ny>=c or vis[nx][ny]!=-1:
                    continue
                vis[nx][ny]=vis[i][j]+1
                q.append([nx, ny])
        

        return vis

                
                

        


                    

        



                


        
        

