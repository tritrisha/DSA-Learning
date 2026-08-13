class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        d=copy.deepcopy(matrix)
        for r in range(n):
            for c in range(n):
                d[r][c]= matrix[c][r]


        for i in range(n):
            matrix[i]=d[i][::-1]
            


            
        