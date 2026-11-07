class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        @lru_cache(None)
        def tryy(day, buy, cap):
            if day>=len(prices):
                return 0

            if buy and cap>0:
                return max(-prices[day]+tryy(day+1, 0, cap-1),
                            tryy(day+1, 1, cap) )

            elif not buy:
                return max(prices[day]+tryy(day+1, 1, cap),
                            tryy(day+1, 0, cap) )

            return 0

        return tryy(0, 1, 2)
        