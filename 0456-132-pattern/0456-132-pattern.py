class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        m=-10**9
        nums=nums[::-1]
        l=[nums[0]]
        print(nums)
        for i in nums[1:]:
            if i<l[-1]:
                l.append(i)

            else:
                while l and i>l[-1]:
                    m=l.pop(-1)
                l.append(i)

            if i<m:
                return True
        return False





            
                




            




        