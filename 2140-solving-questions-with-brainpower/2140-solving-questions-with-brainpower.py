class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        def bp(x):
            if x>=len(questions):
                return 0

            if dp[x]!=-1:
                return dp[x]

            dp[x]=max(bp(x+questions[x][1]+1)+questions[x][0], bp(x+1))
            return dp[x]


        dp=[-1]*len(questions)
        return bp(0)
        
        

        
        