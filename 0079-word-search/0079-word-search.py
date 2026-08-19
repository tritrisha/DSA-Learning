class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r=len(board)
        c=len(board[0])
        visa=[[0]*c for _ in range(r)]
        s=[]
        def dfs(i, j,k):
            if i<0 or j<0 or i>=r or j>=c or k>=len(word) or board[i][j]!=word[k] or visa[i][j]==1 :
                return

            visa[i][j]=1
            s.append(word[k])
            dfs(i-1, j, k+1 )
            dfs(i+1, j, k+1)
            dfs(i, j-1, k+1 )
            dfs(i, j+1, k+1)
            
            if word=="".join(s):
                return 
            else:
                s.pop(-1)
                visa[i][j]=0
               
                

        for i in range(r):
            for j in range(c):
                if board[i][j]==word[0]:
                    dfs(i, j, 0)
                    if len(s)==len(word):
                        return True

        return False


        