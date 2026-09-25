class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        def jump(i, co):
            if i==0:
                return cost[0]

            if i==1:
                return cost[1]


            if dp[i]!=-1:
                return dp[i]

            dp[i]=min(jump(i-1, cost[i-1]), jump(i-2, cost[i-2])) + co
            return dp[i]

        
        dp=[-1]*(len(cost)+1)
        
        return jump(len(cost), 0)

    
            
            
            




        


        