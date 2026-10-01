class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        list1=[0]*(max(nums)+1)
        for i in nums:
            list1[i]+=1
        for i in range(len(list1)):
            list1[i]*=i

        print(list1)
        
        for curr in range(2, len(list1)):
            list1[curr]=max(list1[curr]+list1[curr-2], list1[curr-1])

        return list1[-1]

        