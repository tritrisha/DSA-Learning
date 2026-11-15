class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        def part(i, s):
            if s>ss:
                return 0
            if i>=len(stones):
                return s

            if dp[i][s]!=-1:
                return dp[i][s]
        
            dp[i][s]=max(part(i+1, s+stones[i]), part(i+1, s))
            return dp[i][s]
        

        ss=sum(stones)//2
        dp=[[-1]*(ss+1) for _ in range(len(stones))]

        x=abs(2*part(0,0)-sum(stones))
        return x
        