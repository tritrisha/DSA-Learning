class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f=0
        l=len(nums)-1
        mas=nums.index(min(nums))

        if target==nums[l]:
                return l

        if target==nums[f]:
                return f

        if nums[l]<target:
            l=mas
                
        elif nums[f]>target: 
            f=mas  
                     
        while f<l+1:
            m=(l+f) // 2
            if nums[m]==target:
                return m

            elif nums[m]> target:
                l=m-1
            else:
                f=m+1


        return -1


            
        
        