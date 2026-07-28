class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        vis=set()
        c=0
        def dfs(node):
            for j in range(n):
                if isConnected[node][j]==1 and j not in vis:
                    vis.add(j)
                    dfs(j)


        for i in range(n):
            if i not in vis:
                c+=1
                vis.add(i)
                dfs(i)

        return c


        








    









        