class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost=cost+[0]
        for i in range(2,len(cost)):
            cost[i]= min(cost[i-1], cost[i-2])+cost[i] 
        return cost[-1]





            

    
            
            
            




        


        