class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr=[-n for n in nums]
        heapify(arr)
        for i in range(k):
            r=heappop(arr)
            
        return -r