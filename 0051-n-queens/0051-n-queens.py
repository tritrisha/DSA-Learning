class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def checksafe(i, j, r): 
            for y in range(n):
                if r[y][j]=='Q':
                    return False
            x, y = i, j 
            while x >= 0 and y >= 0:
                if r[x][y] == 'Q':
                    return False
                x-=1
                y-=1
            
            x, y = i, j 
            while x>=0 and y < n:
                if r[x][y] == 'Q':
                    return False
                x-=1
                y+=1

            return True

                
        def bt(i, r):
            if i==n:
                print(r)
                cop=["".join(row) for row in r]
                ans.append(cop)
                return

            for j in range(n):
                if checksafe(i, j, r):
                    r[i][j]='Q'
                    bt(i+1, r)
                    r[i][j]='.'
            
        
        ans=[]
        r=[['.']*n for _ in range(n)]
        bt(0, r)
        return ans



        