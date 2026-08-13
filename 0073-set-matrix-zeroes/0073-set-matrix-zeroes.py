class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        r=len(matrix)
        c=len(matrix[0])
        q=deque()
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    q.append([i, j])
                    

        while q:
            i, j=q.popleft()
            for row in range(r):
                matrix[row][j]=0
                matrix[row][j]=0

            for col in range(c):
                matrix[i][col]=0
                matrix[i][col]=0


        
            
        