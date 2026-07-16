class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        mod=10**9+7
        heapify(nums)
        for i in range(k):
            heappush(nums, heappop(nums)+1)

        r=1
        for i in nums:
            r= (r*i ) % mod

        return r



        