class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        adj=[0]*n
        for i in range(n):
            adj[i]=[]
            for j in range(n):
                if isConnected[i][j]==1:
                    adj[i].append(j)

        def dfs(node):
            if v[node]==1:
                return 

            v[node]=1
            for j in adj[node]:
                dfs(j)

            return

        c=0
        v=[0]*n
        for i in range(n):
            if v[i]==0:
                c+=1
                dfs(i)
            else:
                continue


        return c










    









        