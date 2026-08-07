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

        while q:
            i, j, cou=q.popleft()
            cou+=1
            if i+1<r and g[i+1][j]==1:
                g[i+1][j]=2
                q.append([i+1, j, cou])

            if j+1<c and g[i][j+1]==1:
                g[i][j+1]=2
                q.append([i, j+1, cou])

            if i-1>=0 and g[i-1][j]==1:
                g[i-1][j]=2
                q.append([i-1, j, cou])

            if j-1>=0 and g[i][j-1]==1:
                g[i][j-1]=2
                q.append([i, j-1, cou])
            

        print(g) 
        print(grid)
        for i in range(r):
            for j in range(c):
                if g[i][j]==1:
                    return -1

        if cou==0:
            return 0
        return cou-1


            

            



            
        

            


        
                

        


        

        