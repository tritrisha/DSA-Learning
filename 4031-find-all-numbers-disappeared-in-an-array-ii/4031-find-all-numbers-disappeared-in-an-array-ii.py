class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if lower>nums[i]:
                continue
            if lower==nums[i]:
                lower=nums[i]+1
            
            if upper<=nums[i]:
                break
            if lower<nums[i]:
                res.append([lower, nums[i]-1]) 
                lower=nums[i]+1

        
        print(nums)
        print(nums[i])
        if upper>nums[i]:
            res.append([lower, upper])
            
        elif upper<nums[i] and lower<nums[i]:
            if res:
                res.append([nums[i-1]+1, upper])
                print(nums[i])
            else:
                res.append([lower, upper])

        elif upper==nums[i] and nums[i]-1>=lower:
            res.append([lower, nums[i]-1])

        
        return res
        


            

            



            



        