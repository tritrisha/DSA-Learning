class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        def ds(x, y):
            if x>=len(triangle) or y>=len(triangle):
                return 0

            if dp[x][y]!='x':
                return dp[x][y]
            dp[x][y]=min(ds(x+1, y+1), ds(x+1, y))+triangle[x][y]
            return dp[x][y]
            

        n=len(triangle)
        dp=[['x']*n for _ in range(n)]

        return ds(0, 0)
        



