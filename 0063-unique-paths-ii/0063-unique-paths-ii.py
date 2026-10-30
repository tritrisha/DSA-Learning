class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        r=len(obstacleGrid)
        c=len(obstacleGrid[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c or obstacleGrid[i][j]==1:
                return 0

            if i==r-1 and j==c-1:
                return 1

            if dp[i][j]!=-1:
                return dp[i][j]

            dp[i][j]=dfs(i+1, j)+dfs(i, j+1)
            return dp[i][j]

        dp=[[-1]*c for _ in range(r)]
        return dfs(0, 0)
        