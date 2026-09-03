class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.presum=[0]*(len(self.nums)+1)
        for i in range(len(self.nums)):
            self.presum[i]=self.presum[i-1]+self.nums[i]


    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right]- self.presum[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)