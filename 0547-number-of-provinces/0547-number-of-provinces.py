class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            for j in range(n):
                if isConnected[node][j]==1 and visited[j]!=1:
                    visited[j]=1
                    dfs(j)

            return 

        c=0
        n=len(isConnected)
        visited=[0]*n
        for i in range(n):
            if visited[i]==0:
                c+=1
                dfs(i)
                

        return c





        