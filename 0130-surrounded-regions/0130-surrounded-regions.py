class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q=deque()
        r=len(board)
        c=len(board[0])
        vis=[[False]*c for _ in range(r)]
        for i in range(r):
            if board[i][0]=="O":
                q.append([i, 0])

        for j in range(c):
            if board[0][j]=="O":
                q.append([0, j])

        for i in range(r):
            if board[i][c-1]=="O":
                q.append([i, c-1])

        for j in range(c):
            if board[r-1][j]=="O":
                q.append([r-1, j])

        dire=[0, 1, 0, -1, 0]
        while q:
            i, j= q.popleft()
            vis[i][j]=True
            for k in range(len(dire)-1):
                x=i+dire[k]
                y=j+dire[k+1]
                if x<0 or y<0 or x>=r or y>=c or vis[x][y]:
                    continue
                if board[x][y]=="O":
                    vis[x][y]=True
                    q.append([x,y])


        for i in range(r):
            for j in range(c):
                if board[i][j]=="O" and not vis[i][j]:
                    board[i][j]="X"

        



        


            



    

        