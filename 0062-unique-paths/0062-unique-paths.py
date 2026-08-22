class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        vis=[[-1]*n for _ in range(m)]
        def up(i, j):
            if i==(m-1) and j==(n-1):
                return 1

            if i>=m or j>=n:
                return 0
            
            if vis[i][j]!=-1:
                return vis[i][j]
            
            vis[i][j]=up(i+1, j) + up(i, j+1)
            
            return vis[i][j]

        
        return up(0, 0)
        

        