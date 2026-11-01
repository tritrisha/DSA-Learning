class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n=len(triangle)
        for i in range(n-1, 0, -1):
            for j in range(i):
                triangle[i-1][j]=min(triangle[i][j], triangle[i][j+1])+triangle[i-1][j]

        return triangle[0][0]

            

        



