class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r=len(board)
        c=len(board[0])
        def dfs(i, j , k):
            if k==len(word):
                return True
            if i<0 or j<0 or i>=r or j>=c or board[i][j]!=word[k]:
                return False

            t=board[i][j]
            board[i][j]='#'
            if dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1):
                return True

            board[i][j]=t
            return False

        for i in range(r):
            for j in range(c):
                if board[i][j]==word[0] and dfs(i, j, 0):
                    return True

        return False




        