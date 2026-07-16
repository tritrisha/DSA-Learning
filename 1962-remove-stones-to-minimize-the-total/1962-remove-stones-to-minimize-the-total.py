class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pl=[-n for n in piles]
        heapify(pl)
        print(pl)
        for i in range(k):
            heappush(pl, floor(heappop(pl)/2))

        
        return -sum(pl)
            

