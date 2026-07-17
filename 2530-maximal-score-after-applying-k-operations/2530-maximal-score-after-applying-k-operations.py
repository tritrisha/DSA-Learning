class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score=0
        s=[-n for n in nums]
        heapify(s)
        for i in range(k):
            x=heappop(s)
            heappush(s, x//3)
            score+=x

        return -score
            
            
            
            

        
        