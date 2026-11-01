class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n=len(triangle)
        dp=[[0]*n for _ in range(n)]
        for i in range(n):
            dp[n-1][i]=triangle[n-1][i]
        for i in range(n-1, 0, -1):
            for j in range(i):
                dp[i-1][j]=min(dp[i][j], dp[i][j+1])+triangle[i-1][j]

        return dp[0][0]

            

        



