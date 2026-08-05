class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        le=len(invocations)
        adj=[[] for _ in range(n)]
        for i, j in invocations:
            adj[i].append(j)

        def dfs(i):
            lis[i]=True
            for k in adj[i]:
                if not lis[k]:
                    dfs(k)
        
        lis=[False]*n
        dfs(k)
        for u, v in invocations:
            if not lis[u] and lis[v]:
                return list(range(n))

        ans = []
        for i in range(n):
            if not lis[i]:
                ans.append(i)

        return ans

        
        







            

        