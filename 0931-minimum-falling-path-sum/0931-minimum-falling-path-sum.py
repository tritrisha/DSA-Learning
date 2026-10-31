class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n=len(matrix)
        def ds(i, j):
            if i<0 or i>=n:
                return 0

            if j<0 or j>=n:
                return float('inf')

            if dp[i][j]!='x':
                return dp[i][j]

            dp[i][j]=min(ds(i+1, j-1), ds(i+1, j), ds(i+1, j+1))+matrix[i][j]
            return dp[i][j]

        m=float('inf')
        dp=[['x']*n for _ in range(n)]
        for i in range(n):
            m=min(m, ds(0, i))
        return m
        