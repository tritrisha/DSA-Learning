class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        r=len(grid)
        c=len(grid[0])
        oneinr=[0]*r
        oneinc=[0]*c

        for i in range(r):
            for j in range(c):
                oneinr[i]+=grid[i][j]
                oneinc[j]+=grid[i][j]


        for i in range(r):
            for j in range(c):
                grid[i][j]=2*oneinr[i]+2*oneinc[j] - r - c

        return grid


        



        