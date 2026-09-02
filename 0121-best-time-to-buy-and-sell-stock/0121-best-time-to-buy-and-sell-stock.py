class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        bi=0
        m=0
        for i in range(1,len(prices)):
            if buy>prices[i]:
                buy=prices[i]
                bi=i

            
            if prices[i]>buy and bi<i:
                m=max(m, prices[i]-buy)

        return m
            
        