class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r=len(mat)
        c=len(mat[0])
        q=deque()
        vis=[[False]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if mat[i][j]==0:
                    q.append([i, j])
                    

        dis=[(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            i, j=q.popleft()
            cou=0
            for x, y in dis:
                ni=i+x
                nj=j+y
                if ni<0 or nj<0 or ni>=r or nj>=c:
                    continue

                if mat[ni][nj]==1 and not vis[ni][nj]:
                    mat[ni][nj]=mat[i][j]+1
                    vis[ni][nj]=True
                    q.append([ni, nj])

        return mat